from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.planner import plan_steps
from agent.explainer import explain_results
from agent.router import needs_analysis
from tools.data_tools import (
    inspect_data,
    clean_data,
    groupby_sum,
    category_distribution,
    plot_bar,
)

# ---------------- NODES ----------------

def plan_node(state: AgentState):
    state["plan"] = plan_steps(state["question"])
    return state


def inspect_node(state: AgentState):
    state["inspection"] = inspect_data(state["df"])
    return state


def analysis_node(state: AgentState):
    df = clean_data(state["df"])

    top_branches = groupby_sum(df, "branch_name", "total")
    top_colleges = groupby_sum(df, "college_name", "total")
    category_avg = category_distribution(df)

    state["analysis"] = {
        "top_branches": top_branches.to_dict(orient="records"),
        "top_colleges": top_colleges.to_dict(orient="records"),
        "category_distribution": category_avg,
    }

    state["charts"] = {
        "branches": plot_bar(
            top_branches,
            "branch_name",
            "total",
            "Top Branches by Total Seats",
        ),
        "colleges": plot_bar(
            top_colleges,
            "college_name",
            "total",
            "Top Colleges by Total Seats",
        ),
    }

    return state


def explain_node(state: AgentState):
    state["explanation"] = explain_results(
        state["question"],
        state.get("analysis", {})
    )
    return state



# ---------------- GRAPH ----------------

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("plan", plan_node)
    graph.add_node("inspect", inspect_node)
    graph.add_node("analyze", analysis_node)
    graph.add_node("explain", explain_node)

    graph.set_entry_point("plan")
    graph.add_edge("plan", "inspect")

    # 🔥 CONDITIONAL ROUTING HERE
    graph.add_conditional_edges(
        "inspect",
        needs_analysis,
        {
            "analyze": "analyze",
            "explain": "explain",
        },
    )

    graph.add_edge("analyze", "explain")
    graph.add_edge("explain", END)

    return graph.compile()

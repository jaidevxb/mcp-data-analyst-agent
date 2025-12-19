from utils.file_loader import load_file
from agent.graph import build_graph

graph = build_graph()

def run_agent(file, question):
    df = load_file(file)

    state = {
        "question": question,
        "df": df,
        "plan": "",
        "inspection": {},
        "analysis": {},
        "charts": {},
        "explanation": "",
    }

    return graph.invoke(state)

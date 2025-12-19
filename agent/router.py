def needs_analysis(state) -> str:
    """
    Decide whether to run analysis based on plan + question
    """
    plan = state.get("plan", "").lower()
    question = state.get("question", "").lower()

    keywords = ["analyze", "trend", "top", "compare", "visual", "chart", "pattern"]

    if any(k in plan for k in keywords) or any(k in question for k in keywords):
        return "analyze"

    return "explain"
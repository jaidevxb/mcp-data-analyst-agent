def detect_intent(question: str) -> dict:
    q = question.lower()

    return {
        "needs_analysis": any(word in q for word in ["trend", "pattern", "compare", "top"]),
        "needs_charts": any(word in q for word in ["chart", "plot", "visual"]),
        "needs_report": any(word in q for word in ["export", "report", "pdf"])
    }

from typing import TypedDict, Any
import pandas as pd

class AgentState(TypedDict):
    question: str
    df: pd.DataFrame
    plan: str
    inspection: dict
    analysis: dict
    charts: dict
    explanation: str

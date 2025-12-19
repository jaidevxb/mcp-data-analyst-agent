# agent/planner.py

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

GEMINI_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_KEY:
    raise RuntimeError("❌ GEMINI_API_KEY not found in .env")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   # fast + free-tier friendly
    temperature=0,
    google_api_key=GEMINI_KEY
)

def plan_steps(user_query: str) -> str:
    prompt = f"""
You are an autonomous data analyst agent.

User request:
"{user_query}"

Create a numbered step-by-step analysis plan using ONLY these actions:
- inspect_data
- clean_data
- plot_data
- explain_results

Return only the steps.
"""

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

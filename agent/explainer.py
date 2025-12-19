import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY")
)

def explain_results(question: str, analysis: dict) -> str:
    if not analysis or "top_branches" not in analysis:
        return (
            "Based on the dataset structure and available information, "
            "the data represents engineering seat allocation across colleges, "
            "branches, and reservation categories. The dataset can be used to "
            "understand capacity distribution, popular disciplines, and "
            "policy-driven seat allocation patterns."
        )

    prompt = f"""
You are a data analyst.

User question:
{question}

Computed analysis results (use ONLY this data):

Top Branches:
{analysis.get("top_branches", [])}

Top Colleges:
{analysis.get("top_colleges", [])}

Category-wise Average Seats:
{analysis.get("category_distribution", {})}

Task:
- Derive 3 to 5 meaningful insights
- Explain why each insight matters
- Avoid hallucination
- Be concise and professional
"""

    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content

# 🧠 MCP-Powered Data Analyst Agent

An autonomous AI agent that inspects datasets, performs intelligent analysis, generates visual insights, and explains results in plain English — adapting its behavior dynamically based on the user’s question.

---

## 📌 Project Overview

The **MCP-Powered Data Analyst Agent** is an end-to-end agentic AI application designed to analyze real-world datasets intelligently.  
Unlike traditional data analysis scripts or static dashboards, this system **plans, decides, and executes analysis steps dynamically** based on the user’s query.

The agent can:
- Inspect unknown datasets
- Decide whether deep analysis is required
- Perform aggregations and computations
- Generate visualizations
- Explain insights in natural language
- Skip unnecessary steps when not needed

All decisions are orchestrated using a **LangGraph state machine**, making the system genuinely agentic.

---

## 🧠 How the Agent Works

### 1️⃣ User Input
- User uploads a CSV / Excel dataset
- User asks a natural-language analytical question

---

### 2️⃣ Planning (LLM-Driven)
- An LLM generates a **high-level analysis plan**
- Example steps: `inspect_data → analyze → visualize → explain`

---

### 3️⃣ Intent-Aware Routing (LangGraph)
- The agent decides **which steps to execute**
- Example:
  - Inspection-only questions → skip analysis
  - Trend / visualization questions → run full pipeline

This avoids unnecessary computation and mimics human analyst reasoning.

---

### 4️⃣ Tool Execution
The agent executes tools only when required:
- Dataset inspection (schema, shape, missing values)
- Aggregations (top branches, top colleges, category distribution)
- Chart generation (readable visual summaries)

---

### 5️⃣ Grounded Explanation
- The LLM explains insights **only from computed results**
- No hallucination, no guessing
- Insights are written from both **student** and **policymaker** perspectives when relevant

---

## 📊 Example Capabilities

- Identify top branches and colleges by total seats
- Visualize seat distribution using charts
- Explain trends affecting students and policymakers
- Adapt behavior for inspection-only vs analysis-heavy queries

---

## 🏗 Architecture
User Query  
↓  
LLM Planner  
↓  
LangGraph State Machine  
↓  
Conditional Tool Execution  
↓  
Analysis + Charts  
↓  
LLM-Generated Insights  


---

## 🛠 Tech Stack

- **Python**
- **LangGraph** – agent state orchestration
- **LangChain**
- **Google Gemini API** – planning & explanation
- **Pandas** – data analysis
- **Matplotlib** – visualization
- **Streamlit** – interactive web UI

---

## 🎯 Why This Project Is Different

- Not a static data analysis script
- Not a prompt-only chatbot
- Implements **true agentic behavior**
- Demonstrates **planning, reasoning, and tool orchestration**
- Built on real data, not toy examples
- Implements decision-making at runtime instead of static pipelines


---

## 🧪 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```
Add your API key in a .env file:
GEMINI_API_KEY=your_api_key_here

---

## 🏆 Use Cases

Data analysis automation
Policy & education analytics
Agentic AI demonstrations
Portfolio project for Data Science / AI roles

---

## 📌 Future Improvements

Dynamic chart selection
Multi-dataset comparison
Exportable reports
Advanced LangGraph branching

---
## 👤 Author

Built as a hands-on exploration of Agentic AI + Data Analytics, focusing on correctness, reasoning, and real-world applicability.
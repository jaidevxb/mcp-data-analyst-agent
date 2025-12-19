# app.py

import streamlit as st
from main import run_agent
from utils.report import build_markdown, export_pdf

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="MCP Data Analyst Agent",
    page_icon="📊",
    layout="wide"
)

# -------------------- TITLE --------------------
st.title("🧠 MCP-Powered Data Analyst Agent")
st.caption(
    "Autonomous agent for dataset inspection, analysis, visualization, "
    "and insight generation using agentic AI principles."
)

# -------------------- INPUTS --------------------
uploaded_file = st.file_uploader(
    "Upload CSV / Excel file",
    type=["csv", "xlsx"]
)

question = st.text_input(
    "Ask a data question",
    placeholder="e.g. Find 3 important trends that matter to policymakers"
)

# -------------------- RUN BUTTON --------------------
if st.button("Run Analysis", use_container_width=True):

    if uploaded_file is None:
        st.warning("Please upload a dataset before running the analysis.")
        st.stop()

    if not question.strip():
        st.warning("Please enter a question for the agent.")
        st.stop()

    with st.spinner("🤖 Agent is analyzing the data..."):
        result = run_agent(uploaded_file, question)

    # -------------------- AGENT PLAN --------------------
    st.subheader("🧩 Agent Plan")
    if "plan" in result:
        st.text(result["plan"])
    else:
        st.warning("Agent plan not available.")

    # -------------------- DATASET OVERVIEW --------------------
    st.subheader("📊 Dataset Overview")
    if "inspection" in result:
        st.json(result["inspection"])
    else:
        st.warning("Dataset inspection not available.")

    # -------------------- ANALYSIS RESULTS --------------------
    st.subheader("📈 Key Analysis")

    if "analysis" in result and result["analysis"]:

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### 🔹 Top Branches by Total Seats")
            if result["analysis"].get("top_branches"):
                st.dataframe(
                    result["analysis"]["top_branches"],
                    use_container_width=True
                )
            else:
                st.info("Top branches analysis not available.")

        with col2:
            st.markdown("### 🔹 Top Colleges by Total Seats")
            if result["analysis"].get("top_colleges"):
                st.dataframe(
                    result["analysis"]["top_colleges"],
                    use_container_width=True
                )
            else:
                st.info("Top colleges analysis not available.")

        st.markdown("### 🔹 Average Seats per Category")
        if result["analysis"].get("category_distribution"):
            st.json(result["analysis"]["category_distribution"])
        else:
            st.info("Category-wise distribution not available.")

    else:
        st.warning("No analysis results returned by the agent.")

    # -------------------- CHARTS --------------------
    st.subheader("📊 Visualizations")

    if "charts" in result and result["charts"]:
        for title, chart in result["charts"].items():
            st.image(chart, use_container_width=True)
    else:
        st.info("No charts generated for this question.")

    # -------------------- EXPLANATION --------------------
    st.subheader("🧠 Agent Insights")

    if "explanation" in result:
        st.markdown(result["explanation"])
    else:
        st.warning("No explanation generated.")

    # -------------------- EXPORT --------------------
    st.subheader("📄 Export Report")

    markdown_report = build_markdown(result)

    st.download_button(
        label="⬇️ Download Markdown Report",
        data=markdown_report,
        file_name="analysis_report.md",
        mime="text/markdown"
    )

    if st.button("Generate PDF Report"):
        pdf_path = export_pdf(markdown_report)
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="⬇️ Download PDF Report",
                data=f,
                file_name="analysis_report.pdf",
                mime="application/pdf"
            )


    # -------------------- DONE --------------------
    st.success("✅ Analysis completed successfully.")

# tools/data_tools.py

import pandas as pd
import matplotlib.pyplot as plt
import io
from mcp.registry import mcp_registry


# ---------- BASIC INSPECTION ----------

def inspect_data(df: pd.DataFrame):
    return {
        "shape": df.shape,
        "columns": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict()
    }


# ---------- CLEANING ----------

def clean_data(df: pd.DataFrame):
    # no missing values, return copy for safety
    return df.copy()


# ---------- ANALYSIS TOOLS (NEW) ----------

def groupby_sum(df: pd.DataFrame, group_col: str, value_col: str):
    """
    Aggregate data by summing value_col grouped by group_col
    """
    result = (
        df.groupby(group_col)[value_col]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    return result.head(10)


def category_distribution(df: pd.DataFrame):
    """
    Compute average seats per category
    """
    categories = ["oc", "bc", "bcm", "mbc", "sc", "sca", "st"]
    return df[categories].mean().to_dict()


# ---------- VISUALIZATION ----------

def plot_bar(df, x, y, title):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(df[x], df[y])
    ax.set_title(title)
    ax.invert_yaxis()
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    plt.close()
    return buf




def plot_category_pie(category_dict: dict):
    fig, ax = plt.subplots()
    ax.pie(
        category_dict.values(),
        labels=category_dict.keys(),
        autopct="%1.1f%%",
        startangle=90
    )
    ax.set_title("Average Seat Distribution by Category")
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()
    return buf

# ---------- MCP REGISTRATION ----------

mcp_registry.register("inspect_data", inspect_data)
mcp_registry.register("clean_data", clean_data)
mcp_registry.register("groupby_sum", groupby_sum)
mcp_registry.register("category_distribution", category_distribution)
mcp_registry.register("plot_bar", plot_bar)
mcp_registry.register("plot_category_pie", plot_category_pie)


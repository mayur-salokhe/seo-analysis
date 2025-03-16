import streamlit as st
import pandas as pd
import plotly.express as px
from serpapi_scraper import get_serp_results
from database import fetch_rankings, fetch_top_competitors, check_search_quota

# 🏆 App Title
st.title("🔍 SEO Performance Analysis Dashboard")

# 📊 Display Remaining Monthly Search Quota
remaining_searches = check_search_quota()
st.warning(f"Remaining Searches for this month: {remaining_searches}/100")

# 🔎 Keyword Input
keyword = st.text_input("Enter Keyword", "")

if st.button("Fetch SERP Data"):
    if remaining_searches > 0:
        result = get_serp_results(keyword)
        if "success" in result:
            st.success(result["success"])
        elif "error" in result:
            st.error(result["error"])
    else:
        st.error("Monthly SerpAPI search limit reached!")


# 📊 Fetch and Display Keyword Ranking Data
st.subheader("📌 Keyword Ranking History")
data = fetch_rankings()
df = pd.DataFrame(data, columns=["ID", "Keyword", "Rank", "Previous Rank", "Title", "URL", "Domain", "Snippet", "Date"])

if not df.empty:
    # 📈 Ranking Trends
    st.dataframe(df)
    fig = px.line(df, x="Date", y="Rank", color="Keyword", title="📈 Ranking Trends")
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig)

    # 📊 Ranking Distribution
    st.subheader("📊 Keyword Ranking Distribution")
    df["Ranking Group"] = pd.cut(df["Rank"], bins=[0, 10, 20, 50, 100, float("inf")], labels=["Top 10", "Top 20", "Top 50", "Top 100", "Beyond 100"])
    st.bar_chart(df["Ranking Group"].value_counts().sort_index())

    # 🔄 Rank Changes
    st.subheader("🔄 Keyword Rank Changes")
    df["Change"] = df["Previous Rank"] - df["Rank"]
    st.dataframe(df.sort_values(by="Change", ascending=False)[["Keyword", "Previous Rank", "Rank", "Change"]])

    # ✨ Featured Snippet Tracking
    st.subheader("✨ Featured Snippets Analysis")
    snippet_count = df["Snippet"].sum()
    st.metric("Snippets Captured", snippet_count)

    # 🏆 Competitor Analysis
    st.subheader("🏆 Competitor Performance")
    competitor_data = fetch_top_competitors()
    comp_df = pd.DataFrame(competitor_data, columns=["Domain", "Appearances"])
    st.bar_chart(comp_df.set_index("Domain"))
else:
    st.warning("No ranking data available. Fetch data to see insights!")

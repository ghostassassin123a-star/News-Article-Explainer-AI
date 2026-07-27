from pdf_export import create_pdf
import streamlit as st

from ai import analyze_article
from utils import article_stats

# -----------------------------
# LOAD CSS
# -----------------------------
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="News Article Explainer AI",
    page_icon="📰",
    layout="wide"
)

load_css()

# ==========================
# HEADER
# ==========================
st.title("📰 AI News Article Explainer")

st.markdown("""
Analyze any news article using **Google Gemini AI**.

### ✨ Features
- 📄 AI Summary
- 🔑 Five Key Points
- 😊 Sentiment Analysis
- 👤 Important People
- 📍 Important Places
- ⚠️ Fake News Risk
- 👦 Easy Explanation
- ⏱ Reading Time
""")

st.divider()

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:

    st.header("🤖 AI News Explainer")

    st.info("""
This application uses **Google Gemini AI**
to analyze long news articles and explain
them in simple language.
""")

    st.divider()

    st.subheader("✨ Features")

    st.markdown("""
- AI Summary
- Five Key Points
- Sentiment Analysis
- Important People
- Important Places
- Fake News Risk
- Easy Explanation
- Download Results
""")



# -----------------------------
# SAMPLE ARTICLE
# -----------------------------
if "article" not in st.session_state:
    st.session_state.article = ""

sample_article = """
NASA has announced the successful launch of a new Earth observation satellite designed to monitor climate change and natural disasters. The satellite will provide high-resolution images of Earth's atmosphere, oceans, and forests. Scientists believe the mission will improve weather forecasting, disaster response, and environmental research. The mission is expected to operate for at least seven years and collect valuable data for researchers worldwide.
"""


  # -----------------------------
# CALLBACKS
# -----------------------------
def load_sample():
    st.session_state["article"] = sample_article

def clear_article():
    st.session_state["article"] = ""  


# -----------------------------
# ARTICLE INPUT
# -----------------------------
st.subheader("📰 Paste News Article")

col1, col2 = st.columns([1, 3])

with col1:
    st.button(
        "📰 Load Sample",
        use_container_width=True,
        on_click=load_sample
    )

with col2:
    st.caption("Paste any news article below and click Analyze.")

article = st.text_area(
    "News Article",
    value=st.session_state.get("article", ""),
    height=350,
    placeholder="Paste the complete news article here..."
)
st.session_state["article"] = article
# -----------------------------
# ARTICLE STATS
# -----------------------------
if article.strip():

    st.subheader("📊 Article Statistics")

    stats = article_stats(article)

    c1, c2, c3 = st.columns(3)

    c1.metric("📝 Words", stats["Words"])
    c2.metric("🔠 Characters", stats["Characters"])
    c3.metric("⏱ Reading Time", stats["Reading Time"])

# -----------------------------
# BUTTONS
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    analyze = st.button(
        "🤖 Analyze Article",
        use_container_width=True
    )

with col2:
    st.button(
        "🗑 Clear",
        use_container_width=True,
        on_click=clear_article
    )

# -----------------------------
# ANALYSIS
# -----------------------------
if analyze:

    if not article.strip():
        st.warning("Please paste a news article first.")
        st.stop()

    with st.spinner("🤖 AI is analyzing the article..."):
        result = analyze_article(article)

    st.success("✅ Analysis Complete!")

    st.subheader("✨ AI Analysis")

    st.markdown(result)

    # Create PDF
    pdf_file = create_pdf(result)

    # Download Button
    with open(pdf_file, "rb") as pdf:

        st.download_button(
            "📄 Download Professional PDF",
            data=pdf,
            file_name="AI_News_Analysis_Report.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

st.divider()

st.caption(
    "Developed as an AI-powered News Article Explainer using Python, Streamlit, and Google Gemini AI."
)
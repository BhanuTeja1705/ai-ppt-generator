import streamlit as st
import asyncio
import os
import traceback

from my_ppt_agent import run_agent

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI PPT Generator",
    page_icon="📊",
    layout="wide"
)

# =========================================
# CUSTOM CSS
# =========================================

st.markdown("""
<style>

.main {
    background-color: #0f172a;
    color: white;
}

.stTextInput input {
    border-radius: 12px;
    padding: 12px;
}

.stButton button {
    background-color: #6366f1;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton button:hover {
    background-color: #4f46e5;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================

st.title("🚀 AI Presentation Generator")

st.caption(
    "Modern AI PPT generation using MCP + LangChain + HuggingFace"
)

st.divider()

# =========================================
# SIDEBAR
# =========================================

with st.sidebar:

    st.header("⚙️ Presentation Settings")

    slides = st.slider(
        "Number of Slides",
        5,
        20,
        10
    )

    style = st.selectbox(
        "Presentation Style",
        [
            "Professional",
            "Modern Startup",
            "Minimal Clean",
            "Investor Pitch"
        ]
    )

    st.divider()

    st.info(
        f"""
        📑 Slides: {slides}

        ✨ Style: {style}
        """
    )

# =========================================
# MAIN INPUT
# =========================================

topic = st.text_input(
    "Enter Presentation Topic",
    placeholder="Example: AI in Healthcare"
)

# =========================================
# GENERATE BUTTON
# =========================================

if st.button("✨ Generate AI Presentation"):

    if topic.strip() == "":

        st.warning("Please enter a topic.")

    else:

        try:

            with st.spinner(
                "Generating Modern AI Presentation..."
            ):

                asyncio.run(
                    run_agent(
                        topic,
                        slides,
                        style
                    )
                )

            st.success(
                "✅ Presentation Generated Successfully!"
            )

        except Exception:

            st.error(traceback.format_exc())

# =========================================
# DOWNLOAD SECTION
# =========================================

if os.path.exists("final_output.pptx"):

    st.divider()

    st.subheader("📥 Download Presentation")

    with open("final_output.pptx", "rb") as f:

        st.download_button(
            label="Download PPTX",
            data=f,
            file_name="AI_Presentation.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )

# =========================================
# FOOTER
# =========================================

st.divider()

st.caption(
    "Built with MCP + LangChain + HuggingFace + Streamlit"
)

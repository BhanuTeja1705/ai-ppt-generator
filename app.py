import streamlit as st
import asyncio
from my_ppt_agent import run_agent
import os
import traceback

st.title("📊 AI PPT Generator (MCP + LLM)")

topic = st.text_input("Enter topic")

if st.button("Generate PPT"):
    if topic:
        try:
            asyncio.run(run_agent(topic))
            st.success("✅ PPT Created Successfully!")
        except Exception:
            st.error(traceback.format_exc())

if os.path.exists("final_output.pptx"):
    with open("final_output.pptx", "rb") as f:
        st.download_button("📥 Download PPT", f, "final_output.pptx")
from dotenv import load_dotenv
import os

load_dotenv()
import asyncio
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage

# ✅ Better topic extraction
def get_topic(text):
    text = text.lower()
    if "presentation on" in text:
        topic = text.split("presentation on")[-1]
    elif "on" in text:
        topic = text.split("on", 1)[-1]
    else:
        topic = text
    return topic.strip().title()

# ✅ LLM content generation
async def generate_facts_llm(topic):
    try:
        llm = ChatHuggingFace(
            llm=HuggingFaceEndpoint(
                repo_id="Qwen/Qwen2.5-7B-Instruct",
                max_new_tokens=300,
                temperature=0.7
            )
        )

        response = await llm.ainvoke([
            HumanMessage(content=f"Give 12 short bullet points about {topic}")
        ])

        lines = response.content.split("\n")

        facts = []
        for l in lines:
            l = l.strip("-•123456789. ")
            if len(l.split()) > 3:
                facts.append(l)

        return facts[:12]

    except Exception:
        return [f"{topic} concept"] * 12

# ✅ Slide planner
def create_plan(topic, facts):
    return [
        {"title": topic, "bullets": []},
        {"title": "Introduction", "bullets": facts[0:3]},
        {"title": "Details", "bullets": facts[3:6]},
        {"title": "Process", "bullets": facts[6:9]},
        {"title": "Conclusion", "bullets": facts[9:12]},
    ]

# 🔥 MAIN AGENT
async def run_agent(prompt):

    topic = get_topic(prompt)

    facts = await generate_facts_llm(topic)
    plan = create_plan(topic, facts)

    ppt_params = StdioServerParameters(
        command="python",
        args=["ppt_mcp_server.py"]
    )

    async with stdio_client(ppt_params) as (r, w):
        async with ClientSession(r, w) as ppt:
            await ppt.initialize()
            tools = await load_mcp_tools(ppt)
            tool_map = {t.name: t for t in tools}

            await tool_map["create_presentation"].ainvoke({})

            for slide in plan:
                if slide["bullets"]:
                    await tool_map["add_content_slide"].ainvoke({
                        "title": slide["title"],
                        "points": slide["bullets"]
                    })
                else:
                    await tool_map["add_title_slide"].ainvoke({
                        "title": slide["title"],
                        "subtitle": "AI Generated Presentation"
                    })

            await tool_map["save_presentation"].ainvoke({
                "filename": "final_output.pptx"
            })

    print("✅ PPT Generated!")

if __name__ == "__main__":
    user_input = input("Enter topic: ")
    asyncio.run(run_agent(user_input))
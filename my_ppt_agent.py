from dotenv import load_dotenv
import asyncio

load_dotenv()

from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters

from langchain_mcp_adapters.tools import load_mcp_tools

from langchain_huggingface import (
    ChatHuggingFace,
    HuggingFaceEndpoint
)

from langchain_core.messages import HumanMessage

# =========================================
# TOPIC EXTRACTION
# =========================================

def get_topic(text):

    text = text.lower()

    if "presentation on" in text:
        topic = text.split("presentation on")[-1]

    elif "on" in text:
        topic = text.split("on", 1)[-1]

    else:
        topic = text

    return topic.strip().title()

# =========================================
# SLIDE TYPE DETECTION
# =========================================

def detect_slide_type(title):

    title = title.lower()

    if any(word in title for word in [
        "workflow",
        "process",
        "steps",
        "architecture",
        "implementation"
    ]):
        return "timeline"

    elif any(word in title for word in [
        "applications",
        "benefits",
        "features",
        "technologies",
        "advantages",
        "future trends"
    ]):
        return "cards"

    return "content"

# =========================================
# GENERATE AI STRUCTURE
# =========================================

async def generate_presentation_structure(
    topic,
    slide_count,
    style
):

    try:

        llm = ChatHuggingFace(
            llm=HuggingFaceEndpoint(
                repo_id="Qwen/Qwen2.5-7B-Instruct",
                max_new_tokens=2500,
                temperature=0.5
            )
        )

        actual_slides = max(slide_count - 1, 3)

        prompt = f"""
Create a PROFESSIONAL presentation on:

{topic}

Requirements:
- Create exactly {actual_slides} slides
- Follow logical educational flow
- Start from beginner concepts
- Gradually move to advanced concepts
- End with conclusion
- Content must stay highly relevant
- Use {style} presentation style

Preferred Structure:
1. Introduction
2. Core Concepts
3. How It Works
4. Technologies
5. Applications
6. Benefits
7. Challenges
8. Future Trends
9. Conclusion

Rules:
- 5 to 7 bullet points per slide
- Each point 8 to 14 words
- Add meaningful explanation phrases
- Include practical details
- Make slides information rich
- Avoid single-word bullets

Return ONLY in this format:

Slide: Introduction
- point
- point
- point
- point

Slide: Conclusion
- point
- point
- point
- point
"""

        response = await llm.ainvoke([
            HumanMessage(content=prompt)
        ])

        return response.content

    except Exception:

        return f"""
Slide: Introduction
- Overview of {topic}
- Industry importance
- Core fundamentals
- Modern innovations

Slide: Core Concepts
- Smart automation systems
- Real time monitoring
- AI driven optimization
- Scalable architecture

Slide: Applications
- Enterprise automation systems
- Predictive analytics platforms
- Smart recommendation engines
- Workflow optimization systems

Slide: Benefits
- Improved operational efficiency
- Faster business decisions
- Reduced operational costs
- Enhanced user experience

Slide: Conclusion
- Future ready innovation
- Sustainable digital transformation
- Scalable enterprise adoption
- Long term growth
"""

# =========================================
# PARSE STRUCTURE
# =========================================

def parse_presentation_structure(text):

    slides = []

    current_slide = None

    for line in text.split("\n"):

        line = line.strip()

        # New Slide
        if line.lower().startswith("slide:"):

            if current_slide:
                slides.append(current_slide)

            current_slide = {
                "title": line.replace("Slide:", "").strip(),
                "points": []
            }

        # Bullet Point
        elif line.startswith("-"):

            point = line.replace("-", "").strip()

            if current_slide and point:
                current_slide["points"].append(point)

    if current_slide:
        slides.append(current_slide)

    return slides

# =========================================
# CREATE PRESENTATION PLAN
# =========================================

def create_plan(topic, structured_slides):

    plan = []

    # -----------------------------------
    # TITLE SLIDE
    # -----------------------------------

    plan.append({
        "type": "title",
        "title": topic,
        "subtitle": "AI Generated Presentation"
    })

    # -----------------------------------
    # CONTENT FLOW
    # -----------------------------------

    for i, slide in enumerate(structured_slides):

        title = slide["title"]

        content = slide["points"]

        lower_title = title.lower()

        # Introduction
        if i == 0 or "introduction" in lower_title:

            slide_type = "content"

        # Conclusion
        elif (
            i == len(structured_slides) - 1 or
            "conclusion" in lower_title
        ):

            slide_type = "content"

            content = content[:3]

        # Smart Detection
        else:

            slide_type = detect_slide_type(title)

        plan.append({
            "type": slide_type,
            "title": title,
            "content": content
        })

    return plan

# =========================================
# MAIN AGENT
# =========================================

async def run_agent(
    prompt,
    slide_count=10,
    style="Professional"
):

    print("\n🚀 Starting AI PPT Generation...\n")

    # Topic
    topic = get_topic(prompt)

    print("📌 Topic:", topic)

    # Generate Structure
    structure_text = await generate_presentation_structure(
        topic,
        slide_count,
        style
    )

    print("🧠 AI Structure Generated")

    # Parse Slides
    structured_slides = parse_presentation_structure(
        structure_text
    )

    print("📝 Structured Slides Parsed")

    # Create Plan
    plan = create_plan(
        topic,
        structured_slides
    )

    print("📊 Presentation Plan Ready")

    # =========================================
    # PPT MCP SERVER
    # =========================================

    ppt_params = StdioServerParameters(
        command="python",
        args=["ppt_mcp_server.py"]
    )

    async with stdio_client(ppt_params) as (r, w):

        async with ClientSession(r, w) as ppt:

            await ppt.initialize()

            tools = await load_mcp_tools(ppt)

            tool_map = {
                t.name: t for t in tools
            }

            # Create PPT
            await tool_map["create_presentation"].ainvoke({})

            # Generate Slides
            for slide in plan:

                slide_type = slide["type"]

                # Title Slide
                if slide_type == "title":

                    await tool_map["add_title_slide"].ainvoke({
                        "title": slide["title"],
                        "subtitle": slide["subtitle"]
                    })

                # Cards Slide
                elif slide_type == "cards":

                    await tool_map["add_cards_slide"].ainvoke({
                        "title": slide["title"],
                        "points": slide["content"]
                    })

                # Timeline Slide
                elif slide_type == "timeline":

                    await tool_map["add_timeline_slide"].ainvoke({
                        "title": slide["title"],
                        "steps": slide["content"]
                    })

                # Content Slide
                else:

                    await tool_map["add_content_slide"].ainvoke({
                        "title": slide["title"],
                        "points": slide["content"]
                    })

            # Save PPT
            await tool_map["save_presentation"].ainvoke({
                "filename": "final_output.pptx"
            })

    print("\n✅ PPT Generated Successfully!")
    print("📂 Saved as final_output.pptx\n")

# =========================================
# ENTRY POINT
# =========================================

if __name__ == "__main__":

    user_input = input("Enter topic: ")

    asyncio.run(
        run_agent(
            user_input,
            10,
            "Professional"
        )
    )

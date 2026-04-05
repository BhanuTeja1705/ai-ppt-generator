from mcp.server.fastmcp import FastMCP
from pptx import Presentation

mcp = FastMCP("Custom PPT MCP Server")

prs = None

@mcp.tool()
def create_presentation():
    global prs
    prs = Presentation()
    return "Created"

@mcp.tool()
def add_title_slide(title: str, subtitle: str):
    global prs
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = title
    slide.placeholders[1].text = subtitle
    return "Title added"

@mcp.tool()
def add_content_slide(title: str, points: list):
    global prs
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = title
    slide.placeholders[1].text = "\n".join(points)
    return "Slide added"

@mcp.tool()
def save_presentation(filename: str):
    global prs
    prs.save(filename)
    return "Saved"

if __name__ == "__main__":
    mcp.run()
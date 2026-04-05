from mcp.server.fastmcp import FastMCP
from ddgs import DDGS
import hashlib

mcp = FastMCP("Custom Research Server")

@mcp.tool()
def get_topic_facts(topic: str) -> list:
    results = []

    try:
        with DDGS() as search:
            data = list(search.text(f"{topic} facts", max_results=5))
            for item in data:
                text = item.get("body", "")
                if text:
                    results.append(text.split(".")[0])
    except:
        pass

    return results[:10]

@mcp.tool()
def get_image(query: str) -> str:
    seed = int(hashlib.md5(query.encode()).hexdigest(), 16) % 1000
    return f"https://picsum.photos/seed/{seed}/800/600"

if __name__ == "__main__":
    mcp.run()
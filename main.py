# main.py
from fastmcp import FastMCP
import random

mcp = FastMCP("MCP Server")

FACTS = [
    "Bananas are berries, but strawberries are not.",
    "Octopuses have three hearts.",
    "Your fingerprints have a 1 in 64 billion chance of matching someone else’s.",
    "Honey never spoils — archaeologists found 3,000-year-old edible honey.",
    "The Eiffel Tower can grow 15 cm taller during summer."
]

@mcp.tool()
def get_unique_fact():
    """Return a random unique fact"""
    return random.choice(FACTS)

if __name__ == "__main__":
    mcp.run()
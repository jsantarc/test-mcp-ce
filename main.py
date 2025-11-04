# main.py
from fastapi import FastAPI
import random

app = FastAPI(title="Toy MCP Server")

FACTS = [
    "Bananas are berries, but strawberries are not.",
    "Octopuses have three hearts.",
    "Your fingerprints have a 1 in 64 billion chance of matching someone else’s.",
    "Honey never spoils — archaeologists found 3,000-year-old edible honey.",
    "The Eiffel Tower can grow 15 cm taller during summer."
]

@app.get("/get_unique_fact")
def get_unique_fact():
    """Return a random unique fact"""
    return {"fact": random.choice(FACTS)}

if __name__ == "__main__":
    app.run()
from fastapi import FastAPI
from app.brain.llm import ask_ai
from app.memory.memory import save_memory
from app.database.db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"status": "Victorial AI Running"}


@app.get("/chat")
def chat(message: str):

    save_memory(message)

    reply = ask_ai(message)

    return {
        "user": message,
        "ai": reply
    }

@app.get("/memories")
def memories():

    from app.memory.memory import get_memories

    data = get_memories()

    return [
        {
            "id": m.id,
            "content": m.content,
            "category": m.category
        }
        for m in data
    ]

@app.get("/project")
def project():

    from app.memory.memory import search_project

    return {
        "project": search_project()
    }
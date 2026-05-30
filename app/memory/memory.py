from app.database.db import SessionLocal
from app.models.models import Memory

def save_memory(content, category="general"):
    db = SessionLocal()

    memory = Memory(
        content=content,
        category=category
    )

    db.add(memory)
    db.commit()
    db.close()


def get_memories(limit=10):
    db = SessionLocal()

    memories = (
        db.query(Memory)
        .order_by(Memory.id.desc())
        .limit(limit)
        .all()
    )

    db.close()

    return memories

def get_memory_context(limit=20):

    memories = get_memories(limit)

    context = ""

    for memory in memories:
        context += f"- {memory.content}\n"

    return context

def search_project():

    memories = get_memories(50)

    for memory in memories:

        text = memory.content.lower()

        if "my project is" in text:
            return memory.content

    return None

def search_memory(keyword):

    memories = get_memories(100)

    results = []

    for memory in memories:

        if keyword.lower() in memory.content.lower():
            results.append(memory.content)

    return results
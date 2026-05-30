from app.memory.memory import search_project

def ask_ai(prompt):

    prompt_lower = prompt.lower()

    if "what is my project" in prompt_lower:

        project = search_project()

        if project:
            return f"Your project is {project.replace('My project is ', '')}"

        return "I do not know your project yet."

    return "Victorial AI Online"
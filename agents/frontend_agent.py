from agno.agent import Agent
from agno.models.google import Gemini
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

frontend_agent = Agent(
    name="Frontend Agent",
    role="Generate professional frontend code.",
    model=Gemini(id="gemini-1.5-flash", api_key=API_KEY),
    instructions=[
        "Decide the best frontend language/framework based on requirements.",
        "Generate professional-level code in HTML, CSS, JavaScript, TypeScript, React, Vue, Angular, or Svelte.",
        "Ensure clean, maintainable, and well-documented code.",
    ],
    markdown=True,
)

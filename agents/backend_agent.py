from agno.agent import Agent
from agno.models.google import Gemini
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

backend_agent = Agent(
    name="Backend Agent",
    role="Generate professional backend code.",
    model=Gemini(id="gemini-1.5-flash", api_key=API_KEY),
    instructions=[
        "Decide the best backend language/framework based on requirements.",
        "Generate professional-level code in Node.js, Django, Flask, FastAPI, Spring Boot, Laravel, CodeIgniter, Ruby on Rails, ASP.NET Core, Go, Rust, or Kotlin.",
        "Ensure scalability, security, and clean architecture.",
    ],
    markdown=True,
)

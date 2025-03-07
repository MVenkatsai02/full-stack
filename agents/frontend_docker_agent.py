from agno.agent import Agent
from agno.models.google import Gemini
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

frontend_docker_agent = Agent(
    name="Frontend Docker Agent",
    role="Generate Dockerfile for the frontend.",
    model=Gemini(id="gemini-1.5-flash", api_key=API_KEY),
    instructions=[
        "Generate an optimized Dockerfile for the frontend.",
        "Ensure best practices like multi-stage builds if necessary.",
    ],
    markdown=True,
)

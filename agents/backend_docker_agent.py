from agno.agent import Agent
from agno.models.google import Gemini
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

backend_docker_agent = Agent(
    name="Backend Docker Agent",
    role="Generate Dockerfile for the backend.",
    model=Gemini(id="gemini-1.5-flash", api_key=API_KEY),
    instructions=[
        "Generate an optimized Dockerfile for the backend.",
        "Ensure best practices like small image size and environment variable security.",
    ],
    markdown=True,
)

import streamlit as st
import os
from dotenv import load_dotenv
from agents.frontend_agent import frontend_agent
from agents.backend_agent import backend_agent
from agents.frontend_docker_agent import frontend_docker_agent
from agents.backend_docker_agent import backend_docker_agent

# Load API Key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

st.title("Multi-Agent AI Code Generator 🚀")
st.subheader("Generate Full-Stack Code and Dockerfiles Using AI Agents")

project_description = st.text_area("Describe your project requirements:", "")

if st.button("Generate Code"):
    if project_description:
        with st.spinner("Generating Frontend Code..."):
            frontend_code = frontend_agent.run(project_description).content
        
        with st.spinner("Generating Backend Code..."):
            backend_code = backend_agent.run(project_description).content

        with st.spinner("Generating Frontend Dockerfile..."):
            frontend_dockerfile = frontend_docker_agent.run(frontend_code).content

        with st.spinner("Generating Backend Dockerfile..."):
            backend_dockerfile = backend_docker_agent.run(backend_code).content

        st.success("Code Generation Complete!")
        
        st.subheader("Frontend Code:")
        st.code(frontend_code, language="javascript")

        st.subheader("Backend Code:")
        st.code(backend_code, language="python")

        st.subheader("Frontend Dockerfile:")
        st.code(frontend_dockerfile, language="docker")

        st.subheader("Backend Dockerfile:")
        st.code(backend_dockerfile, language="docker")
    
    else:
        st.warning("Please enter a project description.")

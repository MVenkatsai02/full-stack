# Use an official Python image as base
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . .

# Install system dependencies (optional, if needed)
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit runs on
EXPOSE 8501

# Set environment variables (ensure .env file is provided)
ENV GOOGLE_API_KEY="your_api_key_here"

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

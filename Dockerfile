# Use official Python slim image
FROM python:3.13-slim

RUN apt-get update && apt-get install -y build-essential python3-dev

# Set working directory inside container
WORKDIR /usr/src/app

# Copy dependency files first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI application code
COPY . .

# Expose the port the app runs on
EXPOSE 8021

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8021"]
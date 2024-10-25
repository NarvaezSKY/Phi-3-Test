# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set environment variables to avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory in the container
WORKDIR /app

#Update pip
RUN pip install --no-cache-dir --upgrade pip

#Install Git (required by models dependencies)
RUN apt-get update && apt-get install -y build-essential git

# Install dev dependencies before requirements (to avoid requirements conflicts)
RUN pip install --no-cache-dir packaging>=21.0
RUN pip install --no-cache-dir torch>=2.3.1

# Copy requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the models directory into the container
COPY models/ ./models/

# Copy only necessary files to avoid duplication
COPY main.py ./main.py

# COPY test.py to run test in the container bash
COPY test.py ./test.py

# Expose port 8000 for the Flask app
EXPOSE 8000

# Run main.py when the container launches
CMD ["python", "main.py"]
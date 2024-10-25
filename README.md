# LLM Docker Deployment Test

## Introduction

This repository is part of a technical test designed to assess your ability to work with language models, Docker containers, and cloud services. The goal is to set up any small language model from Hugging Face inside a Docker image, enabling it to handle questions via a handler script.

## Objectives

- Understand cloud-based AI platforms like Hugging Face.
- Download and integrate a pre-trained language model.
- Build and configure Docker containers for AI services.
- Implement and test a handler script to interact with the model.
- Deploy the Docker image and test its functionality.
- Share the Docker image for external testing.

## Folder Structure

your_repo/ 
├── Dockerfile
├── main.py
├── test.py 
├── download_model.py
├── requirements.txt
├── models/ 
│ └── (model files will be stored here after running download_model.py)
└── README.md


## Prerequisites

- **Docker** installed on your machine.
- **Python 3.7** or higher (optional, for running test scripts locally).
- **Docker Hub account** (for pushing the image).

---

## Steps to Follow

### 1. Unzip the Workspace

- **Unzip** the provided workspace to your local machine.
- **Navigate** into the unzipped directory.

### 2. Download the small LLM Model

- **Download** the small model you chose using the helper script.

Ensure the model files are placed in the models/ directory within your project.

### 3. Build the Docker Image
Use the provided Dockerfile to build the Docker image.

Tag the image with your Docker Hub username, a chosen image name, and a version tag (e.g., v1).

docker build -t your-dockerhub-username/your-image-name:tag .
Example Tag Format: your-dockerhub-username/your-image-name:tag

### 4. Run the Docker Container Locally (Optional)
Run the Docker container using the image you just built.

docker run -p 8000:8000 your-dockerhub-username/your-image-name:tag
Map the container's port to a port on your host machine (e.g., map port 8000 in the container to port 8000 on your host).

This step allows you to test the container locally before pushing it to Docker Hub.

### 5. Test the Model Locally
In a new terminal window, run the test script provided in the repository:

python test.py
The test script sends a sample prompt to the model's API endpoint.

Verify that the model responds appropriately to the input prompt.

### 6. Push the Docker Image to Docker Hub
Log in to your Docker Hub account via the command line using your Docker Hub credentials:

docker login
Push your tagged Docker image to Docker Hub:

docker push your-dockerhub-username/your-image-name:tag
After pushing, ensure that the repository is set to public in your Docker Hub account settings so others can access it.

### . Share the Docker Image Name
Provide the full Docker image name, including your Docker Hub username, image name, and tag.

Example Image Name: your-dockerhub-username/your-image-name:tag
Sharing this name allows others to pull and test your Docker image.

## Expected Results

Successful Docker Image Build:
The Docker image builds without any errors, indicating all dependencies are correctly installed and the Dockerfile is properly configured.

Container Running Smoothly:
The Flask API inside the container starts successfully and listens on the specified port.
There are no runtime errors when the container is launched.

Model Responding Appropriately:
When you run the test script, the model provides meaningful and accurate responses to the input prompts.
The API endpoint correctly processes requests and returns responses in the expected format.

Docker Image Available Publicly:
The Docker image is successfully pushed to Docker Hub.
The image is set to public, allowing others to pull it without authentication issues.

External Testing Possible:
Others can pull your Docker image using the provided image name.
They can run the container and test the model following your instructions.
The model responds correctly during external testing, confirming the deployment works outside your local environment.

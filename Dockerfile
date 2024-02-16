# syntax=docker/dockerfile:1

FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Make sure to copy the ML model file into the container
COPY iris_model.pkl .

# Command to run the app 
CMD ["python", "server.py"]
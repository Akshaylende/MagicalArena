# Use an official Python runtime as a parent image
From Python:3.9-slim

# Set the working directory in the container
WORKDIR /home/app

# Copy required Files into the Docker Image
Copy ..

# Run main.py when the container launches
CMD["python", "main.py"]


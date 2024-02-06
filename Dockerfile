# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN apt-get update \
    && pip install --no-cache-dir -r src/requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python", "src/app.py"]
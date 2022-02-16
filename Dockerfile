# The docker file is a blueprint for creating docker images. 
# Docker container is a an instance of a docker image

# This is our base image!
FROM python:3.8.8-slim-buster 

# Working Directory
WORKDIR /my_app

# copy the requirements to the working directory
COPY requirements.txt .

# Install packages from requirements.txt
RUN pip install -r requirements.txt

# Copy source code to working directory
COPY . ./my_app

# what are the entry point for the container - what to run when just doing docker run -t <docker name>
ENTRYPOINT [ "python", "./my_app/app.py"]
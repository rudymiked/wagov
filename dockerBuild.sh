#!/bin/bash

# Variables
DOCKER_USERNAME="rudymiked"
DOCKER_IMAGE_NAME="rudymiked/ccfssearch"
DOCKER_TAG="latest"

# Build the Docker image
echo "Building Docker image..."
docker build -t $DOCKER_IMAGE_NAME:$DOCKER_TAG .

# Log in to Docker Hub
echo "Logging in to Docker Hub..."
docker login -u $DOCKER_USERNAME

# Push the Docker image to Docker Hub
echo "Pushing Docker image to Docker Hub..."
docker push $DOCKER_IMAGE_NAME:$DOCKER_TAG

echo "Docker image pushed successfully!"
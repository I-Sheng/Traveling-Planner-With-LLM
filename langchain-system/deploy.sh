#!/bin/bash
set -e
source ../.env

# Build the Docker image
docker build -t recommend .

# Remove any existing container with the same name
docker rm -f recommend || true

# Run the new container with the environment variable
docker run -d -p 5001:5001 --env OPENAI_API_KEY=$OPENAI_API_KEY recommend


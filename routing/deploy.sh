#!/bin/bash
set -e
source ../.env
cp ../data/sitesData.json ./data

# Build the Docker image
docker build -t routing .

# Remove any existing container with the same name
#docker container rm routing1 || true

# Run the new container with the environment variable
docker run -d -p 5002:5002 --env GOOGLE_MAP_API_KEY=$GOOGLE_MAP_API_KEY routing

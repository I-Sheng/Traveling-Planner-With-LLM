#!/bin/bash
docker build -t frontend_app .
docker container run --network langchain --name frontend-container -p 3000:3000 frontend_app

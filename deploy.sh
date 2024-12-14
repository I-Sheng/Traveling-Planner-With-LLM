#!/bin/bash
docker network create langchain
cd langchain-system
bash deploy.sh
cd ../routing
bash deploy.sh
cp data/sitesData.json web/data/
cd ../web
bash deploy.sh

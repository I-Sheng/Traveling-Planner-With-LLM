#!/bin/bash
cd langchain-system
bash deploy.sh
cd ../routing
bash deploy.sh
cp data/sitesData.json web/data/

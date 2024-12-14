#!/bin/bash
docker build -t nextjs-docker .
docker run -d -p 80:80 nextjs-docker
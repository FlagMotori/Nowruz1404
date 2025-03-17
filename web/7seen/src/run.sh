#!/bin/bash

docker kill 7seen
docker rm 7seen
docker build . -t 7seen-image && docker run --name 7seen -it -d --publish "80:8000" 7seen-image

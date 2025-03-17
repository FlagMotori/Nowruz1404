#!/bin/bash

docker kill "ecal"
docker rm "ecal"
docker build . -t "ecal"
docker run -p5000:5000 --name ecal ecal
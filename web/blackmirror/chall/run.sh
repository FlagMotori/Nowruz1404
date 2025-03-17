#!/bin/bash

docker compose kill
docker compose rm
docker compose build
docker compose up

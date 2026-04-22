#! /usr/bin/bash

sudo docker run -d \
    --name goals-postgres \
    -p 5007:5432 \
    -e POSTGRES_PASSWORD=1234 \
    -e POSTGRES_USER=didorgas \
    -e POSTGRES_DB=goals_db \
    postgres:latest

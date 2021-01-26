#!/usr/bin/env bash
docker run --name poke-query --rm -d -v "$PWD:/home/flask/src" -p "5000:5000" poke-query:development

#!/bin/bash
app="docker.test"
dir=pwd -W
docker build -t ${app} .
docker run -d -p 56733:80 --name=${app}  -v ${dir}:/app ${app}

# docker run -dit --restart unless-stopped \ v ~/Documents/flask/app:/app \ --name app-flesk-app  app-flesk
  
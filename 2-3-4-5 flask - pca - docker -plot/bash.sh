#!/bin/bash
app="sample-test"
docker build -t sample-test .
docker run -d -p 56733:80 --name=flask-1  -v $PWD:/app sample-test


# docker run -dit --restart unless-stopped \ v ~/Documents/flask/app:/app \ --name app-flesk-app  app-flesk
  
#!/bin/bash
# app="docker.test"
# docker build -t ${app} .
# docker run -d -p 56733:80 --name=${app}  -v $PWD:/app ${app}


# docker run -dit --restart unless-stopped \ v ~/Documents/flask/app:/app \ --name app-flesk-app  app-flesk
#   docker run -d -p 56733:80 --name=sample-1-c  -v $PWD:/app sample-1
#  
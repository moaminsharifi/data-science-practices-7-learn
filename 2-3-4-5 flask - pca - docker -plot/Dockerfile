#FROM tiangolo/uwsgi-nginx-flask:python3.7-alpine3.7

#LABEL maintainer="amin sharifi <bigm00bnd@gmail.com>"
FROM tiangolo/uwsgi-nginx-flask


WORKDIR /app
COPY . /app

RUN pip3 install --no-cache-dir -U pip
RUN pip3 install -r req.txt

#RUN apk --update add bash nano
#RUN apk add --no-cache python3-dev libstdc++ && \
    # apk add --no-cache g++ && \
    # ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    # pip3 install numpy && \
    # pip3 install pandas && \
    # pip install --upgrade pip

#ENV STATIC_URL /static
#ENV STATIC_PATH /var/www/app/static
#WORKDIR /app
#COPY . /app

#COPY ./req.txt /var/www/app/req.txt
#RUN pip install -r  /var/www/app/req.txt

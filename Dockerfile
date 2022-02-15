FROM alpine:3.14.3
WORKDIR /app
RUN apk update && apk upgrade
RUN apk add python3 py3-pip
COPY ./openportals.db .
COPY ./__main__.py .
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT ./__main__.py

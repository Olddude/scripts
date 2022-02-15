FROM alpine:3.14.3
RUN apk update && apk upgrade
RUN apk add python3 py3-pip
RUN echo $(python3 --version)
RUN echo $(pip --version)


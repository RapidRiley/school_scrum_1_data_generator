FROM python:alpine3.15

ARG DATA_DIR
ENV DATA_DIR=${DATA_DIR}

COPY ./src/*.py /app/

RUN mkdir /scripts
COPY ./scripts/run.sh /scripts/run.sh

RUN mkdir ${DATA_DIR}

WORKDIR /
CMD /bin/sh /scripts/run.sh
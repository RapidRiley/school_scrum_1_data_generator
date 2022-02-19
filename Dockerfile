FROM alpine

RUN apk add python3

ARG DATA_DIR
ENV DATA_DIR=${DATA_DIR}

COPY ./generate.py /app/

RUN mkdir ${DATA_DIR}

CMD python3 /app/generate.py & /bin/sh
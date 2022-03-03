FROM python:alpine3.15

ARG DATA_DIR
ENV DATA_DIR=${DATA_DIR}

COPY ./src/*.py /app/
COPY ./scripts/run.sh /scripts/

RUN mkdir ${DATA_DIR}

CMD /scripts/run.sh
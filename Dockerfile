FROM python:3.8

ARG PUID=1000
ARG PGID=1000
ARG ENVIRONMENT=development

ENV PUID ${PUID}
ENV PGID ${PGID}

RUN groupadd -g ${PGID} flask \
    && useradd -u ${PUID} -g flask -m flask -s /bin/bash

USER flask

WORKDIR /home/flask/src

ADD requirements requirements

RUN pip install --user --no-warn-script-location -r requirements/${ENVIRONMENT}.txt

CMD python -m flask run -h 0.0.0.0

EXPOSE 5000

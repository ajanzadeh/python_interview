FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN chmod +X ./bootstrap.sh

ENTRYPOINT ["/bin/bash", "/usr/src/app/bootstrap.sh"]

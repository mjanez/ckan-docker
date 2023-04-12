FROM python:3.11-slim-bullseye
LABEL maintainer="mnl.janez@gmail.com"

ENV APP_DIR=/app
ENV TZ=UTC
RUN echo ${TZ} > /etc/timezone
ENV PYCSW_CKAN_SCHEMA=iso19139_inspire
ENV PYCSW_CONFIG=${APP_DIR}/pycsw.conf
ENV CKAN_URL=http://localhost:5000/
ENV PYCSW_PORT=8000
ENV PYCSW_URL=http://localhost:${PYCSW_PORT}/
ENV DEV_MODE: False
ENV TIMEOUT=300

RUN apt-get -q -y update && \
    apt-get install -y wget && \
    DEBIAN_FRONTEND=noninteractive apt-get -yq install gettext-base
ADD https://raw.githubusercontent.com/eficode/wait-for/v2.2.3/wait-for /wait-for
RUN chmod +x /wait-for && \
    python3 -m pip install pdm

WORKDIR ${APP_DIR}
COPY pyproject.toml pdm.lock .

RUN pdm install --no-self --group prod

COPY pycsw/conf/pycsw.conf.template pycsw/entrypoint.sh .
COPY ckan2pycsw ckan2pycsw

EXPOSE 8080/TCP
ENTRYPOINT ["/bin/bash", "./entrypoint.sh"]
CMD ["pdm", "run", "python3", "-m", "gunicorn", "pycsw.wsgi:application", "-b", "0.0.0.0:${PYCSW_PORT}"]
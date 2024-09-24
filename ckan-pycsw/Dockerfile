# Base image
FROM ghcr.io/mjanez/ckan-pycsw:main AS base
LABEL maintainer="mnl.janez@gmail.com"

# ckan-pycsw envvars
ENV APP_DIR=/app
ENV TZ=UTC
ENV PYCSW_CKAN_SCHEMA=iso19139_inspire
ENV PYCSW_CONFIG=${APP_DIR}/pycsw.conf
ENV CKAN_URL=http://localhost:5000/
ENV PYCSW_PORT=8000
ENV PYCSW_URL=http://localhost:${PYCSW_PORT}/
ENV DEV_MODE=False
ENV TIMEOUT=300
ENV PYCSW_CRON_DAYS_INTERVAL=2
ENV PYCSW_CRON_HOUR_START=4
ENV SSL_UNVERIFIED_MODE=False

WORKDIR ${APP_DIR}

# Update files if needed
COPY pycsw/conf/pycsw.conf.template docker-entrypoint.d/entrypoint.sh ./

ENTRYPOINT ["/bin/bash", "./entrypoint.sh"]
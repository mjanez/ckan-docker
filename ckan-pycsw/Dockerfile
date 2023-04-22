FROM ghcr.io/mjanez/ckan-pycsw:latest

# Set up environment variables
ENV APP_DIR=/app
ENV TZ=UTC
RUN echo ${TZ} > /etc/timezone
ENV PYCSW_CKAN_SCHEMA=iso19139_inspire
ENV PYCSW_CONFIG=${APP_DIR}/pycsw.conf
ENV CKAN_URL=http://localhost:5000/
ENV PYCSW_PORT=8000
ENV PYCSW_URL=http://localhost:${PYCSW_PORT}/
ENV DEV_MODE=False
ENV TIMEOUT=300
ENV PYCSW_CRON_DAYS_INTERVAL=2
ENV PYCSW_CRON_HOUR_START=4
WORKDIR ${APP_DIR}

COPY pycsw/conf/pycsw.conf.template pycsw/entrypoint.sh .

EXPOSE ${PYCSW_PORT}/TCP

ENTRYPOINT ["/bin/bash", "./entrypoint.sh"]
CMD ["tail", "-f", "/dev/null"]
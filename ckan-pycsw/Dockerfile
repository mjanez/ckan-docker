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

# PYCSW Catalog configuration
ENV CSW_IDENTIFICATION_TITLE="Sample Geospatial Catalogue" \
    CSW_IDENTIFICATION_ABSTRACT="OGC CSW server powered by pycsw" \
    CSW_PROVIDER_NAME="ckan-docker development team" \
    CSW_PROVIDER_URL="https://github.com/mjanez/ckan-docker" \
    CSW_CONTACT_NAME="ckan-docker development team" \
    CSW_CONTACT_POSITION="Site Administrator" \
    CSW_CONTACT_ADDRESS="ckan-docker development team" \
    CSW_CONTACT_CITY="Madrid" \
    CSW_CONTACT_STATE_OR_PROVINCE="Madrid" \
    CSW_CONTACT_POSTAL_CODE="28001" \
    CSW_CONTACT_COUNTRY="Spain" \
    CSW_CONTACT_EMAIL=${CKAN_SYSADMIN_EMAIL} \
    CSW_CONTACT_URL=${CKAN_URL} \
    CSW_INSPIRE_DATE="2024-01-01" \
    CSW_INSPIRE_GEMET_KEYWORDS="Utility and governmental services" \
    CSW_INSPIRE_CONFORMITY="notEvaluated" \
    CSW_INSPIRE_CONTACT_NAME=${CSW_CONTACT_NAME} \
    CSW_INSPIRE_CONTACT_EMAIL=${CKAN_SYSADMIN_EMAIL} \
    CSW_INSPIRE_TEMP_EXTENT="2024-01-01/2024-12-31"

WORKDIR ${APP_DIR}

# Update files if needed
COPY pycsw/conf/pycsw.conf.template docker-entrypoint.d/entrypoint.sh ./

ENTRYPOINT ["/bin/bash", "./entrypoint.sh"]
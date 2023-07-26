#!/bin/bash

# Update who.ini when exists PROXY_CKAN_LOCATION
echo "Update who.ini"
if [ -n "$PROXY_CKAN_LOCATION" ] && [ "$PROXY_CKAN_LOCATION" != "/" ]; then \
        sed -i "s|\${WHO_LOCATION}|$PROXY_CKAN_LOCATION|g" ${APP_DIR}/who.ini; \
    else \
        sed -i "s|\${WHO_LOCATION}|/|g" ${APP_DIR}/who.ini; \
    fi
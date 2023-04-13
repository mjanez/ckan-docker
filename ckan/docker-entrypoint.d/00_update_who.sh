#!/bin/bash

# Update who.ini when exists APACHE_CKAN_LOCATION
echo "Update who.ini"
if [ -n "$APACHE_CKAN_LOCATION" ] && [ "$APACHE_CKAN_LOCATION" != "/" ]; then \
        sed -i "s|\${WHO_LOCATION}|$APACHE_CKAN_LOCATION|g" ${APP_DIR}/who.ini; \
    else \
        sed -i "s|\${WHO_LOCATION}|/|g" ${APP_DIR}/who.ini; \
    fi
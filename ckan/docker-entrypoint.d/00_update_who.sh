#!/bin/bash

# Update who.ini when exists PROXY_CKAN_LOCATION
echo "[docker-entrypoint.00_update_who] Update who.ini"
if [ -n "$PROXY_CKAN_LOCATION" ] && [ "$PROXY_CKAN_LOCATION" != "/" ]; then
    sed -i "s|\${WHO_LOCATION}|$PROXY_CKAN_LOCATION|g" "${APP_DIR}/who.ini";
else
    # Check if the value is exactly "/"
    if [ "$PROXY_CKAN_LOCATION" = "/" ]; then
        sed -i "s|\${WHO_LOCATION}||g" "${APP_DIR}/who.ini";
    else
        # Handle the case when $PROXY_CKAN_LOCATION is empty or not set
        sed -i "s|\${WHO_LOCATION}|/|g" "${APP_DIR}/who.ini";
    fi
fi

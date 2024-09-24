#!/bin/bash

set -xeuo pipefail

envsubst < pycsw.conf.template > pycsw.conf

# TODO: -Xfrozen_modules=off from: https://bugs.python.org/issue1666807

# Check if SSL_UNVERIFIED_MODE is enabled
if [ "${SSL_UNVERIFIED_MODE:-false}" = "true" ] || [ "${SSL_UNVERIFIED_MODE:-false}" = "True" ]; then
    export REQUESTS_CA_BUNDLE=""
    export CURL_CA_BUNDLE=""
    SSL_FLAGS="--insecure"  # Add SSL ignore flag
    echo "[INSECURE] SSL_UNVERIFIED_MODE is enabled. SSL certificate verification is disabled."
else
    SSL_FLAGS=""
fi

# Use curl directly instead of wait-for if necessary
echo 'Waiting for $CKAN_URL to become available...'
until curl $SSL_FLAGS --output /dev/null --silent --head --fail "$CKAN_URL"; do
    printf '.'
    sleep 30
done
echo 'CKAN is available.'

# Ejecutar el comando Python
pdm run python3 -Xfrozen_modules=off ckan2pycsw/ckan2pycsw.py

exec "$@"

#!/bin/bash

set -xeuo pipefail

envsubst < pycsw.conf.template > pycsw.conf
/wait-for --timeout "$TIMEOUT" "$CKAN_URL" -- pdm run python3 ckan2pycsw/ckan2pycsw.py

exec "$@"

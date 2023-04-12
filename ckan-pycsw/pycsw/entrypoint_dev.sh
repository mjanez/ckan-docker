#!/bin/bash

set -xeuo pipefail

envsubst < pycsw.conf.template > pycsw.conf
/wait-for --timeout "$TIMEOUT" "$CKAN_URL" -- pdm run python3 -m ptvsd --host 0.0.0.0 --port 5678 --wait ckan2pycsw/ckan2pycsw.py

exec "$@"

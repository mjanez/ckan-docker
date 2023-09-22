#!/bin/bash

set -xeuo pipefail

envsubst < pycsw.conf.template > pycsw.conf

#TODO: -Xfrozen_modules=off from: https://bugs.python.org/issue1666807
/wait-for --timeout "$TIMEOUT" "$CKAN_URL" -- pdm run python3 -Xfrozen_modules=off ckan2pycsw/ckan2pycsw.py

exec "$@"

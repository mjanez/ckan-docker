#!/bin/bash

set -xeuo pipefail

# Change ownership of log and metadata directories
chown -R $USERNAME:$USERNAME ${APP_DIR}/log
chown -R $USERNAME:$USERNAME ${APP_DIR}/metadata

# Switch to the non-root user
su - $USERNAME

envsubst < pycsw.conf.template > pycsw.conf

#TODO: -Xfrozen_modules=off from: https://bugs.python.org/issue1666807
/wait-for --timeout "$TIMEOUT" "$CKAN_URL" -- pdm run python3 -Xfrozen_modules=off ckan2pycsw/ckan2pycsw.py

exec "$@"

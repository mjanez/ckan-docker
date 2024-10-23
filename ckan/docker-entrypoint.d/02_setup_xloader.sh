#!/bin/bash

# Set the name of the token to revoke
TOKEN_NAME="xloader"

# Get the list of tokens and extract the IDs for tokens with the specified name
TOKEN_IDS=$(ckan -c $CKAN_INI user token list $CKAN_SYSADMIN_NAME | grep "$TOKEN_NAME" | awk -F'[][]' '{print $2}' | tr -d '[]')

# Revoke each previous token of xloader
for TOKEN_ID in $TOKEN_IDS
do
  if [ -z "$TOKEN_ID" ]; then
    echo "[docker-entrypoint.01_setup_xloader] No API Token to revoke"
    continue
  fi
  ckan -c $CKAN_INI user token revoke -- $TOKEN_ID
  if [ $? -eq 0 ]; then
    echo "[docker-entrypoint.01_setup_xloader] API Token $TOKEN_ID has been revoked"
  fi
done

# Add ckanext.xloader.api_token to the CKAN config file
echo "[docker-entrypoint.01_setup_xloader] Loading ckanext-xloader settings in the CKAN config file"
ckan config-tool $CKAN_INI \
    "ckanext.xloader.api_token=xxx"

# Create ckanext-xloader API_TOKEN
echo "[docker-entrypoint.01_setup_xloader] Set up ckanext.xloader.api_token in the CKAN config file"
ckan config-tool $CKAN_INI "ckanext.xloader.api_token=$(ckan -c $CKAN_INI user token add $CKAN_SYSADMIN_NAME xloader | tail -n 1 | tr -d '\t')"
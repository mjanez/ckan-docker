#!/bin/bash

# ckanext-scheming/ckanext-schemingdcat: Update settings defined in the envvars (https://github.com/ckan/ckanext-pages#configuration)
echo "[docker-entrypoint.01_setup_ckanext_config] Clear index"
ckan -c $CKAN_INI search-index clear

# ckan: Update core settings
echo "[docker-entrypoint.01_setup_ckanext_config] Loading CKAN core settings in the CKAN config file"
ckan config-tool $CKAN_INI \
    "ckan.display_timezone=$TZ"

# Rebuild index
echo "[docker-entrypoint.01_setup_ckanext_config] Rebuild index"
ckan -c $CKAN_INI search-index rebuild
#!/bin/bash

# Add pages CKAN config file (https://github.com/ckan/ckanext-pages#configuration)
echo "Loading pages config in the CKAN config file"
ckan config-tool $CKAN_INI \
     "ckan.pages.allow_html = $CKANEXT__PAGES__ALOW_HTML" \
     "ckanext.pages.organization = $CKANEXT__PAGES__ORGANIZATION" \
     "ckanext.pages.group = $CKANEXT__PAGES__GROUP" \

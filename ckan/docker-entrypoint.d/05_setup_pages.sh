#!/bin/bash

# Add pages CKAN config file (https://github.com/ckan/ckanext-pages#configuration)
echo "Loading pages config in the CKAN config file"
ckan config-tool $CKAN_INI \
     "ckan.pages.allow_html = $CKANEXT__PAGES__ALOW_HTML" \
     "ckanext.pages.organization = $CKANEXT__PAGES__ORGANIZATION" \
     "ckanext.pages.group = $CKANEXT__PAGES__GROUP" \
     "ckanext.pages.about_menu = $CKANEXT__PAGES__ABOUT_MENU" \
     "ckanext.pages.group_menu = $CKANEXT__PAGES__GROUP_MENU" \
     "ckanext.pages.organization_menu = $CKANEXT__PAGES__ORGANIZATION_MENU"

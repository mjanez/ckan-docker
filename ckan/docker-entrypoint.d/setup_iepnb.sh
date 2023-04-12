#!/bin/bash

# Update ckanext-iepnb settings
echo "Set up ckanext-iepnb"

#TODO: Version with solr
#ckan -c $CKAN_INI search-index clear

ckan config-tool $CKAN_INI \
    "iepnb.server=$CKANEXT__IEPNB_SERVER" \
    "iepnb.path_menu =$CKANEXT__IEPNB_PATH_MENU" \
    "iepnb.breadcrumbs=$CKANEXT__IEPNB_BREADCRUMBS" \
    "iepnb.popular_tags=$CKANEXT__IEPNB_POPULAR_TAGS" \
    "iepnb.facet_list=$CKANEXT__IEPNB_FACET_LIST"

#TODO: Version with solr
#ckan -c $CKAN_INI search-index rebuild
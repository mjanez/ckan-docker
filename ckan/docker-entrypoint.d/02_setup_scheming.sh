#!/bin/bash

# Update ckanext-scheming and ckanext-facet_scheming settings defined in the env var
echo "Set up ckanext-facet_scheming. Clear index"
ckan -c $CKAN_INI search-index clear

echo "Loading ckanext-scheming and ckanext-facet_scheming settings into ckan.ini"
ckan config-tool $CKAN_INI \
    "scheming.dataset_schemas=$SCHEMA_CKANEXT_SCHEMING_DATASET_SCHEMA" \
    "scheming.group_schemas=$SCHEMA_CKANEXT_SCHEMING_GROUP_SCHEMAS" \
    "scheming.organization_schemas=$SCHEMA_CKANEXT_SCHEMING_ORGANIZATION_SCHEMAS" \
    "scheming.presets=$SCHEMA_CKANEXT_SCHEMING_PRESETS" \
    "facet_scheming.facet_list=$CKANEXT__FACET_FACET_LIST"

echo "ckanext-facet_scheming. Rebuild index"
ckan -c $CKAN_INI search-index rebuild
#!/bin/bash

# Update ckanext-scheming and ckanext-schemingdcat settings defined in the env var
echo "[docker-entrypoint.02_setup_scheming] Clear index"
ckan -c $CKAN_INI search-index clear

echo "[docker-entrypoint.02_setup_scheming] Loading ckanext-scheming and ckanext-schemingdcat settings into ckan.ini"
ckan config-tool $CKAN_INI \
    "scheming.dataset_schemas=$CKANEXT__SCHEMINGDCAT_DATASET_SCHEMA" \
    "scheming.group_schemas=$CKANEXT__SCHEMINGDCAT_GROUP_SCHEMAS" \
    "scheming.organization_schemas=$CKANEXT__SCHEMINGDCAT_ORGANIZATION_SCHEMAS" \
    "scheming.presets=$CKANEXT__SCHEMINGDCAT_PRESETS" \
    "schemingdcat.facet_list=$CKANEXT__SCHEMINGDCAT_FACET_LIST" \
    "schemingdcat.organization_custom_facets=$CKANEXT__SCHEMINGDCAT_ORGANIZATION_CUSTOM_FACETS" \
    "schemingdcat.group_custom_facets=$CKANEXT__SCHEMINGDCAT_GROUP_CUSTOM_FACETS" \
    "schemingdcat.geometadata_base_uri=$CKANEXT__SCHEMINGDCAT_GEOMETADATA_BASE_URI"

echo "[docker-entrypoint.02_setup_scheming] Rebuild index"
ckan -c $CKAN_INI search-index rebuild
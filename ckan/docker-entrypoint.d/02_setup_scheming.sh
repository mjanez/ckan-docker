#!/bin/bash

# Update ckanext-scheming and ckanext-scheming_dcat settings defined in the env var
echo "[docker-entrypoint.02_setup_scheming] Clear index"
ckan -c $CKAN_INI search-index clear

echo "[docker-entrypoint.02_setup_scheming] Loading ckanext-scheming and ckanext-scheming_dcat settings into ckan.ini"
ckan config-tool $CKAN_INI \
    "scheming.dataset_schemas=$CKANEXT__SCHEMING_DCAT_DATASET_SCHEMA" \
    "scheming.group_schemas=$CKANEXT__SCHEMING_DCAT_GROUP_SCHEMAS" \
    "scheming.organization_schemas=$CKANEXT__SCHEMING_DCAT_ORGANIZATION_SCHEMAS" \
    "scheming.presets=$CKANEXT__SCHEMING_DCAT_PRESETS" \
    "scheming_dcat.facet_list=$CKANEXT__SCHEMING_DCAT_FACET_LIST" \
    "scheming_dcat.organization_custom_facets=$CKANEXT__SCHEMING_DCAT_ORGANIZATION_CUSTOM_FACETS" \
    "scheming_dcat.group_custom_facets=$CKANEXT__SCHEMING_DCAT_GROUP_CUSTOM_FACETS" \
    "scheming_dcat.geometadata_base_uri=$CKANEXT__SCHEMING_DCAT_GEOMETADATA_BASE_URI"

echo "[docker-entrypoint.02_setup_scheming] Rebuild index"
ckan -c $CKAN_INI search-index rebuild
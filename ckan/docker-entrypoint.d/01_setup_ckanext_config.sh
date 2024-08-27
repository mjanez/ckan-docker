#!/bin/bash

# ckanext-scheming/ckanext-schemingdcat: Update settings defined in the envvars (https://github.com/ckan/ckanext-pages#configuration)
echo "[docker-entrypoint.01_setup_ckanext_config] Clear index"
ckan -c $CKAN_INI search-index clear

echo "[docker-entrypoint.01_setup_ckanext_config] Loading ckanext-scheming and ckanext-schemingdcat settings into ckan.ini"
ckan config-tool $CKAN_INI \
    "scheming.dataset_schemas=$CKANEXT__SCHEMINGDCAT_DATASET_SCHEMA" \
    "scheming.group_schemas=$CKANEXT__SCHEMINGDCAT_GROUP_SCHEMAS" \
    "scheming.organization_schemas=$CKANEXT__SCHEMINGDCAT_ORGANIZATION_SCHEMAS" \
    "scheming.presets=$CKANEXT__SCHEMINGDCAT_PRESETS" \
    "schemingdcat.facet_list=$CKANEXT__SCHEMINGDCAT_FACET_LIST" \
    "schemingdcat.organization_custom_facets=$CKANEXT__SCHEMINGDCAT_ORGANIZATION_CUSTOM_FACETS" \
    "schemingdcat.group_custom_facets=$CKANEXT__SCHEMINGDCAT_GROUP_CUSTOM_FACETS" \
    "schemingdcat.geometadata_base_uri=$CKANEXT__SCHEMINGDCAT_GEOMETADATA_BASE_URI" \
    "schemingdcat.default_package_item_icon=$CKANEXT__SCHEMINGDCAT_DEFAULT_PACKAGE_ITEM_ICON" \
    "schemingdcat.default_package_item_show_spatial=$CKANEXT__SCHEMINGDCAT_DEFAULT_PACKAGE_ITEM_SHOW_SPATIAL" \
    "schemingdcat.show_metadata_templates_toolbar=$CKANEXT__SCHEMINGDCAT_SHOW_METADATA_TEMPLATES_TOOLBAR" \
    "schemingdcat.metadata_templates_search_identifier=$CKANEXT__METADATA_TEMPLATES_SEARCH_IDENTIFIER" \
    "schemingdcat.endpoints_yaml=$CKANEXT__SCHEMINGDCAT_ENDPOINTS_YAML" \

# ckanext-dcat: Add settings to the CKAN config file
echo "[docker-entrypoint.01_setup_ckanext_config] Loading ckanext-dcat settings in the CKAN config file"
ckan config-tool $CKAN_INI \
    "ckanext.dcat.base_uri = $CKANEXT__DCAT__BASE_URI" \
    "ckanext.dcat.catalog_endpoint = $CKANEXT__DCAT__DEFAULT_CATALOG_ENDPOINT" \
    "ckanext.dcat.rdf.profiles = $CKANEXT__DCAT__RDF_PROFILES"

# ckan previews: Add CKAN Resource views to the CKAN config file
echo "[docker-entrypoint.01_setup_ckanext_config] Loading resource views in the CKAN config file"
ckan config-tool $CKAN_INI \
    "ckan.views.default_views = $CKAN__VIEWS__DEFAULT_VIEWS" \
    "ckan.preview.json_formats = $CKAN__PREVIEW__JSON_FORMATS" \
    "ckan.preview.xml_formats = $CKAN__PREVIEW__XML_FORMATS" \
    "ckan.preview.text_formats = $CKAN__PREVIEW__TEXT_FORMATS" \
    "ckan.preview.loadable = $CKAN__PREVIEW__LOADABLE"

# ckanext-geoview: Add geoviews CKAN config file
echo "[docker-entrypoint.01_setup_ckanext_config] Loading geoviews in the CKAN config file"
ckan config-tool $CKAN_INI \
    "ckanext.geoview.ol_viewer.formats = $CKANEXT__GEOVIEW__OL_VIEWER__FORMATS" \
    "ckanext.geoview.shp_viewer.srid = $CKANEXT__GEOVIEW__SHP_VIEWER__SRID" \
    "ckanext.geoview.shp_viewer.encoding = $CKANEXT__GEOVIEW__SHP_VIEWER__ENCODING" \
    "ckanext.geoview.geojson.max_file_size = $CKANEXT__GEOVIEW__GEOJSON__MAX_FILE_SIZE"

# ckanext-pages: Add pages CKAN config file
echo "[docker-entrypoint.01_setup_ckanext_config] Loading pages config in the CKAN config file"
ckan config-tool $CKAN_INI \
     "ckan.pages.allow_html = $CKANEXT__PAGES__ALOW_HTML" \
     "ckanext.pages.organization = $CKANEXT__PAGES__ORGANIZATION" \
     "ckanext.pages.group = $CKANEXT__PAGES__GROUP" \
     "ckanext.pages.about_menu = $CKANEXT__PAGES__ABOUT_MENU" \
     "ckanext.pages.group_menu = $CKANEXT__PAGES__GROUP_MENU" \
     "ckanext.pages.organization_menu = $CKANEXT__PAGES__ORGANIZATION_MENU"

# Rebuild index
echo "[docker-entrypoint.01_setup_ckanext_config] Rebuild index"
ckan -c $CKAN_INI search-index rebuild
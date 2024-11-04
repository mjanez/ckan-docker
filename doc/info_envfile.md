# Environment variables
## Overview
This file is a template for environment variables needed by the application. It's not used by the application directly, but serves as a guide for creating a `.env` file, which is used. Here's a breakdown of the variables:

### Base
Basic configurations such as the location of the application.

- `APP_DIR`: The directory where the application is located.

### Host Ports
Ports on which various services are running.

- `CKAN_PORT_HOST`: The port on which CKAN is running.
- `PYCSW_PORT_HOST`: The port on which PYCSW is running.
- `PROXY_SERVER_HTTP_PORT_HOST`: The HTTP port for the proxy server.
- `PROXY_SERVER_HTTPS_PORT_HOST`: The HTTPS port for the proxy server.
- `NGINX_PORT_HOST`: The port on which NGINX is running.
- `NGINX_SSLPORT_HOST`: The port on which NGINX is running with SSL.
- `APACHE_PORT_HOST`: The port on which Apache is running.

### Solr
Solr is a highly reliable, scalable, and fault-tolerant full-text search engine. CKAN uses it for indexing and searching data.

- `SOLR_IMAGE_VERSION`: The version of the Solr image.
- `SOLR_PORT`: The port on which Solr is running.
- `SOLR_CKAN_DATABASE`: The CKAN database for Solr.
- `CKAN_SOLR_URL`: The URL of the Solr instance used by CKAN.
- `TEST_CKAN_SOLR_URL`: The URL of the Solr instance used by CKAN for testing.

### Redis
Redis is an in-memory data structure store, used as a database, cache, and message broker. CKAN uses it for tasks such as session management and job queueing.

- `REDIS_VERSION`: The version of Redis.
- `REDIS_PORT`: The port on which Redis is running.
- `REDIS_CKAN_DATABASE`: The CKAN database for Redis.
- `CKAN_REDIS_URL`: The URL of the Redis instance used by CKAN.
- `TEST_CKAN_REDIS_URL`: The URL of the Redis instance used by CKAN for testing.

### NGINX
NGINX is a high-performance web server and reverse proxy. In the context of CKAN, it is used to serve static content and as a reverse proxy to improve performance and scalability. [**Default reverse proxy**]

- `NGINX_PORT`: The port on which NGINX is running.
- `NGINX_SSLPORT`: The port on which NGINX is running with SSL.
- `NGINX_LOG_DIR`: The directory where NGINX logs are stored.

### Apache HTTP Server
Apache is an open-source web server. It can be used by CKAN to serve its web application. [**Alternative reverse proxy/Development reserve proxy**]

- `APACHE_VERSION`: The version of Apache.
- `APACHE_PORT`: The port on which Apache is running.
- `APACHE_LOG_DIR`: The directory where Apache logs are stored.

### NGINX/APACHE
This section refers to the proxy server configuration, which can be either NGINX or Apache. The proxy server is used to route requests to the correct CKAN application.

- `PROXY_SERVER_NAME`: The server name for the proxy.
- `PROXY_SERVER_PROTOCOL`: The protocol for the proxy server.
- `PROXY_SERVER_URL`: The URL of the proxy server.
- `PROXY_CKAN_LOCATION`: The location of the CKAN proxy.
- `PROXY_PYCSW_LOCATION`: The location of the PYCSW proxy.

### pycsw
pycsw is a catalogue server for spatial metadata. CKAN uses it to expose spatial and geospatial metadata using web standards by using [`ckan-pycsw`](https://github.com/mjanez/ckan-pycsw).

- `PYCSW_PORT`: The port on which PYCSW is running.
- `CKAN_URL`: The URL of the CKAN instance.
- `PYCSW_URL`: The URL of the PYCSW instance.
- `PYCSW_CKAN_SCHEMA`: The schema used by PYCSW for CKAN.
- `PYCSW_OUPUT_SCHEMA`: The output schema used by PYCSW.
- `PYCSW_CRON_DAYS_INTERVAL`: The number of days between each scheduler job for PYCSW.
- `PYCSW_CRON_HOUR_START`: The hour of the day when the scheduler job for PYCSW starts.
- `TZ`: The timezone.

### CKAN databases
This section refers to the databases used by CKAN, which are typically PostgreSQL for the main# Environment variables
## Overview
This file is a template for environment variables needed by the application. It's not used by the application directly, but serves as a guide for creating a `.env` file, which is used. Here's a breakdown of the variables:

### Base
Basic configurations such as the location of the application.

- `APP_DIR`: The directory where the application is located.

### Host Ports
Ports on which various services are running.

- `CKAN_PORT_HOST`: The port on which CKAN is running.
- `PYCSW_PORT_HOST`: The port on which PYCSW is running.
- `PROXY_SERVER_HTTP_PORT_HOST`: The HTTP port for the proxy server.
- `PROXY_SERVER_HTTPS_PORT_HOST`: The HTTPS port for the proxy server.
- `NGINX_PORT_HOST`: The port on which NGINX is running.
- `NGINX_SSLPORT_HOST`: The port on which NGINX is running with SSL.
- `APACHE_PORT_HOST`: The port on which Apache is running.

### Solr
Solr is a highly reliable, scalable, and fault-tolerant full-text search engine. CKAN uses it for indexing and searching data.

- `SOLR_IMAGE_VERSION`: The version of the Solr image.
- `SOLR_PORT`: The port on which Solr is running.
- `SOLR_CKAN_DATABASE`: The CKAN database for Solr.
- `CKAN_SOLR_URL`: The URL of the Solr instance used by CKAN.
- `TEST_CKAN_SOLR_URL`: The URL of the Solr instance used by CKAN for testing.

### Redis
Redis is an in-memory data structure store, used as a database, cache, and message broker. CKAN uses it for tasks such as session management and job queueing.

- `REDIS_VERSION`: The version of Redis.
- `REDIS_PORT`: The port on which Redis is running.
- `REDIS_CKAN_DATABASE`: The CKAN database for Redis.
- `CKAN_REDIS_URL`: The URL of the Redis instance used by CKAN.
- `TEST_CKAN_REDIS_URL`: The URL of the Redis instance used by CKAN for testing.

### NGINX
NGINX is a high-performance web server and reverse proxy. In the context of CKAN, it is used to serve static content and as a reverse proxy to improve performance and scalability. [**Default reverse proxy**]

- `NGINX_PORT`: The port on which NGINX is running.
- `NGINX_SSLPORT`: The port on which NGINX is running with SSL.
- `NGINX_LOG_DIR`: The directory where NGINX logs are stored.

### Apache HTTP Server
Apache is an open-source web server. It can be used by CKAN to serve its web application. [**Alternative reverse proxy/Development reserve proxy**]

- `APACHE_VERSION`: The version of Apache.
- `APACHE_PORT`: The port on which Apache is running.
- `APACHE_LOG_DIR`: The directory where Apache logs are stored.

### NGINX/APACHE
This section refers to the proxy server configuration, which can be either NGINX or Apache. The proxy server is used to route requests to the correct CKAN application.

- `PROXY_SERVER_NAME`: The server name for the proxy.
- `PROXY_SERVER_PROTOCOL`: The protocol for the proxy server.
- `PROXY_SERVER_URL`: The URL of the proxy server.
- `PROXY_CKAN_LOCATION`: The location of the CKAN proxy.
- `PROXY_PYCSW_LOCATION`: The location of the PYCSW proxy.

### pycsw
pycsw is a catalogue server for spatial metadata. CKAN uses it to expose spatial and geospatial metadata using web standards by using [`ckan-pycsw`](https://github.com/mjanez/ckan-pycsw).

- `PYCSW_PORT`: The port on which PYCSW is running.
- `CKAN_URL`: The URL of the CKAN instance.
- `PYCSW_URL`: The URL of the PYCSW instance.
- `PYCSW_CKAN_SCHEMA`: The schema used by PYCSW for CKAN.
- `PYCSW_OUPUT_SCHEMA`: The output schema used by PYCSW.
- `PYCSW_CRON_DAYS_INTERVAL`: The number of days between each scheduler job for PYCSW.
- `PYCSW_CRON_HOUR_START`: The hour of the day when the scheduler job for PYCSW starts.
- `TZ`: The timezone.

### CKAN databases
This section refers to the databases used by CKAN, which are typically PostgreSQL for the main database and DataStore.

- `POSTGRES_USER`: The username for the Postgres database.
- `POSTGRES_PASSWORD` The password for the Postgres database.
- `POSTGRES_DB`: The name of the Postgres database.
- [`POSTGRES_HOST`: The host of the Postgres database.
- `CKAN_DB_USER`: The username for the CKAN database.
- `CKAN_DB_PASSWORD`: The password for the CKAN database.
- `CKAN_DB`: The name of the CKAN database.
- `DATASTORE_READONLY_USER`: The username for the read-only Datastore database.
- `DATASTORE_READONLY_PASSWORD`: The password for the read-only Datastore database.
- `DATASTORE_DB`: The name of the Datastore database.
- `CKAN_SQLALCHEMY_URL`: The SQLAlchemy URL for the CKAN database.
- `CKAN_DATASTORE_WRITE_URL`: The SQLAlchemy URL for writing to the Datastore database.
- `CKAN_DATASTORE_READ_URL`: The SQLAlchemy URL for reading from the Datastore database.

### Test database connections
This section refers to the test databases used by CKAN during integration and unit testing.

- `CKAN_TEST_DB`: The name of the CKAN test database.
- `DATASTORE_TEST_DB`: The name of the Datastore test database.
- `TEST_CKAN_SQLALCHEMY_URL`: The SQLAlchemy URL for the CKAN test database.
- `TEST_CKAN_DATASTORE_WRITE_URL`: The SQLAlchemy URL for writing to the Datastore test database.
- `TEST_CKAN_DATASTORE_READ_URL`: The SQLAlchemy URL for reading from the Datastore test database.

### Dev settings
This section contains configurations specific to the CKAN development environment.

- `USE_HTTPS_FOR_DEV`: Whether to use HTTPS for development.
- `CKAN_DEV_COMPOSE_SERVICE`: The Docker Compose service for CKAN development.

### CKAN core
This section contains configurations related to the core CKAN application. It includes variables for the CKAN version, site ID, site URL, root path, port, favicon, logo, and secrets for the Beaker session and JWT API tokens.

- `CKAN_VERSION`: The version of CKAN.
- `CKAN_SITE_ID`: The site ID for CKAN.
- `CKAN_SITE_URL`: The URL of the CKAN site.
- `CKAN__ROOT_PATH`: The root path for CKAN.
- `CKAN__FAVICON`: The path to the favicon for CKAN.
- `CKAN__SITE_LOGO`: The path to the logo for CKAN.
- `CKAN__SITE_TITLE`: The title of the CKAN site.
- `CKAN__SITE_DESCRIPTION`: The description of the CKAN site.
- `CKAN__SITE_INTRO_TEXT`: The intro text for the CKAN site.
- `CKAN__SITE_ABOUT`: The about text for the CKAN site.
- `LICENSES_GROUP_URL`: The URL for custom licenses.
- `CKAN___BEAKER__SESSION__SECRET`: The secret for the Beaker session.
- `CKAN___API_TOKEN__JWT__ENCODE__SECRET`: The secret for encoding JWT API tokens.
- `CKAN___API_TOKEN__JWT__DECODE__SECRET`: The secret for decoding JWT API tokens.
- `CKAN_SYSADMIN_NAME`: The username for the CKAN sysadmin.
- `CKAN_SYSADMIN_PASSWORD`: The password for the CKAN sysadmin.
- `CKAN_SYSADMIN_EMAIL`: The email for the CKAN sysadmin.
- `CKAN_STORAGE_PATH`: The path where CKAN data is stored.
- `CKAN_LOGS_PATH`: The path where CKAN logs are stored.
- `CKAN__SMTP_ENABLED`: Whether SMTP is enabled.
- `CKAN_SMTP_SERVER`: The SMTP server for CKAN.
- `CKAN_SMTP_STARTTLS`: Whether to use STARTTLS for the SMTP server.
- `CKAN_SMTP_USER`: The username for the SMTP server.
- `CKAN_SMTP_PASSWORD`: The password for the SMTP server.
- `CKAN_SMTP_MAIL_FROM`: The email address for outgoing mail from CKAN.
- `CKAN__PREVIEW__JSON_FORMATS`: The JSON formats that CKAN can preview.
- `CKAN__PREVIEW__XML_FORMATS`: The XML formats that CKAN can preview.
- `CKAN__PREVIEW__TEXT_FORMATS`: The text formats that CKAN can preview.
- `CKAN__PREVIEW__LOADABLE`: The formats that CKAN can load for preview.
- `CKAN__SEARCH__SOLR_ALLOWED_QUERY_PARSERS`: The query parsers allowed by Solr.
- `CKAN__CORS__ORIGIN_ALLOW_ALL`: Whether to allow all origins for CORS.
- `CKAN__CORS__ORIGIN_WHITELIST`: The whitelist of origins for CORS.
- `CKAN__AUTH__ALLOW_DATASET_COLLABORATORS`: Whether to allow dataset collaborators.
- `CKAN__AUTH__ALLOW_ADMIN_COLLABORATORS`: Whether to allow admin collaborators.
- `SEARCH__FACETS__DEFAULT`: The default number of facets shown in search results.
- `CKAN__DATASTORE__SQLSEARCH__ENABLED`: Whether the DataStore SQL search backend is enabled.

### Resource Proxy settings
This section refers to the configuration of CKAN's resource proxy, which is used to fetch and display resources from external sites.

- `CKAN__RESOURCE_PROXY__MAX_FILE_SIZE`: The maximum file size for the resource proxy.
- `CKAN__RESOURCE_PROXY__CHUNK_SIZE`: The chunk size for the resource proxy.
- `CKAN__RESOURCE_PROXY__TIMEOUT`: The timeout for the resource proxy.
- `CKAN__VIEWS__DEFAULT_VIEWS`: The default views for CKAN.

### Localization
This section refers to CKAN's localization settings, which determine the languages available in the user interface.

- `CKAN__LOCALE_DEFAULT`: The default locale for CKAN.
- `CKAN__LOCALE_ORDER`: The order of locales for CKAN.
- `CKAN__LOCALES_OFFERED`: The locales offered by CKAN.

### Extensions
This section refers to CKAN extensions, which are software modules that add additional functionality to the core CKAN application.

- `CKAN__PLUGINS`: The plugins for CKAN.

### ckanext-harvest
This is a CKAN extension that allows users to harvest dataset metadata from multiple sources.

- `CKAN__HARVEST__MQ__TYPE`: The type of message queue for the Harvest extension.
- `CKAN__HARVEST__MQ__HOSTNAME`: The hostname for the message queue for the Harvest extension.
- `CKAN__HARVEST__MQ__PORT`: The port for the message queue for the Harvest extension.
- `CKAN__HARVEST__MQ__REDIS_DB`: The Redis database for the message queue for the Harvest extension.
- `CKAN__HARVEST__LOG_TIMEFRAME`: The timeframe for the Harvest log.

### ckanext-xloader
This is a CKAN extension that allows users to load data into CKAN's data store for faster and more efficient processing.

- `CKANEXT__XLOADER__JOBS_DB__URI`: The database URI for the XLoader jobs.

### ckanext-dcat
This is a CKAN extension that provides support for the DCAT standard, allowing CKAN to expose and consume metadata in this format.

- `CKANEXT__DCAT__BASE_URI`: The base URI for the DCAT extension.
- `CKANEXT__DCAT__RDF_PROFILES`: The RDF profiles for the DCAT extension.
- `CKANEXT__DCAT__DEFAULT_CATALOG_ENDPOINT`: The default catalog endpoint for the DCAT extension.

### ckanext-spatial
This is a CKAN extension that provides spatial functionalities, such as geographic search and map user interface.

- `CKANEXT__SPATIAL__SEARCH_BACKEND`: The search backend for the Spatial extension.
- `CKAN__SPATIAL__SRID`: The SRID for the Spatial extension.
- `CKANEXT__SPATIAL__COMMON_MAP__TYPE`: The type of common map for the Spatial extension.
- `CKANEXT__SPATIAL__COMMON_MAP__CUSTOM__URL`: The URL of the custom common map for the Spatial extension.
- `CKANEXT__SPATIAL__COMMON_MAP__ATTRIBUTION`: The attribution for the common map for the Spatial extension.

### ckanext-geoview
This is a CKAN extension that allows users to visualize geospatial resources directly in the CKAN interface.

- `CKANEXT__GEOVIEW__GEOJSON__MAX_FILE_SIZE`: The maximum file size for GeoJSON in the GeoView extension.
- `CKANEXT__GEOVIEW__OL_VIEWER__FORMATS`: The formats for the OpenLayers viewer in the GeoView extension.
- `CKANEXT__GEOVIEW__SHP_VIEWER__SRID`: The SRID for the Shapefile viewer in the GeoView extension.
- `CKANEXT__GEOVIEW__SHP_VIEWER__ENCODING`: The encoding for the Shapefile viewer in the GeoView extension.

### ckanext-schemingdcat
This extension provides a way to configure and customize CKAN's dataset, resource, organization and group schemas.

- `CKANEXT__SCHEMINGDCAT_GEOMETADATA_BASE_URI`: This is the base URI for the CSW Endpoint for spatial metadata.
- `CKANEXT__SCHEMINGDCAT_DATASET_SCHEMA`: This is the path to the dataset schema file.
- `CKANEXT__SCHEMINGDCAT_GROUP_SCHEMAS`: This is the path to the group schema file.
- `CKANEXT__SCHEMINGDCAT_ORGANIZATION_SCHEMAS`: This is the path to the organization schema file.
- `CKANEXT__SCHEMINGDCAT_PRESETS`: This is the path to the presets file.
- `CKANEXT__SCHEMINGDCAT__FACET_LIST`: This is a list of facets for the dataset.
- `CKANEXT__SCHEMINGDCAT_ORGANIZATION_CUSTOM_FACETS`: This is a boolean value to enable or disable custom facets for organizations.
- `CKANEXT__SCHEMINGDCAT_GROUP_CUSTOM_FACETS`: This is a boolean value to enable or disable custom facets for groups.
- `CKANEXT__SCHEMINGDCAT_DEFAULT_PACKAGE_ITEM_ICON`: The default icon for package items.
- `CKANEXT__SCHEMINGDCAT_DEFAULT_PACKAGE_ITEM_SHOW_SPATIAL`: Whether to show spatial information for package items.
- `CKANEXT__SCHEMINGDCAT_SHOW_METADATA_TEMPLATES_TOOLBAR`: Whether to show the metadata templates toolbar.
- `CKANEXT__METADATA_TEMPLATES_SEARCH_IDENTIFIER`: The search identifier for metadata templates.
- `CKANEXT__SCHEMINGDCAT_ENDPOINTS_YAML`: The path to the endpoints YAML file.
- `CKANEXT__SCHEMINGDCAT__SOCIAL_GITHUB`: The GitHub URL for the schemingdcat extension.
- `CKANEXT__SCHEMINGDCAT__SOCIAL_X`: The X (formerly Twitter) URL for the schemingdcat extension.
- `CKANEXT__SCHEMINGDCAT__SOCIAL_LINKEDIN`: The LinkedIn URL for the schemingdcat extension.

### ckanext-pages
This extension provides a way to add simple internal pages.

- `CKANEXT__PAGES__ALOW_HTML`: This is a boolean value to enable or disable HTML in pages.
- `CKANEXT__PAGES__ORGANIZATION`: This is a boolean value to enable or disable organization pages.
- `CKANEXT__PAGES__GROUP`: This is a boolean value to enable or disable group pages.
- `CKANEXT__PAGES__ABOUT_MENU`: This is a boolean value to enable or disable the about menu.
- `CKANEXT__PAGES__GROUP_MENU`: This is a boolean value to enable or disable the group menu.
- `CKANEXT__PAGES__ORGANIZATION_MENU`: This is a boolean value to enable or disable the organization menu.

### ckan-pycsw
This extension provides a way to interact with a CSW endpoint.

- `CSW_IDENTIFICATION_TITLE`: The title for the CSW identification.
- `CSW_IDENTIFICATION_ABSTRACT`: The abstract for the CSW identification.
- `CSW_PROVIDER_NAME`: The name of the CSW provider.
- `CSW_PROVIDER_URL`: The URL of the CSW provider.
- `CSW_CONTACT_NAME`: The contact name for the CSW provider.
- `CSW_CONTACT_POSITION`: The contact position for the CSW provider.
- `CSW_CONTACT_ADDRESS`: The contact address for the CSW provider.
- `CSW_CONTACT_CITY`: The contact city for the CSW provider.
- `CSW_CONTACT_STATE_OR_PROVINCE`: The contact state or province for the CSW provider.
- `CSW_CONTACT_POSTAL_CODE`: The contact postal code for the CSW provider.
- `CSW_CONTACT_COUNTRY`: The contact country for the CSW provider.
- `CSW_CONTACT_EMAIL`: The contact email for the CSW provider.
- `CSW_CONTACT_URL`: The contact URL for the CSW provider.
- `CSW_INSPIRE_DATE`: The date of the last update of the metadata.
- `CSW_INSPIRE_GEMET_KEYWORDS`: The keywords for the CSW INSPIRE.
- `CSW_INSPIRE_CONFORMITY`: The level of INSPIRE conformance for spatial data sets and services.
- `CSW_INSPIRE_CONTACT_NAME`: The contact name for the CSW INSPIRE.
- `CSW_INSPIRE_CONTACT_EMAIL`: The contact email for the CSW INSPIRE.
- `CSW_INSPIRE_TEMP_EXTENT`: The temporal extent of the service.
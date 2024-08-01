FROM solr:9

ENV SOLR_PORT=8983

EXPOSE ${SOLR_PORT}

ARG CKAN_BRANCH="dev-v2.10"

ENV SOLR_INSTALL="/opt/solr"
ENV SOLR_CONFIG_DIR="$SOLR_INSTALL/server/solr/configsets"
ENV SOLR_SCHEMA_FILE="$SOLR_CONFIG_DIR/ckan/conf/managed-schema"
ENV SOLR_CKAN_DATABASE=ckan

USER root

# Create a CKAN configset by copying the default one
RUN cp -R $SOLR_CONFIG_DIR/_default $SOLR_CONFIG_DIR/$SOLR_CKAN_DATABASE

# Update the schema
ADD https://raw.githubusercontent.com/ckan/ckan/$CKAN_BRANCH/ckan/config/solr/schema.xml $SOLR_SCHEMA_FILE
RUN chmod 644 $SOLR_SCHEMA_FILE 

USER solr

CMD ["sh", "-c", "solr-precreate $SOLR_CKAN_DATABASE $SOLR_CONFIG_DIR/$SOLR_CKAN_DATABASE"]
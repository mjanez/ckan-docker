FROM ghcr.io/mjanez/ckan-spatial-base:2.10.5-py3.10
LABEL maintainer="mnl.janez@gmail.com"

# Set up environment variables
ENV APP_DIR=/srv/app
ENV TZ=UTC

# Set working directory
WORKDIR ${APP_DIR}

# requirements.txt files fixed until next releases
COPY req_fixes req_fixes

# CKAN configuration & extensions
## XLoader - 1.0.1 ##
## Harvest - v1.5.6 (Worker with supervisor) ##
## Geoview - v0.1.0 ##
## Spatial - v2.1.1 ##
## DCAT - v1.8.0 (Latest stable version of ckanext-dcat with minor fixes) ##
## Scheming - release-3.0.0 ##
## Resource dictionary - v1.0.1 (mjanez/Fixed version) ##
## Pages - v0.5.2 ##
## PDFView - 0.0.8 ##
## Fluent - v1.0.1  (mjanez/Forked stable version) ##
## Scheming DCAT - v3.2.2 (mjanez/GeoDCAT-AP/NTI-RISP extended version) ##
RUN echo ${TZ} > /etc/timezone && \
    if ! [ /usr/share/zoneinfo/${TZ} -ef /etc/localtime ]; then cp /usr/share/zoneinfo/${TZ} /etc/localtime; fi && \
    # Install patch utility
    apt-get update && \
    apt-get install -y patch && \
    # Install CKAN extensions
    echo "ckan/ckanext-xloader" && \
    pip3 install --no-cache-dir -e git+https://github.com/ckan/ckanext-xloader.git@1.0.1#egg=ckanext-xloader && \ 
    pip3 install --no-cache-dir -r ${APP_DIR}/src/ckanext-xloader/requirements.txt && \
    pip3 install --no-cache-dir -U requests[security] && \
    echo "ckan/ckanext-harvest" && \
    pip3 install --no-cache-dir -e git+https://github.com/ckan/ckanext-harvest.git@v1.5.6#egg=ckanext-harvest && \
    pip3 install --no-cache-dir -r ${APP_DIR}/src/ckanext-harvest/requirements.txt && \
    echo "ckan/ckanext-geoview" && \
    pip3 install --no-cache-dir -e git+https://github.com/ckan/ckanext-geoview.git@v0.1.0#egg=ckanext-geoview && \
    echo "ckan/ckanext-spatial" && \
    pip3 install --no-cache-dir -e git+https://github.com/ckan/ckanext-spatial.git@v2.1.1#egg=ckanext-spatial && \
    pip3 install --no-cache-dir -r ${APP_DIR}/req_fixes/ckanext-spatial/requirements.txt && \
    echo "mjanez/ckanext-dcat (GeoDCAT-AP extended version)" && \
    pip3 install --no-cache-dir -e git+https://github.com/mjanez/ckanext-dcat.git@v1.8.0#egg=ckanext-dcat && \
    pip3 install --no-cache-dir -r ${APP_DIR}/src/ckanext-dcat/requirements.txt && \
    echo "ckan/ckanext-scheming" && \
    pip3 install --no-cache-dir -e git+https://github.com/ckan/ckanext-scheming.git@release-3.0.0#egg=ckanext-scheming && \
    echo "mjanez/ckanext-resourcedictionary" && \
    pip3 install --no-cache-dir -e git+https://github.com/mjanez/ckanext-resourcedictionary.git@v1.0.1#egg=ckanext-resourcedictionary && \
    echo "ckan/ckanext-pages" && \
    pip3 install --no-cache-dir -e git+https://github.com/ckan/ckanext-pages.git@v0.5.2#egg=ckanext-pages && \
    echo "ckan/ckanext-pdfview" && \
    pip3 install --no-cache-dir -e git+https://github.com/ckan/ckanext-pdfview.git@0.0.8#egg=ckanext-pdfview && \
    echo "mjanez/ckanext-fluent" && \
    pip3 install --no-cache-dir -e git+https://github.com/mjanez/ckanext-fluent.git@v1.0.1#egg=ckanext-fluent && \
    echo "mjanez/ckanext-schemingdcat" && \
    pip3 install --no-cache-dir -e git+https://github.com/mjanez/ckanext-schemingdcat.git@v3.2.2#egg=ckanext_schemingdcat && \
    pip3 install --no-cache-dir -r ${APP_DIR}/src/ckanext-schemingdcat/requirements.txt && \
    # Remove system cache
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Used to configure the container environment by setting environment variables, creating users, running initialization scripts, .etc
COPY docker-entrypoint.d/* /docker-entrypoint.d/

# Update who.ini with PROXY_CKAN_LOCATION
COPY setup/who.ini ./

# Apply any patches needed to CKAN core
COPY patches patches

RUN for d in $APP_DIR/patches/*; do \
    if [ -d $d ]; then \
        for f in `ls $d/*.patch | sort -g`; do \
            cd $SRC_DIR/`basename "$d"` && \
            if patch -R --dry-run -p1 < "$f"; then \
                echo "$0: Patch $f has already been applied or reversed, skipping..."; \
            else \
                echo "$0: Applying patch $f to $SRC_DIR/`basename $d`"; \
                sed -i 's/\r$//' "$f" && \
                patch -p1 < "$f" ; \
            fi \
        done ; \
    fi ; \
done

# Workers
## Update start_ckan.sh with custom workers
COPY setup/start_ckan.sh.override ${APP_DIR}/start_ckan.sh
RUN chmod +x ${APP_DIR}/start_ckan.sh

## Load workers supervisor configuration
COPY setup/workers/* /etc/supervisord.d/

# Start CKAN
CMD ["/bin/sh", "-c", "$APP_DIR/start_ckan.sh"]

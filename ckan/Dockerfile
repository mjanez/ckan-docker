FROM ghcr.io/mjanez/ckan-base-spatial:ckan-2.9.9

# Set up environment variables
ENV APP_DIR=/srv/app \
    TZ=UTC

# requirements.txt files fixed until next releases
COPY req_fixes ${APP_DIR}/req_fixes

# Extensions
### XLoader - 1.0.1 ###
### Harvester - v1.5.1 ###
### Geoview - v0.0.20 ###
### Spatial - v2.0.0 ### fixed requirements.txt
### DCAT - 1.0.0-geodcatap (GeoDCAT-AP extended version) ###
### Scheming - release-3.0.0 ###
### Resource dictionary - 1.0.1 ###
### Pages - v0.5.2 ###
### PDFView - 0.0.8 ###
### Scheming DCAT - v1.1.0 (GeoDCAT-AP extended version) ###
### SPARQL Interface - 2.0.1 ###
RUN echo ${TZ} > /etc/timezone && \
    if ! [ /usr/share/zoneinfo/${TZ} -ef /etc/localtime ]; then cp /usr/share/zoneinfo/${TZ} /etc/localtime ; fi && \
    # Install CKAN extensions
    echo "ckan/ckanext-xloader" && \
    pip3 install -e 'git+https://github.com/ckan/ckanext-xloader.git@1.0.1#egg=ckanext-xloader' && \ 
    pip3 install -r ${APP_DIR}/src/ckanext-xloader/requirements.txt && \
    pip3 install -U requests[security] && \
    echo "ckan/ckanext-harvest" && \
    pip3 install -e 'git+https://github.com/ckan/ckanext-harvest.git@v1.5.1#egg=ckanext-harvest' && \
    pip3 install -r ${APP_DIR}/src/ckanext-harvest/pip-requirements.txt && \
    echo "ckan/ckanext-geoview" && \
    pip3 install -e 'git+https://github.com/ckan/ckanext-geoview.git@v0.0.20#egg=ckanext-geoview' && \
    echo "ckan/ckanext-spatial" && \
    pip3 install -e 'git+https://github.com/ckan/ckanext-spatial.git@v2.0.0#egg=ckanext-spatial' && \
    pip3 install -r ${APP_DIR}/req_fixes/ckanext-spatial_requirements.txt && \
    echo "mjanez/ckanext-dcat (GeoDCAT-AP extended version)" && \
    pip3 install -e git+https://github.com/mjanez/ckanext-dcat.git@1.0.0-geodcatap#egg=ckanext-dcat && \
    pip3 install -r https://raw.githubusercontent.com/mjanez/ckanext-dcat/master/requirements.txt && \
    echo "ckan/ckanext-scheming" && \
    pip3 install -e git+https://github.com/ckan/ckanext-scheming.git@release-3.0.0#egg=ckanext-scheming && \
    echo "mjanez/ckanext-resourcedictionary" && \
    pip3 install -e 'git+https://github.com/mjanez/ckanext-resourcedictionary.git@1.0.1#egg=ckanext-resourcedictionary' && \
    echo "ckan/ckanext-pages" && \
    pip3 install -e git+https://github.com/ckan/ckanext-pages.git@v0.5.2#egg=ckanext-pages && \
    echo "ckan/ckanext-pdfview" && \
    pip3 install -e git+https://github.com/ckan/ckanext-pdfview.git@0.0.8#egg=ckanext-pdfview && \
    echo "mjanez/ckanext-scheming_dcat" && \
    pip3 install -e git+https://github.com/mjanez/ckanext-scheming_dcat.git@v1.1.0#egg=ckanext_scheming_dcat && \
    pip3 install -r https://raw.githubusercontent.com/mjanez/ckanext-scheming_dcat/v1.1.0/requirements.txt

# Used to configure the container environment by setting environment variables, creating users, running initialization scripts, .etc
COPY docker-entrypoint.d/* /docker-entrypoint.d/

# Update who.ini with PROXY_CKAN_LOCATION
COPY setup/who.ini ${APP_DIR}/

# Apply any patches needed to CKAN core
COPY patches ${APP_DIR}/patches

RUN for d in $APP_DIR/patches/*; do \
    if [ -d $d ]; then \
    for f in `ls $d/*.patch | sort -g`; do \
    cd $SRC_DIR/`basename "$d"` && echo "$0: Applying patch $f to $SRC_DIR/`basename $d`"; patch -p1 < "$f" ; \
    done ; \
    fi ; \
    done

CMD $APP_DIR/start_ckan.sh

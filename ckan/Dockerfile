FROM ghcr.io/mjanez/ckan-base-spatial:ckan-2.9.8

# Set up environment variables
ENV APP_DIR=/srv/app
ENV TZ=UTC
RUN echo ${TZ} > /etc/timezone

# Make sure both files are not exactly the same
RUN if ! [ /usr/share/zoneinfo/${TZ} -ef /etc/localtime ]; then \
    cp /usr/share/zoneinfo/${TZ} /etc/localtime ;\
    fi ;

# Extensions
### XLoader - v0.12.2 ###
### Harvester - v1.5.1 ###
### Geoview - v0.0.20 ###
### Spatial - v2.0.0 ###
### DCAT - 1.0.0-geodcatap (GeoDCAT-AP extended version) ###
### Scheming - 1.0.0-geodcatap (GeoDCAT-AP extended version) ###
### Resource dictionary - 1.0.1 ###
### Pages - v0.5.1 ###
### PDFView - v0.0.8 ###
RUN echo "ckan/ckanext-xloader" && \
    pip3 install -e 'git+https://github.com/ckan/ckanext-xloader.git@0.12.2#egg=ckanext-xloader' && \ 
    pip3 install -r ${APP_DIR}/src/ckanext-xloader/requirements.txt && \
    pip3 install -U requests[security] && \
    echo "ckan/ckanext-harvest" && \
    pip3 install -e 'git+https://github.com/ckan/ckanext-harvest.git@v1.5.1#egg=ckanext-harvest' && \
    pip3 install -r ${APP_DIR}/src/ckanext-harvest/pip-requirements.txt && \
    echo "ckan/ckanext-geoview" && \
    pip3 install -e 'git+https://github.com/ckan/ckanext-geoview.git@v0.0.20#egg=ckanext-geoview' && \
    echo "ckan/ckanext-spatial" && \
    pip3 install -e 'git+https://github.com/ckan/ckanext-spatial.git@v2.0.0#egg=ckanext-spatial' && \
    pip3 install -r https://raw.githubusercontent.com/ckan/ckanext-spatial/bae9290395b252ee8e40056256fa694569d1d78b/requirements.txt && \
    echo "mjanez/ckanext-dcat (GeoDCAT-AP extended version)" && \
    pip3 install -e git+https://github.com/mjanez/ckanext-dcat.git@1.0.0-geodcatap#egg=ckanext-dcat && \
    pip3 install -r https://raw.githubusercontent.com/mjanez/ckanext-dcat/master/requirements.txt && \
    echo "mjanez/ckanext-scheming (GeoDCAT-AP extended version)" && \
    pip3 install -e git+https://github.com/mjanez/ckanext-scheming.git@1.0.0-geodcatap#egg=ckanext-scheming && \
    echo "mjanez/ckanext-resourcedictionary" && \
    pip3 install -e 'git+https://github.com/mjanez/ckanext-resourcedictionary.git@1.0.1#egg=ckanext-resourcedictionary' && \
    echo "ckan/ckanext-pages" && \
    pip3 install -e git+https://github.com/ckan/ckanext-pages.git@v0.5.1#egg=ckanext-pages && \
    echo "ckan/ckanext-pdfview" && \
    pip3 install -e git+https://github.com/ckan/ckanext-pdfview.git@0.0.8#egg=ckanext-pdfview

# Used to configure the container environment by setting environment variables, creating users, running initialization scripts, .etc
COPY docker-entrypoint.d/* /docker-entrypoint.d/

# Update who.ini with APACHE_CKAN_LOCATION
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

FROM nginx:1.27.2-alpine3.20

ARG PROXY_CKAN_LOCATION=/catalog
ARG PROXY_PYCSW_LOCATION=/csw

ENV CKAN_PORT=5000
ENV PYCSW_PORT=8000
ENV PYCSW_COMPOSE_SERVICE=pycsw
ENV CKAN_COMPOSE_SERVICE=ckan
ENV PROXY_SERVER_NAME=localhost
ENV PROXY_PYCSW_PROXY_PASS=http://${PYCSW_COMPOSE_SERVICE}:${PYCSW_PORT}
ENV PROXY_CKAN_PROXY_PASS=http://${CKAN_COMPOSE_SERVICE}:${CKAN_PORT}

ENV NGINX_PORT=80
ENV NGINX_LOG_DIR=/var/log/nginx
ENV NGINX_DIR=/etc/nginx
ENV NGINX_SHARE_HTML_DIR=/usr/share/nginx/html

RUN mkdir -p ${NGINX_LOG_DIR} \
    && mkdir -p ${NGINX_DIR}/certs

# Copy configuration and static files
COPY setup/nginx.conf ${NGINX_DIR}/nginx.conf
COPY setup/default.conf.template ${NGINX_DIR}/templates/default.conf.template
COPY setup/ckan-local.* ${NGINX_DIR}/certs/
COPY setup/html/index.html setup/html/robots.txt ${NGINX_SHARE_HTML_DIR}/

# Replace $PROXY_CKAN_LOCATION and $PROXY_PYCSW_LOCATION in index.html
RUN sed -i "s|<a href=\"/catalog\">|<a href=\"${PROXY_CKAN_LOCATION}\">|g; s|<a href=\"/csw\">|<a href=\"${PROXY_PYCSW_LOCATION}\">|g" ${NGINX_SHARE_HTML_DIR}/index.html

EXPOSE ${NGINX_PORT}
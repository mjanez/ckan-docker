FROM nginx:stable-alpine

ENV CKAN_PORT_HOST=5000
ENV PYCSW_PORT_HOST=8000
ENV PYCSW_CONTAINER_NAME=pycsw
ENV CKAN_CONTAINER_NAME=ckan
ENV PROXY_SERVER_NAME=localhost
ENV PROXY_CKAN_LOCATION=/catalog
ENV PROXY_PYCSW_LOCATION=/csw
ENV PROXY_PYCSW_PROXY_PASS=http://${PYCSW_CONTAINER_NAME}:${PYCSW_PORT_HOST}
ENV PROXY_CKAN_PROXY_PASS=http://${CKAN_CONTAINER_NAME}:${CKAN_PORT_HOST}

ENV NGINX_PORT=80
ENV NGINX_LOG_DIR=/var/log/nginx
ENV NGINX_DIR=/etc/nginx

RUN mkdir -p ${NGINX_LOG_DIR}

COPY setup/nginx.conf ${NGINX_DIR}/nginx.conf
COPY setup/index.html /usr/share/nginx/html/index.html
COPY setup/default.conf.template ${NGINX_DIR}/templates/default.conf.templateç

RUN mkdir -p ${NGINX_DIR}/certs
COPY setup/ckan-local.* ${NGINX_DIR}/certs/

EXPOSE ${NGINX_PORT}
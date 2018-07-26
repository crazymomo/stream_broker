FROM buildpack-deps:stretch

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

# Versions of Nginx and nginx-rtmp-module to use
ENV NGINX_VERSION nginx-1.15.0
ENV NGINX_RTMP_MODULE_VERSION 1.2.1

# Install dependencies
RUN apt-get update && \
    apt-get install -y ca-certificates openssl libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# install libraries
RUN apt-get update
RUN apt-get install -yy net-tools htop ffmpeg

# Download and decompress Nginx
RUN mkdir -p /tmp/build/nginx && \
    cd /tmp/build/nginx && \
    wget -O ${NGINX_VERSION}.tar.gz https://nginx.org/download/${NGINX_VERSION}.tar.gz && \
    tar -zxf ${NGINX_VERSION}.tar.gz

# Use local repositroy instead wgeting from internet
ADD service/nginx-rtmp-module /tmp/build/nginx-rtmp-module

# Build and install Nginx
# The default puts everything under /usr/local/nginx, so it's needed to change
# it explicitly. Not just for order but to have it in the PATH
RUN cd /tmp/build/nginx/${NGINX_VERSION} && \
    ./configure \
        --sbin-path=/usr/local/sbin/nginx \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=/var/log/nginx/error.log \
        --pid-path=/var/run/nginx/nginx.pid \
        --lock-path=/var/lock/nginx/nginx.lock \
        --http-log-path=/var/log/nginx/access.log \
        --http-client-body-temp-path=/tmp/nginx-client-body \
        --with-http_ssl_module \
        --with-threads \
        --with-ipv6 \
        --add-module=/tmp/build/nginx-rtmp-module

# make file
RUN cd /tmp/build/nginx/${NGINX_VERSION} \
    make -j $(getconf _NPROCESSORS_ONLN) && \
    make install && \
    mkdir /var/lock/nginx

# Forward logs to Docker
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \
    ln -sf /dev/stderr /var/log/nginx/error.log

# Set up config file
COPY config /opt/config
RUN rm /etc/nginx/nginx.conf
RUN ln -s /opt/config/nginx.conf /etc/nginx/nginx.conf

EXPOSE 1935
CMD ["nginx", "-g", "daemon off;"]

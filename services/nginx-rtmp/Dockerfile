FROM tiangolo/nginx-rtmp

# install libraries 
RUN apt-get update
RUN apt-get install -yy net-tools inotify-tools htop ffmpeg

# copy nginx config
COPY config /opt/config
RUN rm /etc/nginx/nginx.conf
RUN ln -s /opt/config/nginx.conf /etc/nginx/nginx.conf

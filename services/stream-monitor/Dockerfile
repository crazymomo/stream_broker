FROM ubuntu:16.04

# install libraries 
RUN apt-get update
RUN apt-get install -yy net-tools inotify-tools htop ffmpeg

# run root
CMD [ "bash", "/opt/script/monitor.sh" ]

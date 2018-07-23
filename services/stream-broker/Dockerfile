FROM python:3

# install libraries 
RUN apt-get update
RUN apt-get install -yy net-tools inotify-tools htop ffmpeg

# set working dir
WORKDIR /usr/src/app

# install requirements
COPY ./config/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# run root
CMD [ "python", "-m",  "root" ]

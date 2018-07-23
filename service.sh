#! /bin/bash

# set static variables
COLOR_RED='\033[0;31m'
COLOR_GREEN='\033[0;32m'
COLOR_BLUE='\033[0;34m'
COLOR_PURPLE='\033[0;35m'
COLOR_NO='\033[0m'

log() {
    echo -e "$COLOR_RED$@$COLOR_NO"
}

# check function exist or not
command_exist() {
    if [ -n "$(type -t $1)" ] && [ "$(type -t $1)" = function ]; then 
        echo 0
    else
        echo 1 
    fi
}

# ===================================== command list =====================================

init() {
    # init service
    cd $DIR/services
    docker-compose build
}

start() {
    # start service
    cd $DIR/services
    docker-compose up -d
}

stop() {
    # stop service
    cd $DIR/services
    docker-compose down
}

restart() {
    # restart service
    stop
    start
}

test() {
    # get full file path
    fullfile=$DIR/data/sample_data/$1

    # check file is exited
    if [ -f $fullfile ]; then 
        # trim extension
        filename=$(basename -- "$fullfile")
        filename="${filename%.*}"

        # start ffmpeg to upload stream
        docker exec -ti nginx-rtmp ffmpeg -re -i /opt/sample_data/$1 -vcodec libx264 -acodec aac -f flv rtmp://localhost/src/$filename
    else
        echo "$fullfile is not existed"
    fi
}

testlog() {
    # if rpeort log is not existed, create it.
    if [ ! -f $DIR/data/log_data/report.log ]; then
        touch $DIR/data/log_data/report.log
    fi

    # bind report log
    docker exec -ti stream-monitor tail -F /opt/log_data/report.log
}

# ===================================== main logic =====================================

# Make sure only root can run our script
if [ "$(uname)" == "Darwin" ]; then
    :
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    if [ "$(id -u)" != "0" ]; then 
        echo "This script must be run as root"
        exit 1
    fi
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    :
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
    :
fi

# get current dir
DIR=$(cd $(dirname $0) && pwd)
# change working directory
cd $DIR

# check command support or not
if [ ! -z $1 ] && [ $(command_exist "$1") == 0 ]; then
    # should stop when receive non-zero status
    set -e
    # do command
    "$1" "${@:2:${#}}"
fi

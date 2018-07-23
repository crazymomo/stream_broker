#!/bin/bash

duration() {
    ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 $1
}

log() {
    date=$(date --rfc-3339=seconds)
    path=$1
    m3u8="$path"index.m3u8
    duration=$(duration $path$file)
    echo $date - [$file] [$duration]["$path"index.m3u8] >> /opt/log_data/report.log
}

inotifywait -r -m /opt/hls_data -e close_write -e moved_to |
while read path action file; do
    if [[ "$file" =~ .*ts$ ]]; then
        log $path $file 
    fi
done

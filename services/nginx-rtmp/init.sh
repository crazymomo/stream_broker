#!/bin/bash

# get current dir
DIR=$(cd $(dirname $0) && pwd)
cd $DIR

# move to nginx
cd $DIR/service/nginx
git submodule update

# move to nginx-rtmp-module
cd $DIR/service/nginx-rtmp-module
git submodule update

# revert to clean repository
git checkout . 
git clean -f -d

# apply patch
git apply $DIR/patch/nginx-rtmp-module.patch

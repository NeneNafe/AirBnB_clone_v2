#!/usr/bin/env bash
#sets up web servers for the deployment of web_static
source=/data/web_static/releases/test/
symlink=/data/web_static/current
configcode="location /hbnb_static {
    alias /data/web_static/current/
    index index.html
}"
sudo apt-get install -y nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "snippet content" | sudo tee "$source/index.html"
if [ -e "$symlink "]; then
    rm "$symlink"
fi
sudo ln -s $source $symlink
sudo chown -R ubuntu:ubuntu /data/
#!/usr/bin/env bash
#sets up web servers for the deployment of web_static
source=/data/web_static/releases/test/
symlink=/data/web_static/current
configcode="location /hbnb_static {
    alias /data/web_static/current/;
    index index.html;
};"
configfile=/etc/nginx/sites-enabled/default
if ! command -v nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "snippet content" | sudo tee -a "$source/index.html"
if [ -e "$symlink "]; then
    sudo rm "$symlink"
fi

sudo ln -s $source $symlink
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/server {/a '"$configcode" "$configfile"
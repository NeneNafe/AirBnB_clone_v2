#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -hR ubuntu:ubuntu /data/

printf %s "server {
    listen 80;
    listen [::]:80;

    add_header X-Served-By 318591-web-01;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        try_files $uri $uri/ =404;
    }
    location /redirect_me {
        return 301 http://github.com/NeneNafe;
    }
    error_page 404 /404.html;
    location = /404.html {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-enabled/default

service nginx restart

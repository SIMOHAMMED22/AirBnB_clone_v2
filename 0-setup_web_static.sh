#!/usr/bin/env bash
# Sets up your web servers for the deployment of web_static

sudo apt -y update
sudo apt -y install nginx
sudo mkdir -p /data
sudo mkdir -p /data/web_static
sudo mkdir -p /data/web_static/releases
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo sh -c 'echo "hi there!"  > /data/web_static/releases/test/index.html'
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '/^}$/i \ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart

#!/usr/bin/env bash

# Install Nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
  sudo apt-get update
  sudo apt-get -y install nginx
fi

# Create necessary folders if they don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/

# Create a fake HTML file for testing
echo "<html><body>Hello, this is a test</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link (delete and recreate if it already exists)
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_text="server {
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}"
echo "$config_text" | sudo tee /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

# Exit successfully
exit 0


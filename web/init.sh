#!/bin/bash

PRJ_NAME=stepic-web-technologies

echo "mv $HOME/$PRJ_NAME/web ."
mv $HOME/$PRJ_NAME/web .

echo "rm -rf $HOME/$PRJ_NAME"
rm -rf $HOME/$PRJ_NAME

echo "sudo rm /etc/nginx/sites-enabled/default"
sudo rm /etc/nginx/sites-enabled/default

echo "sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/tasyrkin_web.conf"
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/tasyrkin_web.conf

echo "sudo /etc/init.d/nginx restart"
sudo /etc/init.d/nginx restart

echo 'sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py'
sudo ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py

echo 'sudo /etc/init.d/gunicorn restart'
sudo /etc/init.d/gunicorn restart

# sudo /etc/init.d/mysql start

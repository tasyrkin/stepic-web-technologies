sudo rm /etc/ngnix/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/tasyrkin_web.conf
sudo /etc/init.d/nginx restart
# sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
# sudo /etc/init.d/gunicorn restart
# sudo /etc/init.d/mysql start
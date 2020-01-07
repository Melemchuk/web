sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
sudo -c /home/box/web/etc/gunicorn.conf hello:wsgi_application
sudo -c /home/box/web/etc/gunicorn-django.conf ask.wsgi_application

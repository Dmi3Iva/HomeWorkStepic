#nginx
sudo rm -rf /etc/nginx/sites-enabled/default /etc/nginx/sites-availibale/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart

#gunicorn
#sudo rm -f /etc/gunicorn.d/hello.py
sudo touch /home/box/web/gunicorn.log
#sudo ln -sf /home/box/web/etc/django.py /etc/gunicorn.d/hello.py
#sudo ln -sf /home/box/web/etc/django.py /etc/gunicorn.d/django.py
#sudo gunicorn -c /etc/gunicorn.d/django.py ask.wsgi

sudo ln -sf /home/box/web/etc/gunicorn_django.conf /etc/gunicorn.d/gunicorn_django.conf

sudo /etc/init.d/gunicorn restart gunicorn_django.conf

#mysql

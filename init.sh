#nginx
sudo rm -rf /etc/nginx/sites-enabled/default /etc/nginx/sites-availibale/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-available/default
sudo /etc/init.d/nginx restart

#gunicorn
sudo /etc/init.d/gunicorn stop
sudo touch /home/box/web/gunicorn.log
sudo ln -sf /home/box/web/etc/django_conf.py /etc/gunicorn.d/django_conf.py
sudo gunicorn -c /etc/gunicorn.d/django_conf.py ask.wsgi:application

#mysql
sudo /etc/init.d/mysql start
mysql -uroot -e "create database db_stepic"

python ask/manage.py makemigrations qa
python ask/manage.py migrate
#python ask/manage.py syncdb

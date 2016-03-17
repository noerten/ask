sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo rm /usr/bin/python2.7
sudo ln -sf /usr/bin/python3.4 /usr/bin/python2.7
sudo apt-get update
sudo apt-get install libmysqlclient-dev
sudo apt-get install python3-dev python-dev libxml2-dev libxslt1-dev zlib1g-dev
sudo pip install --upgrade pip
sudo pip install django
sudo pip install gunicorn
sudo pip install django-autofixture
sudo pip install mysqlclient 
sudo sed -i 's/skip-external-locking/skip-external-locking\ninnodb_use_native_aio = 0/' /etc/mysql/my.cnf
sudo /etc/init.d/mysql restart
mysql -uroot -e "create database stepic;"
mysql -uroot -e "CREATE USER 'trasea'@'localhost' IDENTIFIED BY 'trasea';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON * . * TO 'trasea'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
sudo /etc/init.d/nginx restart


# Stack
* **python** 3.7
* **django** 2.1
* **restframework** 3.9

## Set up server on local
```console
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

## Set up database(MariaDB) on a docker container
```console
$ docker-compose up -d (It can take some time when first up)
$ python manage.py migrate
```

## RUN
```console
$ python manage.py runserver
```

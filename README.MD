I have implemented it on heroku here is the link:

```
    fafadgaeg
```

## First-time setup

1.  Make sure Python 3.7x and Pipenv are already installed. [See here for help](https://djangoforbeginners.com/initial-setup/).
2.  Clone the repo and configure the virtual environment:

```
$ git clone https://github.com/vinhbui107/newspaper-website.git
$ cd newspaper-website
$ pipenv install
$ pipenv shell
```

3.  Set up the initial migration for our custom user models and build the database.

```
(djangox) $ python manage.py makemigrations
(djangox) $ python manage.py migrate
```

4.  Create a superuser:

```
(djangox) $ python manage.py createsuperuser
```

5.  Confirm everything is working:

```
(djangox) $ python manage.py runserver
```

Load the site at [http://127.0.0.1:8000](http://127.0.0.1:8000).

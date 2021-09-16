# DRF Demo

DRF Demo is a [Django REST Framework](https://github.com/encode/django-rest-framework) project reference <...> currency and location fixture API.

<img align="right" src="./documentation/images/drf-demo-schema.png" alt="screenshot runserver in browser">

The codebase associated with this project provides a comprehensive implementation of the following features:

- **Heroku**-compatible environment and dependency management using the [Pipenv](https://github.com/pypa/pipenv) library -- See [Pipfile](./Pipfile) | [Pipfile.lock](./Pipfile.lock).

- **Environment-specific project settings** with a `.env` file and the [Python Decouple](https://github.com/henriquebastos/python-decouple/) library -- See [settings.py](./config/settings.py) | [.env](./.env.example)

- **Custom User model** that uses an email address instead of a username -- See [settings.py](./config/settings.py) | [user.models.py](./user/models.py)

- **PostgreSQL** database configuration settings in conjunction with the [psycopg2](https://github.com/psycopg/psycopg2) database adapter -- See [settings.py](./config/settings.py)

- **Amazon AWS S3**-compatible static and media **file hosting** configuration settings in conjunction with the [boto3](https://github.com/boto/boto3) and [django storages](https://github.com/jschneier/django-storages) libraries -- See [settings.py](./config/settings.py) | [storages.py](./config/storages.py)

- **Celery** and **Redis**-compatible project settings for **scheduled and background tasks** in conjunction with [Celery](https://github.com/celery/celery) and [redis-py](https://github.com/andymccurdy/redis-py) -- See [settings.py](./config/settings.py) | [celery.py](./config/celery.py) | [Procfile](./Procfile) | [currency.tasks.py](./currency/tasks.py)

- **Nested API routes** that model database relations in conjunction with the [drf-nested-routers](https://github.com/alanjds/drf-nested-routers) library -- See [api.urls](./api/urls.py)

- **Searchable, sortable, and filterable** endpoints with **side-loadable and traversable relations** in conjunction with the [Dynamic REST](https://github.com/AltSchool/dynamic-rest) library -- See serializers.py and views.py in each project submodule.

- **Unit testing** for models and views -- See test_models.py and test_views.py in the tests directory of each project submodule.

- **Heroku** deployment-ready project settings in conjunction with the [Django-Heroku](https://github.com/heroku/django-heroku) library -- See [settings.py](./config/settings.py) | [Procfile](./Procfile) | [release.sh](./release.sh)

## Live Demo

The live demo of this project is hosted on a Heroku free tier pipeline. Please note that

For convenience, the Browsable API feature has been enabled so that you can easily navigate the API within your browser.

### Endpoints

### Sorting

### Filtering


## Local Installation

Clone this repository into a directory of your choosing:

```console
$ git clone https://github.com/khunspoonzi/drf-demo.git
```

Navigate into the root directory of the newly cloned repository:

```console
$ cd drf-demo
```

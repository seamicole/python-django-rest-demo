# DRF Demo

DRF Demo is a Django REST Framework demo API and project reference.

<img align="right" src="./documentation/images/drf-demo-schema.png" alt="screenshot runserver in browser">

This codebase associated with this project provides a comprehensive implementation of the following features:

- **Heroku**-compatible environment and dependency management using the [Pipenv](https://github.com/pypa/pipenv) library -- See [Pipfile](./Pipfile) | [Pipfile.lock](./Pipfile.lock).

- Environment-specific project settings with a `.env` file and the [Python Decouple](https://github.com/henriquebastos/python-decouple/) library -- See [settings.py](./config/settings.py) |  [.env](./.env.example)

- **Custom User model** uses an email address instead of a username -- See [user / models.py](./user/models.py)

- **PostgreSQL** database configuration settings in conjunction with the [psycopg2](https://github.com/psycopg/psycopg2) database adapter -- See [settings.py](./config/settings.py)

- **Amazon AWS S3**-compatible static and media file hosting configuration settings in conjunction with the [boto3](https://github.com/boto/boto3) and [django storages](https://github.com/jschneier/django-storages) libraries -- See [settings.py](./config/settings.py) | [storages.py](./config/storages.py)

- **Celery** and **Redis**-compatible project settings for scheduled and background tasks in conjunction with [Celery](https://github.com/celery/celery), [django-celery-beat](https://github.com/celery/django-celery-beat), and [redis-py](https://github.com/andymccurdy/redis-py) -- See [settings.py](./config/settings.py) | [celery.py](./config/celery.py) | [Procfile](./Procfile) | [currency / tasks.py](./currency/tasks.py)

- **Heroku** deployment-ready project settings in conjunction with the [Django-Heroku](https://github.com/heroku/django-heroku) library -- See [settings.py](./config/settings.py) | [Procfile](./Procfile) | [release.sh](./release.sh)


## Installation

Pellentesque vestibulum iaculis nisl. In accumsan leo nec dolor accumsan, nec rhoncus ipsum mattis. Maecenas ornare maximus orci, nec fringilla ante dictum non. Fusce volutpat justo ac nisi volutpat, tempus faucibus mi fringilla. Phasellus tempus vestibulum ante, at vehicula risus tristique ac. Curabitur gravida tellus ac dignissim elementum. Nam suscipit congue pellentesque. Sed nisi nisi, malesuada quis tempor at, iaculis nec ex. Proin ac dolor eget ipsum mollis feugiat. Maecenas eu pretium lacus, ac consequat ligula. Etiam vestibulum purus ut diam pellentesque gravida. Maecenas pulvinar convallis ex, pellentesque vestibulum lorem mollis rutrum. Duis quis efficitur augue. Vivamus congue nunc non dignissim pretium. Duis sit amet elementum tortor.

Nulla eget lobortis ipsum, non interdum neque. Sed varius elementum purus, sit amet luctus augue venenatis in. In ut maximus dolor. Donec nec dui non sem iaculis fringilla. Nam lacinia augue risus, et rhoncus est malesuada quis. Vestibulum non tristique dui. Vivamus ac nisl neque. Morbi ipsum felis, consequat sit amet dignissim in, dictum nec purus. Vivamus molestie euismod ligula vel viverra. In at pulvinar dui, nec cursus ligula. Ut scelerisque ante quis porta facilisis.

Nullam id tortor nulla. Aenean id aliquam massa. Ut dui magna, vehicula ac convallis at, maximus nec leo. Praesent leo mi, semper et venenatis ut, tristique eu mi. Sed sed rhoncus sapien. Pellentesque bibendum quam ut ante feugiat, sed blandit lorem volutpat. Fusce cursus mattis tellus, sit amet placerat lacus porttitor vel. Vestibulum eu tellus velit. Sed varius vitae risus a faucibus. Sed congue vel elit vel consectetur.

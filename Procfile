release: ./release.sh
web: gunicorn config.wsgi
worker: celery --app config.celery.app worker -B --scheduler django_celery_beat.schedulers:DatabaseScheduler

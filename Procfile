web: gunicorn appyoutube:appyoutube --timeout 0
worker: celery worker --app=appyoutube.appcelery
REDIS_URL=redis://localhost:6379
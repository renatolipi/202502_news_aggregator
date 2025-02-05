# NEWS AGGREGATOR


#### 2025 project


### Details

This is a simple project built with Python, Poetry, Django, Celery, Kombu with SQLite (message broker), BeautifulSoup4, Requests and Flower for queue monitoring. The objective is to configure Celery and run tasks scheduled and asynchronously, but in a small and simple structure. Will use Django as a web framework and its apps to separate the news scrapers.

Later I added Selenium, using it headlessly, in order to get responses from AJAX pages.


## How to install
...

one of the steps is to `python manage.py migrate`

I'll cover it better later.

## How to run

If you want to have the web app running:
```bash
python manage.py runserver
```
but it's not needed at this point.


Start worker:
```bash
poetry run celery -A news_aggregator.celery worker --loglevel=info
```

Start beat:
```bash
poetry run celery -A news_aggregator.celery beat --loglevel=info
```

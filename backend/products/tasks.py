import json
from celery import states
from celery.exceptions import Ignore

from drfAssignment.celery import app
from services.web_crawlers.crawlers_api import crawl
from services.web_crawlers.web_crawlers.spiders.europe361_crawl import Europe361Crawl
from services.web_crawlers.web_crawlers.spiders.glamorous_uk_crawl import GlamorousUkCrawl


@app.task(bind=True, name="run.spider")
def run_spider(self, spider_name):
    if spider_name == "glamorous-uk-crawl":
        crawl(GlamorousUkCrawl)
    elif spider_name == "europe361_crawl":
        crawl(Europe361Crawl)
    else:
        self.update_state(state=states.FAILURE, meta="Invalid Spider name")
        raise Ignore()

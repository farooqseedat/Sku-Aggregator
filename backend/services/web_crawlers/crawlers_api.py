import os
import json

from scrapy.crawler import CrawlerProcess
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor


def crawl(spider_name):
    settings_file_path = 'services.web_crawlers.web_crawlers.settings' # The path seen from root
    os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
    process = CrawlerProcess(get_project_settings())
    defered = process.crawl(spider_name)
    defered.addCallback(lambda _:reactor.stop())
    reactor.run()

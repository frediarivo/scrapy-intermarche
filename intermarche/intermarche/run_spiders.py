"""
Lancer multiple spider sequentiellement
"""
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

import SpiderMagasin, SpiderCategory, SpiderProduct, SpiderProductInfo

configure_logging()
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(SpiderMagasin)
    yield runner.crawl(SpiderCategory)
    yield runner.crawl(SpiderProduct)
    yield runner.crawl(SpiderProductInfo)
    reactor.stop()

crawl()
reactor.run() # the script will block here until the last crawl call is finished
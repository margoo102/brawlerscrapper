from scrapy.crawler import CrawlerProcess

from brawlers import BrawlersSpider

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'ITEM_PIPELINES': {'pipelines.MyJsonPipeline': 300}
})

process.crawl(BrawlersSpider)
process.start()

process.join()
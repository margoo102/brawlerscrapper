import scrapy
from scrapy.crawler import CrawlerProcess, Crawler


class QuotesSpider(scrapy.Spider):

    name = 'brawler'

    def __init__(self, *args, **kwargs):
        brawler = args[1]["brawler"]
        self.start_urls = [
            f'https://brawlstars.fandom.com/wiki/{brawler}'
        ]
        super().__init__(*args, **kwargs)

    def parse(self, response):
        for quote in response.css('aside.portable-infobox'):
            items = {item.xpath('./h3/text()').get():
                         item.xpath('./div/text()').get()
                     for item in quote.xpath('./div')}

            health = [{entry.xpath('./td[1]/text()').get():
                           entry.xpath('./td[2]/text()').get()
                           for entry in item.css('tr')}
                      for item in quote.xpath('./section[1]')]

            attack = [
                {stat.xpath('./h3/text()').get():
                     stat.xpath('./div/text()').get()
                 for stat in item.xpath('./div')}
                for item in quote.xpath('./section[2]')]

            attacks_per_level = [
                {stat.xpath('./td[1]/text()').get():
                     stat.xpath('./td[2]/text()').get()
                 for stat in item.css('tr')}
                for item in quote.xpath('./section[2]')]

            super_attack = [
                {stat.xpath('./h3/text()').get():
                     stat.xpath('./div/text()').get()
                 for stat in item.xpath('./div')}
                for item in quote.xpath('./section[3]')]

            supers_per_level = [
                {stat.xpath('./td[1]/text()').get():
                     stat.xpath('./td[2]/text()').get()
                 for stat in item.css('tr')}
                for item in quote.xpath('./section[3]')]

            yield {
                'name': quote.css('h2.pi-item::text').get(),
                'details': items,
                'health': health,
                'attack': {
                    'details': attack,
                    'levels': attacks_per_level
                },
                'super': {
                    'details': super_attack,
                    'levels': supers_per_level
                }
            }


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'ITEM_PIPELINES': {'pipelines.MyJsonPipeline': 300}
})

crawler = Crawler(QuotesSpider, {
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'ITEM_PIPELINES': {'pipelines.MyJsonPipeline': 300},
    'BRAWLER': 'Colt'
})

process.crawl(crawler, ["brawler", {"brawler": "Bo"}])
process.start()

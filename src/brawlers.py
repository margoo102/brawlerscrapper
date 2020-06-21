import scrapy


class BrawlersSpider(scrapy.Spider):

    name = 'brawlers'

    def __init__(self, **kwargs):
        self.start_urls = [
            f'https://brawlstars.fandom.com/wiki/Shelly'
        ]
        super().__init__(**kwargs)

    def parse(self, response):
        items = [item.xpath('./text()').get() for item in response.css(
                'body > div.WikiaSiteWrapper '
                '> header > nav > ul > li:nth-child(1) '
                '> div '
                '> div.wds-is-not-scrollable.wds-dropdown__content '
                'a')]

        def fil(value):
            if value in ["\n\t\t\t\t\t\t\t\t\t\t\t\t", "More..."]:
                return False
            else:
                return True

        filtered = list(filter(fil, items))

        yield {"items": filtered}






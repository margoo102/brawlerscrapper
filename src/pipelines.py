from scrapy.exporters import JsonItemExporter, CsvItemExporter


class MyJsonPipeline(object):

    def __init__(self, file="out/brawlers.json"):
        self.file = open(file, 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    # def from_settings(self):
    #     self.file = open("out/brawlers.json", 'wb')
    #     self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
    #     self.exporter.start_exporting()
    #     return self

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class MyCsvPipeline(object):

    def __init__(self):
        self.file = open("brawlers.csv", 'wb')
        self.exporter = CsvItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

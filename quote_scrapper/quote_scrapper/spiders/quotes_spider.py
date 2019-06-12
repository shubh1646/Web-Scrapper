import scrapy
class QuotedSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)




#     def start_request(self):
#         urls = [
#                'http://quotes.toscrape.com/page/1/',
#             'http://quotes.toscrape.com/page/2/',
#         ]
#         for url in urls :
#             yield scrapy.Request(url=url , callback=self.parse)



#     def parse(self, response):
#         page_id = response.url.split("/")[-2]
#         filename = "quotes-%s.html"%page_id
#         with open(filename, 'wb') as f:
#             f.write(response.body)

#         self.log("Saved File %s"%filename)

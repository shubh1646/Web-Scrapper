import scrapy


class QuotedSpider(scrapy.Spider):
    name = "quotes_spider"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        quotes = response.css("div.quote")

        for quote in quotes:
            text = quote.css("span.text::text").get(),
            print(text)
            author = quote.css("small.author::text").get(),
            print(author)
            tags = quote.css("a.tag::text").getall()

            yield {
                "quote": text,
                "author": author,
                "tag": tags,
            }
            next_page_id = response.css("li.next a::attr(href)").get()
            if next_page_id is not None:
                next_page = response.urljoin(next_page_id)
                yield scrapy.Request(next_page, callback=self.parse)

import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon_spider"
    print("lets starts")
    page_no = 2

    def start_requests(self):
        print("inside start request")
        urls = [
            "https://www.amazon.com/s?k = mobiles+phones & page = 1 & crid = 39Y5STO9084OS & qid = 1560789439"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        products = response.css("div.a-section.a-spacing-medium")
        print("starting product")
        for product in products:

            name = product.css(
                "span.a-size-medium.a-color-base.a-text-normal::text").get()
            price = product.css("span.a-offscreen::text").get()
            no_of_people_Reviewd = product.css("span.a-size-base::text").get()
            image = product.css("img.s-image::attr(src)").get()

            if name is None or price is None or no_of_people_Reviewd is None or image is None:
                continue
            else:
                yield {
                    "Product Name": name,
                    "Price": price,
                    "Number of Reviews": no_of_people_Reviewd,
                    "image link": image,
                }
        next_page = "https://www.amazon.com/s?k=mobiles+phones&page=" + \
            str(AmazonSpider.page_no)+"&crid=39Y5STO9084OS&qid=1560789439"

        if AmazonSpider.page_no <= 5:

            AmazonSpider.page_no = AmazonSpider.page_no + 1
            print("inside loop for" + str(AmazonSpider.page_no) + "time")
            yield scrapy.Request(next_page, callback=self.parse)

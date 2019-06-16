import scrapy


class QuoteSpider(scrapy.Spider):
    name = "amazon_spider"
    print("lets starts")

    def start_requests(self):
        print("inside start request")
        urls = [
            "https://www.amazon.com/s?k=mobiles+phones&crid=39Y5STO9084OS&sprefix=mobiles+phone%2Caps%2C131&ref=nb_sb_ss_i_1_13"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        print("inside parse method")
        products = response.css("div.a-section.a-spacing-medium")
        print("starting product")

        for product in products:

            print("inside the loop")
            name = product.css(
                "span.a-size-medium.a-color-base.a-text-normal::text").get()
            price = product.css("span.a-offscreen::text").get()
            no_of_people_Reviewd = product.css("span.a-size-base::text").get()
            image = product.css("img.s-image::attr(src)").get()

            print(name)
            print(price)
            print(no_of_people_Reviewd)
            print(image)
            if name is None or price is None or no_of_people_Reviewd is None or image is None:
                continue
            else:
                yield {
                    "Product Name": name,
                    "Price": price,
                    "Number of Reviews": no_of_people_Reviewd,
                    "image link": image,
                }

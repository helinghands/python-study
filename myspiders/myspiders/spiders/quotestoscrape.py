import scrapy

from myspiders.items import Product


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.amazon.cn/%E6%89%8B%E6%9C%BA-%E9%80%9A%E8%AE%AF/b/ref=sa_menu_top_mobile_l1?ie=UTF8&node=664978051',
    ]

    def parse(self, response):
        print(response.text)
        item = Product()
        print("====================================="*2)
        for li in response.css("div.a-container"):
            yield {
                'price': li.css('div.floor-s9-asin-text2::text').extract_first(),
                'name': li.css('div.floor-s9-asin-text1::text').extract_first(),
                'imgPath':li.css('div img::attr(src)').get()
            }
            # f.write(li.css('div.floor-s9-asin-text2::text').extract_first()+"\n")
            # f.write(li.css('div.floor-s9-asin-text1::text').extract_first()+"\n")
            # f.write(li.css('div img::attr(src)').get()+"\n")
            # print(li.css('div.floor-s9-asin-text2::text').get())
            # print(li.css('div.floor-s9-asin-text1::text').extract_first())
            # print(li.css('div img::attr(src)').get())
        print("====================================="*2)
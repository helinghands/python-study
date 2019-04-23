# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Product(scrapy.Item):
    # define the fields for your item here like:
    # 产品名称
    name = scrapy.Field()
    # 产品价格
    price = scrapy.Field()
    # 图片路径
    imgPath = scrapy.Field()

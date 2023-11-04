# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class ShopifyAppsItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class Category(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    subcategories = scrapy.Field()
    featured_apps = scrapy.Field()

class App(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    short_description = scrapy.Field()
    description = scrapy.Field()
    rating = scrapy.Field()
    reviews = scrapy.Field()
    developer = scrapy.Field()
    developer_url = scrapy.Field()
    pricing = scrapy.Field()
    launched = scrapy.Field()
    languages = scrapy.Field()
    categories = scrapy.Field()
    works_with = scrapy.Field()
    review_summary = scrapy.Field()

class PricingPlan(scrapy.Item):
    app_id = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    feature = scrapy.Field()

class Review(scrapy.Item):
    name = scrapy.Field()
    country = scrapy.Field()
    time_used = scrapy.Field()
    date = scrapy.Field()
    rating = scrapy.Field()
    comment = scrapy.Field()
    app = scrapy.Field()
    replied_date = scrapy.Field()
    replied_comment = scrapy.Field()

class Developer(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    description = scrapy.Field()
    number_of_apps = scrapy.Field()
    average_rating = scrapy.Field()
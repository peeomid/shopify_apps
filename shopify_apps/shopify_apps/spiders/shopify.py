import scrapy


class ShopifySpider(scrapy.Spider):
    name = 'shopify'
    allowed_domains = ['apps.shopify.com']
    # https://apps.shopify.com/sitemap.xml
    start_urls = [
        'https://apps.shopify.com/categories/finding-products',
        'https://apps.shopify.com/categories/selling-products',
        'https://apps.shopify.com/categories/orders-and-shipping',
        'https://apps.shopify.com/categories/store-design',
        'https://apps.shopify.com/categories/marketing-and-conversion',
        'https://apps.shopify.com/categories/store-management',
    ]

    def start_requests(self):
        # return super().start_requests()
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_category_page)
    # def parse(self, response):
    #     pass

    def parse_category_page(self, response):
        title = response.xpath('//h1/text()').get()
        description = response.xpath('//h1/following-sibling::h2[1]').get()

        other_categories = response.xpath("//a[starts-with(@href, 'https://apps.shopify.com/categories/')]/@href")

        for category in other_categories:
            yield scrapy.Request(category, callback=self.parse_category_page)

    def parse_app_page(self, response):
        pass

    def parse_review_page(self, response):
        pass

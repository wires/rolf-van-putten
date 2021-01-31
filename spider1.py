import scrapy

class BlogSpider(scrapy.Spider):
    name = 'putten'
    start_urls = ['https://rolf-van-putten.zoom.nl']

    def parse(self, response):
        for link in response.css('li.photoBlock h3 > a'):
            yield {'foto_link': link.css('a ::attr(href)').get()}

        for next_page in response.css('a.paginatorLink'):
            yield response.follow(next_page, self.parse)
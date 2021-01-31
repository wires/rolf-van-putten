import scrapy

class BlogSpider(scrapy.Spider):
    name = 'putten'
    start_urls = ['https://rolf-van-putten.zoom.nl/albums/index.html']

    # overview with all albums
    def parse(self, response):
        for album_link in response.css('h3 > a.album'):
            yield response.follow(album_link, self.parse_album)

    # album page
    def parse_album(self, response):
        album = response.css('#description > h1 ::text').get()
        for link in response.css('ul.photodescription > li.title h3 > a'):
            yield {'album': album, 'foto_link': link.css('a ::attr(href)').get()}

        for album_next_page_link in response.css('a.paginatorPage'):
            yield response.follow(album_next_page_link, self.parse_album)

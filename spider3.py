import json
import scrapy

# deze download een foto (niet in album)


def load(fn):
    with open(fn, 'r') as json_file:
        return json.load(json_file)


baseUrl = "https://zoom.nl/"
projectLink = lambda o: baseUrl + o['foto_link']

links1 = list(map(projectLink, load("album-links.json")))


class WatEenKutTaalIsPythonToch(scrapy.Spider):
    name = 'adsf'
    start_urls = links1

    def parse(self, response):
        imgSrc = response.css('div#imageloader > img ::attr(src)').get()
        datum = response.css('dl.imagespecs dd:nth-child(2)::text').get()
        title = response.css('h1[itemprop="name"]::text').get()
        comments = []

        for c in response.css('div.commentWrapper'):
            name = c.css('a.name::text').get()
            date = c.css('span.date::text').get()
            comment = ''

            for regel in c.css('p *::text'):
                comment += regel.get()

            comments.append({'name': name, 'date': date, 'comment': comment})

        foto_info = {
            'url': response.url.replace(baseUrl, ''),
            'img_src': imgSrc,
            'date': datum,
            'comments': comments,
            'title': title
        }

        yield foto_info

import scrapy


class GithubtrendingrepoSpider(scrapy.Spider):
    name = 'githubTrendingRepo'
    allowed_domains = ['github.com/trending/']
    start_urls = ['http://github.com/trending//']

    def parse(self, response):
        title_text = response.xpath('//title[1]/text()') 
        print(title_text.get())
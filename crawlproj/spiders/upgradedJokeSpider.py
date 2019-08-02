import scrapy
from crawlproj.items import JokeItem
from scrapy.loader import ItemLoader

class JokesSpider(scrapy.Spider):
    name = 'upspooders'
    # This will be a uniqie name for your spider
    # which you will call 'scrapy crawl spooders -o data.json'
    # another way is 'scrapy runspider quotes_spider.py -o quotes.json'

    start_urls = [
        'http://www.laughfactory.com/jokes/family-jokes'
    ]

    def parse(self, response):
        # .xpath basically grabs all divisors with class=joke-text and save them into an array
        for joke in response.xpath("//div[@class='joke-text']"):
            loader = ItemLoader(item=JokeItem(), selector=joke)
            
            # first one gets just the text, second one gets the pid with the text (basically whole para with labels)
            # 'joke_text': joke.xpath("./p/text()").get() 
            # 'joke_text': joke.xpath("./p").get()

            loader.add_xpath('joke_text',"./p")
            yield loader.load_item()
        

        # this is for scraping the next few pages
        # if we monitor the html closely, theres a next button, in which we can obtain the link for it
        # we can then go to the next page to get the data
        
        # go_next = response.xpath("//li[@class='next']/a/@href").get()
        # if go_next is not None:
        #     print(response.urljoin(go_next))
        #     next_link= response.urljoin(go_next)
        #     yield scrapy.Request(url = next_link, callback = self.parse)
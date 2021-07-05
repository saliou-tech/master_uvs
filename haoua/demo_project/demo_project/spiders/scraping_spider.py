import scrapy
from ..items import  DemoProjectItem

class ScrapingSpider(scrapy.Spider):
    #Nom du spider
    name = "extraction"
    url=[]
    #URL de la page à scraper
    start_urls = [
        "https://www.seneweb.com/"
    ]

    def __init__(self):
        self.links=[]

    BASE_URL='https://www.seneweb.com'
    def parse(self, response):
        #items = DemoProjectItem()

        self.links.append(response.url)
        links=response.css('a.module_main_post_title').xpath('@href').extract()
        for link in links:
            absolute_url=self.BASE_URL +link
            self.url=[]
            self.url.append(absolute_url)
            #print(absolute_url)
            yield scrapy.Request(absolute_url,callback=self.parse_dir_contents)
        #art_categorie = response.css('span.post_header_categ::text').extract()
        #art_categorie=response.xpath("//span[@class='post_header_categ']/text()").extract()
        #art_titre = response.css('h1::text').extract()
        #art_titre=response.xpath("//h1/text()").extract()
        # art_texte = response.css('font::text').extract()
        # art_auteur = response.css('span.meta_item.meta_source>a::text').extract()
        # art_date_pub = response.css('span.meta_item::text').extract()
        # art_audience = response.css('span::text').extract()
        # art_nombre_comments = response.css('span::text').extract()


        # items['categorie'] = art_categorie,
        # items['titre'] = art_titre,
        # items['texte'] = art_texte,
        # items['auteur'] = art_auteur,
        # items['datepub'] =  art_date_pub,
        # items['audiences'] =  art_audience,
        # items['nb_comments'] =  art_nombre_comments

        # yield items


    def parse_dir_contents(self,response):
        items=DemoProjectItem()
        tous_articles=response.css('div.posts_block_content')

        for article in tous_articles:
            categorie=article.css('span.post_header_categ::text').extract()
            self.url=article.css('a.module_news_item_title').xpath('@href').extract()
            titre=article.css('h1::text').extract()
            texte=article.css('font::text').extract()
            publication=article.css('div span.meta_item::text').extract()
            auteur=article.css('div.article_author p::text').extract()
            vue=article.css('span span::text').extract()
            #=article.css('div.comment_item_content').extract()

            items['categorie'] = categorie,
            items['url']=self.url,
            items['titre'] = titre,
            items['texte'] = texte,
            items['auteur'] = auteur,
            items['publication']=publication,
            items['vue']=vue,
            #items['tous_commentaire']=tous_commentaire

            yield items
            
            # items['datepub'] =  art_date_pub,
            # items['audiences'] =  art_audience,
            #items['nb_comments'] =  art_nombre_comments

            
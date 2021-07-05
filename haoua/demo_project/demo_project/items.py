# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    categorie=scrapy.Field()
    url=scrapy.Field()
    titre=scrapy.Field()
    texte=scrapy.Field()
    publication=scrapy.Field()
    auteur=scrapy.Field()
    vue=scrapy.Field()
    #tous_commentaire=scrapy.Field()
    #datepub=scrapy.Field()
    #audiences=scrapy.Field()
    #nb_comments=scrapy.Field()
    pass

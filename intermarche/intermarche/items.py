# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MagasinItem(scrapy.Item):
	"""Item Magasin"""
	id = scrapy.Field()
	nom = scrapy.Field()
	adresse = scrapy.Field()
	tel = scrapy.Field()
	mail = scrapy.Field()
	url_info = scrapy.Field()
	url_drive = scrapy.Field()
	ville = scrapy.Field()
	cp = scrapy.Field()
	latitude = scrapy.Field()
	longitude = scrapy.Field()

class CategoryItem(scrapy.Item):
	"""Item Categorie"""
	id = scrapy.Field()
	magasin_id = scrapy.Field()
	rayon = scrapy.Field()
	sous_rayon = scrapy.Field()
	categorie =  scrapy.Field()
	categorie_id = scrapy.Field()
	categorie_url = scrapy.Field()
	feuille = scrapy.Field()

class ProductItem(scrapy.Item):
	"""Item Produit"""
	id = scrapy.Field()
	nom = scrapy.Field()
	prix = scrapy.Field()
	prix_barre = scrapy.Field()
	promo = scrapy.Field()

class ProductInfoItem(scrapy.Item):
	"""Item Info Produit"""
	id = scrapy.Field()
	nom = scrapy.Field()
	marque = scrapy.Field()
	url = scrapy.Field()
	url_image = scrapy.Field()
	quantite = scrapy.Field()
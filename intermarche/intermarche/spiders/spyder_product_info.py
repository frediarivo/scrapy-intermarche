import scrapy
import json
from ..items import ProductInfoItem

class SpiderProductInfo(scrapy.Spider):
	""" Récupération de la liste des fiches produits d'un magasin """
	name = "spider_product_info"
	allowed_domains = ['https://drive.intermarche.com', 'drive.intermarche.com']

	def start_requests(self):
		urls = [
			'https://drive.intermarche.com/153-mitry-mory',
		]

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		"""Iterate each url"""
		ulrs_driver = []

		# Extracter les urls drives
		for sel in response.xpath("//ul/li/a"):
			h = sel.xpath("@href").extract()
			v = '/153-mitry-mory'
			if len(h)>0:
				if v in h[0]:
					url = self.allowed_domains[0] + '/' + h[0]
					ulrs_driver.append(url)
		
		# Nettoyer la liste des drives (présence des doublons)
		ulrs_driver = list(dict.fromkeys(ulrs_driver))

		for url_drive in ulrs_driver:
			yield scrapy.Request(url_drive, callback=self.parse_item)

	def parse_item(self, response):
		"""Extract all items from url"""
		items = []
		for sel in response.xpath("//li[contains(@class,'vignette_produit_info js-vignette_produit')]/div"):
			info = sel.xpath("div[contains(@class, 'vignette_info')]/p/text()").extract()
			
			url = sel.xpath("div[contains(@class, 'vignette_footer js-vignette_footer js-vignette_produit_info')]/@idproduit").extract()
						
			url_image = sel.xpath("div[contains(@class, 'vignette_img transition')]/img/@src").extract()
			quantite = sel.xpath("div[contains(@class, 'vignette_info')]/div/span/text()").extract()

			if len(info) == 2:
				item = ProductInfoItem()
				self.counter_id += 1

				item['id'] = ""
				item['nom'] = info[1].strip()
				item['marque'] = info[0].strip()
				item['url'] = self.allowed_domains[0] + '/FicheProduit?idProduit=' + url[0]
				item['url_image'] = url_image[0]
				item['quantite'] = quantite[0]

				yield item

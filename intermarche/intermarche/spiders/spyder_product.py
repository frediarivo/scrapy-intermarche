import scrapy
from scrapy import Request
from ..items import ProductItem

class SpiderProduct(scrapy.Spider):
	""" Récupération de la liste des produits d'un magasin """
	name = "spider_product"
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
		"""Extraire les urls de drive du magasin"""
		for sel in response.xpath("//li[contains(@class,'vignette_produit_info js-vignette_produit')]/div"):
			info = sel.xpath("div[contains(@class, 'vignette_info')]/p/text()").extract()
			prix = sel.xpath("div[contains(@class, 'vignette_picto_prix')]/div/p/text()").extract()
			prix_promo = sel.xpath("div[contains(@class, 'vignette_picto_prix')]/div//p[contains(@class, 'red-text')]/text()").extract()
			prix_barre = sel.xpath("div[contains(@class, 'vignette_picto_prix')]/div/del/text()").extract()
						
			if len(info) == 2:
				item = ProductItem()
				self.counter_id += 1

				item['id'] = ""
				item['nom'] = info[1].strip()
				item['prix'] = prix[0]
				
				if len(prix_barre) == 1:
					item['prix_barre'] = prix_barre[0]
				else:
					item['prix_barre'] = "0"

				if len(prix_promo) == 1:
					item['promo'] = str(True)
				else:
					item['promo'] = str(False)

				yield item

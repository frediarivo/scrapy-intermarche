import scrapy
import json
from ..items import MagasinItem

class SpiderMagasin(scrapy.Spider):
	""" Récupération de la lsite des magasins"""
	name = "spider_magasin"
	url_base = 'https://drive.intermarche.com'
	counter_id = 0
	
	def start_requests(self):
		urls = [
			'https://drive.intermarche.com/magasins/',
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		items = []
		
		for sel in response.xpath("//div[contains(@id,'listeDepartements')]/*//a"):
			url_info = self.url_base + sel.xpath("@href").extract()[0]
			if len(url_info.split('/')) == 6:
				item = MagasinItem()
				self.counter_id += 1

				id = str(self.counter_id)
				nom = sel.xpath("text()").extract()[0]
				url_info = url_info
				url_drive = self.url_base + '/' + url_info.split('/')[5]
				ville = sel.xpath("text()").extract()[0].split('(')[0].strip()
				cp = sel.xpath("text()").extract()[0].split('(')[1].strip()[0:-1]
				
				yield scrapy.Request(url_info, callback=self.parse_info, meta={'item': {
					'id': id,
					'nom': nom,
					'url_info': url_info,
					'url_drive': url_drive,
					'ville': ville,
					'cp': cp,
				}})

	def parse_info(self, response):
		item = response.meta['item']
		
		item['tel'] = response.xpath("//p[contains(@class,'tel')]/span/text()").extract_first()
		item['adresse'] = response.xpath("//p[contains(@class,'adresse_info')]/text()").extract_first().strip()
		item['mail'] = self.url_base + response.xpath("//p[contains(@class,'contact_fiche underline cursor')]/a/@href").extract_first()
		map_url = response.xpath("//a[contains(@style,'position: static; overflow: visible; float: none; display: inline;')]/@href").extract_first()
		item['latitude'] = "0"
		item['longiturde'] = "0"

		return item
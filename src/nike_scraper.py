from scraper import Base

import time
import json 

class NikeScraper(Base):
	products = []

	def __init__(self, target):
		self.target = target

	def __get_product_name(self):
		section = self.soup.find(class_='header-pdp-body__detail--desc')
		return section.get_text()

	def __get_product_price(self):
		price = self.soup.find(class_='valor-normal js-valor-normal')
		return price.get_text()

	def __get_photos(self):
		carrousel = self.soup.find(class_='easyzoom easyzoom--adjacent easyzoom--with-thumbnails row')
		imgs = carrousel.find_all('a')

		photos = []

		for index, img in enumerate(imgs):
			photos.append({ 
				"order": index, 
				"url": img['data-standard'] 
			})
		
		return photos
	
	def __add_product(self):
		product = { 
			"name": self.__get_product_name(), 
			"photos": self.__get_photos(),
			"price": self.__get_product_price()
		}

		self.products.append(product)
	
	def scrape(self, delay):
		for path in self.target['paths']:
			response_html = self.target['http_client'].get(
				path=path, 
				headers={
					"user-agent": 'insomnia/2022.2.1',
					"accept": '*/*'
				}
			)
			
			self.set_html(response_html)
			self.__add_product()

			time.sleep(delay)

	def data(self):
		return json.dumps(self.products, indent = 2)
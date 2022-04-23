from scraper import Base

import time
import json 

class NetshoesScraper(Base):
	products = []

	def __init__(self, target):
		self.target = target

	def __get_product_name(self):
		section = self.soup.find(class_='short-description')
		h1 = section.find('h1')
		return h1.get_text()

	def __get_product_price(self):
		price = self.soup.find(class_='default-price')
		return price.get_text()

	def __get_photos(self):
		ul = self.soup.find(class_='swiper-wrapper')
		imgs = ul.find_all('img')

		photos = []

		for index, img in enumerate(imgs):
			photos.append({ 
				"order": index, 
				"url": img['data-src-large'] 
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
					"User-agent": "Mediapartners-Google"
				}
			)
			
			self.set_html(response_html)
			self.__add_product()

			time.sleep(delay)

	def data(self):
		return json.dumps(self.products, indent = 2)
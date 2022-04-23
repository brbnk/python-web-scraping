from bs4 import BeautifulSoup

class Base:
	bs = BeautifulSoup

	def __make_soup(self, html):
		self.soup = self.bs(html, 'html.parser')

	def set_html(self, html):
		self.__make_soup(html)

	def html(self):
		print(self.soup)
#!/usr/local/bin/python3

from http_client      import HttpClient
from netshoes_scraper import NetshoesScraper
from nike_scraper import NikeScraper
import json

def main():
	targets = [
		{
			'http_client': HttpClient('https://www.nike.com.br'),
			'paths': [
				'/tenis-nike-dunk-high-se-masculino-153-169-223-345339'
			],
			'scraper': {
				'agent': NikeScraper,
				'delay': 3
			}
		},
		{
			'http_client': HttpClient('https://www.netshoes.com.br'),
			'paths': [
				'/EUZ-1193-111'
			],
			'scraper': {
				'agent': NetshoesScraper,
				'delay': 3
			}
		}
	]

	for target in targets:  
		ns = target['scraper']['agent'](target)

		ns.scrape(delay = target['scraper']['delay'])

		data = ns.data()

		print(data)
    
if __name__ == '__main__':
	main()
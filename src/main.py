#!/usr/local/bin/python3

from http_client      import HttpClient
from netshoes_scraper import NetshoesScraper

def main():
    httpClient = HttpClient()

    target = {
        'http_client': httpClient.set_baseurl('https://www.netshoes.com.br'),
        'paths': [
            '/EUZ-1193-111',
            '/EUZ-1193-066',
            '/EUZ-1182-274',
            '/EUZ-6876-026',
            '/2IC-5987-006',
            '/HZM-4644-890',
            '/D29-8232-081',
            '/311-3129-218',
            '/HZM-5209-026'
        ]
    }

    ns = NetshoesScraper(target)
    ns.scrape(delay=3)
    data = ns.data()
    
if __name__ == '__main__':
    main()
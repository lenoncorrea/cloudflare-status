#!/home/lenon/cloudflare-status/venv/bin/python

#--------------------------------------------------------------------
# file:         cloudflare.py
# comment:      Coletar informacoes dos status da cloudflare
# author:       Lenon Corrêa <lenonac_@hotmail.com>
# date:         27-08-2020
# Last updated: 27-08-2020
#--------------------------------------------------------------------


from lxml import html
# import requests
# import re
# import sys
import cloudscraper

# def convertTuple(tup):
#     str =  ''.join(tup)
#     return str

# if len(sys.argv) < 2:
#     print("erro, informe o site a ser testado\n")
#     sys.exit(1)
# site = sys.argv[1]

baseUrl = 'https://www.cloudflarestatus.com/'

scraper = cloudscraper.create_scraper()
page = scraper.get(baseUrl)

# print(page)


# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
# headers = {'User-Agent': user_agent}
# page = requests.get(url,headers=headers)
# page = requests.get(url)
# print(response)
if page.status_code != 200:
    # print('Erro: '+page.status_code)
    print("0")
    sys.exit(1)
locale = 'Porto Alegre, Brazil - (POA)'
tree = html.fromstring(page.content)
cities = tree.xpath('//span[contains(text(), "{}")]/text()'.format(locale))
# print(status)

for city in cities:
  # if (x == 'Porto Alegre, Brazil - (POA)'):
  print(city)
  # status = tree.xpath('//span[contains(text(), "{}")]/text()'.format(locale))
  # status = tree.xpath('//span[@class="component-status "]/text()')
  status = tree.xpath('//span[contains(text(), "{}")]///span[@class="component-status "]/text()'.format(locale))
  print(status)

# for x in range(len(status)):
    # data = status[x]
    # print(data)
    # if (data == 'Porto Alegre, Brazil - (POA)'):
    #   print(data)
#     teste = re.compile(".*status: '(.*)',.*", re.MULTILINE)
#     for match in teste.finditer(data):
#         status = match.groups()
#         status = convertTuple(status)
#         # print(status)
#   	    #Conventendo String para Valor numerico
#         if(status == 'success'):
#             status = 10
#         if(status == 'warning'):
#             status = 20
#         if(status == 'danger'):
#             status = 30
#         print(status)
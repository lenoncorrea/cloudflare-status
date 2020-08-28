#!/home/lenon/cloudflare-status/venv/bin/python

#--------------------------------------------------------------------
# file:         cloudflare.py
# comment:      Coletar informacoes dos status da cloudflare
# author:       Lenon Corrêa <lenonac_@hotmail.com>
# date:         27-08-2020
# Last updated: 27-08-2020
#--------------------------------------------------------------------

import requests
import json
import sys
from cachetools import TTLCache

# def convertTuple(tup):
#     str =  ''.join(tup)
#     return str

class Cloudflare:
    def __init__(self):
        self.baseUrl = 'https://yh6f0r4529hb.statuspage.io/api/v2/summary.json'
        
# if len(sys.argv) < 2:
#     print("erro, informe o site a ser testado\n")
#     sys.exit(1)
# site = sys.argv[1]

    def requesting(self):
        response = requests.get(self.baseUrl)
        result = response.text.encode('utf8')
        results = json.loads(result)
        return results

    def params(self,results):
        for data in results:
            data = results['components']
            for component in range(len(data)):
                print(data[component]['id'])
            # for ids in component:
                # if component['id']
                # print(component['id'])
                # city = component[city]
            #     return city
            #     # if (component == '7k05x28lndzb'):
                #     print(id)
            # version = results['0']
            # return city
    
    def city(self,argument):
        cities = {"data": [{"city": "POA", "id": "7k05x28lndzb"}, {"city": "FOR", "id": "2fy0n0pw01nm"}]}
        for data in cities:
            for city in cities['data']:
                if argument == city['city']:
                    # self.city = city['id']
                    return self.city
    
    def check_cache(self):
        if self.city:
            results = self.requesting()
            data = self.params(results)
            # return results
        else:
            return self.city
        
def main(argument):
    cloud = Cloudflare()
    cache = cloud.check_cache()
    # result = cloud.city(cache)
    # else:
        # pass
        # print(data)

if __name__ == '__main__':
  argument = sys.argv[1]
  result = main(argument)

# user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
# headers = {'User-Agent': user_agent}
# page = requests.get(url,headers=headers)
# page = requests.get(url)
# print(response)
# if page.status_code != 200:
#     # print('Erro: '+page.status_code)
#     print("0")
#     sys.exit(1)
  
# doc = html.fromstring(page.content)

# for locale in locales:
#   city = tree.xpath('//span[contains(text(), "{}")]/text()'.format(locale))
#   status = tree.xpath('//span[@class="component-status "]/text()')
#   print(status)

# var = next (city for city in cities if cities(city))
# print(var)

# for city in cities:
  # if (x == 'Porto Alegre, Brazil - (POA)'):
  # print(city)
  # status = tree.xpath('//span[contains(text(), "{}")]/text()'.format(locale))
  # status = tree.xpath('//span[@class="component-status "]/text()')
  # status = tree.xpath('//span[contains(text(), "{}")]///span[@class="component-status "]/text()'.format(locale))
  # print(status)

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
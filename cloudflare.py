#!/usr/lib/zabbix/externalscripts/cloudflare-status/venv/bin/python

#--------------------------------------------------------------------
# file:         cloudflare.py
# comment:      Coletar informacoes dos status da cloudflare
# author:       Lenon Corrêa <lenonac_@hotmail.com>
# date:         27-08-2020
# Last updated: 28-08-2020 16:10:00
#--------------------------------------------------------------------

import requests
import json
import sys

class Cloudflare:
    def __init__(self):
        self.baseUrl = 'https://yh6f0r4529hb.statuspage.io/api/v2/summary.json'

    def requesting(self):
        response = requests.get(self.baseUrl)
        result = response.text.encode('utf8')
        results = json.loads(result)
        return results
    
    def check_status(self,results,argument):
        for data in results:
            data = results['components']
            for component in range(len(data)):
                city_name = data[component]['name']
                if city_name == argument:
                    city_status = data[component]['status']
                    return city_status
    
    def convert_to_str(self,status):
        if status == 'operational':
            status = 10
        if status == 'Re-routed':
            status = 20
        if(status == 'degraded_performance'):
            status = 30
        print(status)

def main(argument):
    cloud = Cloudflare()
    request = cloud.requesting()
    status = cloud.check_status(request,argument)
    status = cloud.convert_to_str(status)
    
if __name__ == '__main__':
  argument = sys.argv[1]
  result = main(argument)

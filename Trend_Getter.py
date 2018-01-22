# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 22:14:33 2018

@author: Ureridu
"""

import requests
import pandas
import json




token_url_start = 'https://trends.google.com/trends/api/explore?hl=en-US&tz=300&req=%7B%22comparisonItem%22:%5B%7B%22keyword%22:%22'
token_url_mid1 = '%22,%22geo%22:%22'
token_url_mid2 = '%22,%22time%22:%22today+'
token_url_mid3 = '-m%22%7D%5D,%22category%22:0,%22property%22:%22%22%7D&tz=300'

search ='ethereium'
location = ''
length = '3'

'''
token_url = 'https://trends.google.com/trends/api/explore?hl=en-US&tz=300&req=%7B%22comparisonItem%22:%5B%7B%22keyword%22:%22whoo%22,%22geo%22:%22%22,%22time%22:%22today+3-m%22%7D%5D,%22category%22:0,%22property%22:%22%22%7D&tz=300'
token_url = 'https://trends.google.com/trends/api/explore?hl=en-US&tz=300&req=%7B%22comparisonItem%22:%5B%7B%22keyword%22:%22whoo%22,%22geo%22:%22US%22,%22time%22:%22today+3-m%22%7D%5D,%22category%22:0,%22property%22:%22%22%7D&tz=300'
token_url = 'https://trends.google.com/trends/api/explore?hl=en-US&tz=300&req=%7B%22comparisonItem%22:%5B%7B%22keyword%22:%22whoo%22,%22geo%22:%22%22,%22time%22:%22today+3-m%22%7D,%7B%22keyword%22:%22what%22,%22geo%22:%22%22,%22time%22:%22today+3-m%22%7D%5D,
%22category%22:0,%22property%22:%22%22%7D&tz=300'
'''

url = token_url_start + search + token_url_mid1 + location + token_url_mid2 + length + token_url_mid3


token_request = requests.get(url)
token_json = json.loads(token_request.text[4:])
req = token_json['widgets'][0]
token=req['token']



payload = {
            'hl': 'en-US',
            'tz': '300',
            'req': '{"time":"2017-10-22 2018-01-22","resolution":"DAY","locale":"en-US","comparisonItem":[{"geo":{"country":"US"},"complexKeywordsRestriction":{"keyword":[{"type":"BROAD","value":"whoo"}]}}],"requestOptions":{"property":"","backend":"IZG","category":0}}',
            'token': 'APP6_UEAAAAAWmaqKmWtY85_NerN-UCk_Bw7IreNLeQl',
            'tz': '300',
            }
#payload['req']=payload['req'].replace('"', '\\"')
url = 'https://trends.google.com/trends/api/widgetdata/multiline'

data = requests.get(url, params = payload)
data = json.loads(data.text[6:])

'https://trends.google.com/trends/api/widgetdata/multiline?hl=en-US&tz=300&req=%7B%22time%22:%222017-10-22+2018-01-22%22,%22resolution%22:%22DAY%22,%22locale%22:%22en-US%22,%22comparisonItem%22:%5B%7B%22geo%22:%7B%22country%22:%22US%22%7D,%22complexKeywordsRestriction%22:%7B%22keyword%22:%5B%7B%22type%22:%22BROAD%22,%22value%22:%22whoo%22%7D%5D%7D%7D%5D,%22requestOptions%22:%7B%22property%22:%22%22,%22backend%22:%22IZG%22,%22category%22:0%7D%7D&token=APP6_UEAAAAAWmaqKmWtY85_NerN-UCk_Bw7IreNLeQl&tz=300'
'https://trends.google.com/trends/api/widgetdata/multiline?hl=en-US&tz=300&req=%7B%5C%22time%5C%22%3A%5C%222017-10-22+2018-01-22%5C%22%2C%5C%22resolution%5C%22%3A%5C%22DAY%5C%22%2C%5C%22locale%5C%22%3A%5C%22en-US%5C%22%2C%5C%22comparisonItem%5C%22%3A%5B%7B%5C%22geo%5C%22%3A%7B%5C%22country%5C%22%3A%5C%22US%5C%22%7D%2C%5C%22complexKeywordsRestriction%5C%22%3A%7B%5C%22keyword%5C%22%3A%5B%7B%5C%22type%5C%22%3A%5C%22BROAD%5C%22%2C%5C%22value%5C%22%3A%5C%22whoo%5C%22%7D%5D%7D%7D%5D%2C%5C%22requestOptions%5C%22%3A%7B%5C%22property%5C%22%3A%5C%22%5C%22%2C%5C%22backend%5C%22%3A%5C%22IZG%5C%22%2C%5C%22category%5C%22%3A0%7'

#u = data.url.replace(')



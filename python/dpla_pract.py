# https://nbviewer.jupyter.org/github/humanitiesprogramming/humanitiesprogramming.github.io/blob/master/python/notebooks/working-with-apis.ipynb
# installed DPLA wrapper on terminal
from dpla.api import DPLA
import os
# gave credential and requested API key (curl -v -XPOST...)
# exported API key on terminal, named 'API_KEY'
my_api_key = os.getenv('API_KEY')
dpla_connection = DPLA(my_api_key)

# retrieving data related to 'Austen'
#result = dpla_connection.search('austen')
#print(type(result))
#print(str(result.__dict__)[:1000])
#item = result.items[0]
#print(item)
#print(item['sourceResource']['stateLocatedIn'])
#print(result.items[0]['sourceResource'])
#print(item.keys())
#for item in result.items[:9]:
#    print(item['sourceResource']['stateLocatedIn'])
# error related to stateLocatedIn, troubleshooting-
#print(result.items[4]['sourceResource'])
# structuring data to include electronic resources (no stateLocatedIn field)
# for item in result.items[:9]:
#     if 'stateLocatedIn' in item['sourceResource']:
#         print(item['sourceResource']['stateLocatedIn'])
#     else:
#         print(item['sourceResource']['format'])

# retrieving data related to Austin, TX
import requests
endpoint = 'https://api.dp.la/v2/items'
params = {
    'api_key': my_api_key,
    'q': 'Austin, Texas'
}
requested_the_hard_way = requests.get(endpoint, params)
#requested_the_hard_way.status_code
#requested_the_hard_way.url
#print(requested_the_hard_way.json()['count'])
#print(requested_the_hard_way.json()['docs'][0])

# counting results?
import math

total_hard_way_results = []
params = {
    'api_key': my_api_key,
    'q': 'Austin, Texas',
    'page_size': '500'
}
total_results = requested_the_hard_way.json()['count']
number_of_pages = math.ceil(total_results / 500)
#print(number_of_pages)
list_of_page_numbers = range(1, 21, 1)
for page_number in list_of_page_numbers:
#    print(page_number)
    params['page'] = page_number
    for result in requests.get(endpoint, params) .json() ['docs']:
        total_hard_way_results.append(result)
#
# print(len(total_hard_way_results))

state_results = {}
state_results['other_format'] = 0
for item in total_hard_way_results:
    if 'stateLocatedIn' in item['sourceResource']:
        if item['sourceResource']['stateLocatedIn'][0]['name'] in state_results:
            state_results[item['sourceResource']['stateLocatedIn'][0]['name']] += 1
        else:
            state_results[item['sourceResource']['stateLocatedIn'][0]['name']] = 1
    elif 'format' in item['sourceResource'] and item['sourceResource']['format'] != 'Text':
        state_results['other_format'] += 1
    else:
        pass
print(state_results)

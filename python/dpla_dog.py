# 1. Write your own script to use the DPLA API for a search item using the Python wrapper.
# Let's find a dog-related item! We'll dig through the JSON to find out the URL for the original item.


from dpla.api import DPLA
import os
my_api_key = os.getenv('API_KEY')
dpla_connection = DPLA(my_api_key)
result = dpla_connection.search('dogs')
item = result.items[0]
print(item)
# item['@id']
#print(item['originalRecord']['metadata']['mods:mods']['mods:identifier'][1]['#text'])

from ipdata import ipdata
from pprint import pprint
import json


ipd=ipdata.IPData('94e7d24a7610566ca951ae281d974d19d7be21764420af641f2f6d0a')


ips = ['69.78.70.144', '8.8.8.8']
locators = ['country_name', 'threat']

dict = {}
for ip in ips:
	response = ipd.lookup(ip)
	#for locator in locators:
	#	print(ip, response[locator])
	#print("\n")
	dict[ip] = {}
	for locator in locators:
		dict[ip][locator] = response[locator]

#print(dict)
jsonobj = json.dumps(dict)
print(jsonobj)

	

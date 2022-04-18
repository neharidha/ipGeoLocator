from ipdata import ipdata
from pprint import pprint
ipd=ipdata.IPData('94e7d24a7610566ca951ae281d974d19d7be21764420af641f2f6d0a')
response = ipd.lookup('69.78.70.144')
pprint(response)

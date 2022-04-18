import os
import json
import datetime


dict = {'neha' : 'firl', 'sam':'boy'}
filename="result"+str(datetime.datetime.now()) +".json"
with open(filename, 'w') as fp:
	json.dump(dict, fp)

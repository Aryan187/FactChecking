import json
import random

all_data = open('full_cleaned.json')
data = json.load(all_data)

sample_data = open('random_all.json')
sample = json.load(sample_data)

rand_clean = {}
for k in sample:
	rand_clean[k] = data[k]
out_json = json.dumps(rand_clean,indent=1)

with open('random_cleaned.json',"w") as out:
	out.write(out_json)
import json
import random

all_data = open('full_cleaned.json')
data = json.load(all_data)

sample_data = open('football_all.json')
sample = json.load(sample_data)

football_clean = {}
for k in sample:
	football_clean[k] = data[k]
out_json = json.dumps(football_clean,indent=1)

with open('football_cleaned.json',"w") as out:
	out.write(out_json)
import json
import random

all_tables = open('all_csv_ids.json')
data = json.load(all_tables)

rand = random.sample(list(data),1000)
out_json = json.dumps(rand,indent=1)

with open('random_all.json',"w") as out:
	out.write(out_json)
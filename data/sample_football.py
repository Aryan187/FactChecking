import json
import random

def search(values, searchFor):
	new_data = {}
	for k in values:
		for v in values[k]:
			if searchFor in v.lower():
				new_data[k] = v
	return new_data

all_tables = open('table_to_page.json')
data = json.load(all_tables)

selected_data = search(data,'football')
selected_data.update(search(data,'f.c.'))
selected_data.update(search(data,'fa cup'))

out_json = json.dumps(list(selected_data),indent=1)

with open('football_all.json',"w") as out:
	out.write(out_json)

print(len(selected_data))
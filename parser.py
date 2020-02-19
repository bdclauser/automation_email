#!/usr/bin/env python3

import json
import csv
import re


def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


with open('/Users/brianclauser/asana_tasks/asana2go_output_json_complete.json') as f:
    data = json.load(f)

results = []
for items in data['tasks']:
    data_html = items["html_notes"]
    if isinstance(data, list) and len(data) > 1:
        results.append(int(data[2]['content']))

for items in data['tasks']:
    data_url = items['url']
    if isinstance(data, list) and len(data) > 1:
        results.append(int(data[1]['url']))

for items in data['tasks']:
    data_name = items['name']
    if isinstance(data, list) and len(data) > 1:
        results.append(int(data[0]['content']))

results = [data_name, data_url, remove_html_tags(data_html)]

with open('out.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile, delimiter=' ',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(results)

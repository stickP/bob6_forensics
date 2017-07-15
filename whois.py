#!/usr/bin/python
import pythonwhois
import json
import datetime

def json_fallback(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    else:
        return obj

domain = []

f = open("domain", 'r')
domain = f.read().splitlines()
f.close()

data = []

for d in domain:
    output = pythonwhois.net.get_whois_raw(d, with_server_list=False)
    parse_output = pythonwhois.parse.parse_raw_whois(output, normalized=True)
    data.append(parse_output)

res = open("whois.json", 'w')

for i in range(0, len(data)):
    res.write(json.dumps(data[i], default=json_fallback))

res.close()

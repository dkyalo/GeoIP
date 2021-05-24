import requests
import os
import json


apikey = ''

apiurl = 'https://api.ipfind.com/?ip={ip}&auth={apikey}'


with open('ip.txt','r') as ipfile:
    with open('out.json', 'a') as outfile:
        for i in ipfile.readlines():
            print(i.strip('\t\n'))
            r = requests.get(apiurl.format(ip=i, apikey=apikey))
            l = r.json()
            print(l)
            outfile.write(json.dumps(l))
            outfile.write(',\n')

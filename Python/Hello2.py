#!/usr/bin/env python3
import socket
import time
import json
import yaml

host1 = 'drive.google.com'
host2 = 'mail.google.com'
host3 = 'google.com'

DNS = {'servers':[{host1 : socket.gethostbyname(host1), host2 : socket.gethostbyname(host2), host3 : socket.gethostbyname(host3)}]}
print (DNS['servers'][0][host2])
for key in DNS['servers'][0]:
        print ('<',key,'>','-','<',DNS['servers'][0][key],'>')
        ip = socket.gethostbyname(key)
#        with open('2.json', 'w') as js:
#            js.write(json.dumps(DNS, indent=2))


with open('2.yaml', 'w') as ym:
    ym.write(yaml.dump(DNS, default_flow_style=False))










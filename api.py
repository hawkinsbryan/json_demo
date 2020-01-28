import json
from urllib.request import urlopen

with urlopen("http://time.jsontest.com/") as response:
    source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))

# for item in data['list']['resources']:
#     print item

print(data['time'])
import json
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_357340.json'
data = urllib.request.urlopen(url).read().decode('utf-8')

info = json.loads(data)
tot = 0

for comment in info['comments']:
   tot = tot + int(comment['count'])

print(tot)

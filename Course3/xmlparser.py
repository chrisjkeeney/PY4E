import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


url = 'http://py4e-data.dr-chuck.net/comments_357339.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

uh = urllib.request.urlopen(url)

data = uh.read()
tree = ET.fromstring(data)
results = tree.findall('.//count')

tot = 0

for count in results:
    tot = int(count.text) + tot

print(tot)

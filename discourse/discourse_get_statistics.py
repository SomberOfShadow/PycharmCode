import requests
from requests.auth import HTTPBasicAuth

url = "https://discourse.lmera.ericsson.se/u"
res = requests.get(url, auth=HTTPBasicAuth('EENHENI', 'Shadow&&19921211'))

print(res.text)
import requests
import json


URL = "http://127.0.0.1:8000/drinkcreate/"
data = {
'name': 'Whiskey',
'description': 'Hello',
# 'price': 1000
}
json_data = json.dumps(data)
r = requests.post(url=URL, json=data)
data == r.json()
print(data)
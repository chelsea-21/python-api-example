from http.client import responses

import requests

# http://127.0.0.1:5000 is a local endpoint
# base_url = 'http://localhost:5000/uppercase'
# base_url = 'http://127.0.0.1:5000/uppercase'
base_url = 'http://127.0.0.1:5000/transform'

params = {'text': 'ThIS IS my dog ', 'duplication_factor': '3', 'capitalization': 'LOWER'}

response = requests.get(base_url, params=params)

print(response.json())
print(f'Status Code: {response.status_code}')

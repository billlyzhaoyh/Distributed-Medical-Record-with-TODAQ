#the file is passed back to Alice and now need to parse the record altogether 

#check if Alice has the record if no prompt her to ask doctor to return the record


import requests
import json

payload = 0
url = 'https://api.todaqfinance.net/accounts/18be8d85-99aa-40d8-8653-8d1a74a2675c/transactions?page=1&limit=100'
headers = {
  'Content-Type': 'application/json',
  'x-api-key': '82572e09-1a47-40e4-a018-22b6daa4e53f'
}
response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
a=response.json()
b=json.loads(str(a))
print(a)



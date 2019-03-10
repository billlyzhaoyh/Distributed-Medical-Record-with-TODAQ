import requests,json

url = 'https://api.todaqfinance.net/transactions'

python_payload={u'data': {u'attributes':{u'metadata': {u'date': 10000}},u'relationships': {u'files': {u'data': [{u'type': u'file', u'id': u'95acb980ce31be3cfc1d6f2bd07447faef6854451c846383de0806063d11752c'}]},
u'recipient': {u'data': {u'type': u'account', u'id': u'18be8d85-99aa-40d8-8653-8d1a74a2675c'}}, u'sender': {u'data': {u'type': u'account',
u'id': u'ad29f480-ae85-4e69-b84d-fcf74c63e9ff'}}}}}

payload = json.dumps(python_payload)

headers = {
  'Content-Type': 'application/json',
  'x-api-key': '82572e09-1a47-40e4-a018-22b6daa4e53f'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)

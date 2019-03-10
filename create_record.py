import requests
url = 'https://api.todaqfinance.net/files'
payload = "{\n    \"data\": {\n    \t\"type\":\"file\",\n    \t\"attributes\":{\n    \t\t\"payload\":{ \n    \t\t\t\"id\": \"1a3c1e04-ab62-4c44-b4a3-873f5d50c07d\",\n\t\t\t\t \"type\": \"loyalty-token\",\n\t\t\t\t \"member-type\": \"gold\"\n    \t\t}\n    \t},\n    \t\"relationships\":{\n    \t\t\"initial-account\":{\n    \t\t\t\"data\":{\n\t    \t\t\t\"type\":\"account\",\n    \t\t\t\t\"id\":\"ad29f480-ae85-4e69-b84d-fcf74c63e9ff\"\n    \t\t\t}\n    \t\t},\n    \t\t\"file-type\": {\n    \t\t\t\"data\": {\n    \t\t\t\t\"id\": \"ddbb8d2fa80f5eeb2c9071026038557571d65db62ba1d32a974c7932dc4a5fa2\"\n    \t\t\t}\n    \t\t}\n    \t}\n    }\n}"
headers = {
  'Content-Type': 'application/json',
  'x-api-key': '82572e09-1a47-40e4-a018-22b6daa4e53f'
}
response = requests.request('POST', url, headers = headers, data = payload, allow_redirects=False)
print(response.text)

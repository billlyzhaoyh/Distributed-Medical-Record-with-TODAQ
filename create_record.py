import requests
url = 'https://api.todaqfinance.net/files'
payload = "{\n\t\"type\": \"account\",\n    \"data\": {\n    \t\"attributes\": {\n\t\t\t\"account-type\": \"individual\",\n\t\t\t\"admin-email\": \"patricia@example.com\",\n\t\t\t\"contact\": {\n\t\t\t   \"email\": \"patricia@example.com\",\n\t\t\t   \"phone\": \"555-555-5323\",\n\t\t\t   \"last-name\": \"Trie\",\n\t\t\t   \"first-name\": \"Patricia\",\n\t\t\t   \"address\": {\n\t\t   \t\t\t\"city\": \"Toronto\",\n\t\t             \"postal-code\": \"N4N2L1\",\n\t\t             \"province-region\": \"Ontario\",\n\t\t             \"street-address-1\": \"925 Madison Avenue\",\n\t\t             \"country\": \"CA\"\n\t\t\t   }\n\t   \t\t}\n\t\t}\n    }\n}"
headers = {
  'Content-Type': 'application/json',
  'x-api-key': '82572e09-1a47-40e4-a018-22b6daa4e53f'
}
response = requests.post(url, headers = headers, data = payload, allow_redirects = False)
print(response.text)

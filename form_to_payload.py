import json

payload = "{\n\t\"data\": {\n    \t\"relationships\":{\n    \t\t\"sender\":{\n    \t\t\t\"data\": {\n\t    \t\t\t\"type\":\"account\",\n    \t\t\t\t\"id\":\"28cd9275-fcdc-4611-9203-7c64621b9efe\"\n    \t\t\t}\n    \t\t},\n    \t\t\"recipient\":{\n    \t\t\t\"data\": {\n\t    \t\t\t\"type\":\"account\",\n    \t\t\t\t\"id\":\"0c39911e-f73a-45d7-b120-b5929a5f3385\"\n    \t\t\t}\n    \t\t},\n    \t\t\"files\":{\n    \t\t\t\"data\":[\n    \t\t\t\t{\n    \t\t\t\t\t\"type\":\"file\",\n\t\t    \t\t\t\"id\":\"7426a353a1908c70d049797ce93ee97821b94233aef9b758ef9600e9aaa520c5\"\n    \t\t\t\t}\n\t\t\t\t]\n    \t\t}\n    \t}\n    }\n}"
a=json.loads(payload)

#print(a)
python_payload={u'data': {u'relationships': {u'files': {u'data': [{u'type': u'file', u'id': u'7426a353a1908c70d049797ce93ee97821b94233aef9b758ef9600e9aaa520c5'}]}, u'recipient': {u'data': {u'type': u'account', u'id': u'0c39911e-f73a-45d7-b120-b5929a5f3385'}}, u'sender': {u'data': {u'type': u'account', u'id': u'28cd9275-fcdc-4611-9203-7c64621b9efe'}}}}}

print(json.dumps(python_payload))

#the data we get from the file: name, date, symptom, diagnosis,prescription construct them in python payload way

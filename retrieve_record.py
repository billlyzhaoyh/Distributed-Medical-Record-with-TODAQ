#the file is passed back to Alice and now need to parse the record altogether 

#check if Alice has the record if no prompt her to ask doctor to return the record

def retrieve_record(user_id):

	import requests
	import json

	payload = 0
	url_base='https://api.todaqfinance.net/accounts/'
	url_end='/transactions?page=1&limit=100'
	url = url_base+user_id+url_end
	headers = {
	  'Content-Type': 'application/json',
	  'x-api-key': '82572e09-1a47-40e4-a018-22b6daa4e53f'
	}
	response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
	a=response.json()
	number_of_entries=(len(a['data']))
	total_record=[]
	for i in range(number_of_entries):
		data_field=a['data'][i]
		record_dict=data_field['attributes']['metadata']
		total_record.append(record_dict)
	return total_record

user_id="de946eab-7f5a-4323-9867-7f1190fb1f5a"
record=retrieve_record(user_id)
print(record)
def display_drug_file (api_key,file_id_list):

	import requests
	import json

	payload = 0
	url_base='https://api.todaqfinance.net/files/'
	drug_history=[]
	for i in range(len(file_id_list)):
		url = url_base+file_id
		headers = {
		  'Content-Type': 'application/json',
		  'x-api-key': api_key
		}
		response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
		a=response.json()
		number_of_entries=(len(a['data']))
		total_record=[]
		for i in range(number_of_entries):
			data_field=a['data'][i]
			record_dict=data_field['attributes']['payload']['assignee-type']
			total_record.append(record_dict)
		drug_history.append(total_record)
	return drug_history
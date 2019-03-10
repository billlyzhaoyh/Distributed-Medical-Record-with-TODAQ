def display_drug_file (api_key,file_id_list):

	import requests
	import json

	payload = 0
	url_base='https://api.todaqfinance.net/files/'
	drug_history=[]
	for i in range(len(file_id_list)):
		url = url_base+file_id_list[i]
		headers = {
		  'Content-Type': 'application/json',
		  'x-api-key': api_key
		}
		response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False)
		a=response.json()
		total_record=[]
		data_field=a['data']
		record_dict=data_field['attributes']['payload']['assignee_type']
		total_record.append(record_dict)
		drug_history.append(total_record)
	return drug_history
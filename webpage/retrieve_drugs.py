def retrieve_drug_file(api_key,account_id,mr_id):

	import requests
	import json

	payload = 0
	
	#get all the files 
	import requests
	url_base = 'https://api.todaqfinance.net/accounts/'
	url_end ='/files?page=1&limit=100'
	url=url_base+account_id+url_end
	headers = {
  	'Content-Type': 'application/json',
  	'x-api-key': 'fd0ae52b-0866-449e-8e60-d0b12525cbbc'
	}
	response = requests.request('GET', url, headers = headers, data = payload, allow_redirects=False, timeout=undefined, allow_redirects=false)
	print(response.text)



	url_base='https://api.todaqfinance.net/files/'
	url_end='/transactions?page=1&limit=100'
	url = url_base+file_id+url_end
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
		record_dict=data_field['attributes']['metadata']
		total_record.append(record_dict)
	return total_record
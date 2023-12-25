import requests
from requests_toolbelt import MultipartEncoder
from settings import *
from wazuhApi import wazuhAPIRequest
import json
import time

wazuh = wazuhAPIRequest(wazuh_host,wazuh_host_port, wazuh_user, wazuh_password)
wazuh_agents = wazuh.get_agents()
wazuh_agents = wazuh_agents[1:]

cert = (dd_client_cert_path, dd_client_key_path)
header_end_point = {'Content-Type': 'application/json', 'Authorization': 'Token ' + dd_token }

for wazuh_agent in wazuh_agents:
	# print(wazuh_agent['ip'],wazuh_agent['id'])
	endpoint_id = 0
	get_endpoint_response = requests.get(dd_url + "endpoints/?host="+wazuh_agent['ip'],headers=header_end_point,cert=cert)
	if (len(get_endpoint_response.json()['results'])> 0):
		endpoint_id = get_endpoint_response.json()['results'][0]['id']
	else:
		endpoint_data = {
			"tags": [
			"wazuh"
			],
			"host": wazuh_agent['ip'],
			"product": 1
		}
		add_endpoint_response = requests.post(dd_url + "endpoints/",headers=header_end_point,json=endpoint_data,cert=cert)
		endpoint_id = add_endpoint_response.json()['id']
	vulnerability = wazuh.get_agentVulnerability(wazuh_agent['id'])
	json_string = json.dumps(vulnerability)
	scanData = MultipartEncoder(fields={
		'active': 'true',
		'close_old_findings': 'true',
		'engagement_name': 'wazuh',
		'push_to_jira': 'false',
		'minimum_severity': 'Info',
		'close_old_findings_product_scope': 'false',
		'create_finding_groups_for_all_findings': 'true',
		'tags': 'wazuhID-' + wazuh_agent['id'],
		'product_name': 'test',
		'service': 'wazuh-'+wazuh_agent['ip'],
		'file': ('vulns', json_string, 'text/plain'),
		'scan_type': 'Wazuh',
		'endpoint_to_add': str(endpoint_id),
		'verified': 'true'
	})
	header = {'Content-Type': scanData.content_type, 'Authorization': 'Token ' + dd_token}
	try:
		response = requests.post(dd_url+"import-scan/",headers=header,data=scanData,cert=cert)
		print(response.text)
	except:
		print("try next")
	time.sleep(3)

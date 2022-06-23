import requests
import os

a = requests.get('https://api.myip.com')
ip_data = a.json()

print(ip_data)



result_dict = {}
result_dict['success'] = True
result_dict['container'] = os.uname()[1]
result_dict['register'] = {}
result_dict['register']['ip'] = ip_data['ip']
result_dict['register']['response'] = ip_data


requests.post(
    url=os.environ['RESULTS_HOOK'],
    json=result_dict
)

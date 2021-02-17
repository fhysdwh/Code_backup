import requests
import json


url = 'https://gitee.com/lxk0301/jd_scripts/raw/master/QuantumultX/lxk0301_gallery.json'
text = requests.get(url).text
json_task_js = json.loads(text)
data = json_task_js['task']
for items in data:
    print(items)

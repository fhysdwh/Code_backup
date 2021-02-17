import requests
import json
import time

start = time.time()
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
}
id_list = []
all_datas = []
for page in range(1, 50):
    page = str(page)
    data = {
        'on': 'true',
        'page': page,
        'pageSize': '15'
    }
    get_result = requests.post(url=url, headers=headers, data=data)
    print(get_result.content)
    print(page)
    json_page = get_result.json()

    for dic in json_page['list']:
        id_list.append(dic['ID'])
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for id in id_list:
    data = {
        'id': id
    }
    content_json = requests.post(url=url, headers=headers, data=data).json()
    all_datas.append(content_json)

f = open('./all_datas.json', 'w', encoding='utf-8')
json.dump(all_datas, fp=f, ensure_ascii=False)
end = time.time()
print('爬取完成,共耗时: ' + str(round(end-start, 2)) + ' 秒')


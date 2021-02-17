import re
import requests
import os
url = 'https://w37fhy.com/sys'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
}
get_page = requests.get(url=url, headers=headers).text

re_str = '<a class="item-thumbnail" href=".*?"><img src=".*?" data-src="(.*?)" alt=.*?</a>'

img_src_list = re.findall(re_str, get_page)

if not os.path.exists('./images'):
    os.mkdir('./images')

for src in img_src_list:
    url = src
    filename = src.split('/')[-1]
    filepath = './images/' + filename
    img_data = requests.get(url=src, headers=headers).content
    with open(filepath, 'wb') as f:
        f.write(img_data)


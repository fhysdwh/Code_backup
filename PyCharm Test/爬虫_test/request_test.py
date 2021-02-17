import requests


url = 'https://w37fhy.cn/'
search_str = input('Enter Search Content:')

params = {
    's':search_str
}
response = requests.get(url=url, params=params)

page_text = response.text

filename = 'search_' + search_str + '.html'
with open(filename, 'w', encoding='utf-8') as  f:
    f.write(page_text)

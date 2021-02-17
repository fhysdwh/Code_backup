from bs4 import BeautifulSoup
import requests

# f = open('./search_github.html', 'r', encoding='utf-8')
#
# soup = BeautifulSoup(f, 'lxml')
# print(soup)

url = 'https://w37fhy.com/newinfo'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
}
get_page = requests.get(url=url, headers=headers)

soup = BeautifulSoup(get_page.text, 'lxml')

# print(soup.find_all('div'))
# aaa = soup.p
# print(aaa)
# # bbb = aaa.get_text()
# bbb = aaa.string
# print(bbb)
f = open('w37fhy.txt', 'w', encoding='utf-8')
posts_list = soup.select('.posts-item > h2 > a')
for post in posts_list:
    title = post.text
    print(title)
    detail_url = post['href']
    detail_page_text = requests.get(url=detail_url, headers=headers)
    detail_soup = BeautifulSoup(detail_page_text.text, 'lxml')
    content = detail_soup.find('div', class_='article-content').text
    print(content)
    content = title + ':' + content + '\n'
    print(content)
    f.write(content)
    print(title + '爬取完成')

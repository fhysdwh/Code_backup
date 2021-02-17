import requests
from lxml import etree

url = 'http://pic.netbian.com/4kmeinv/index_{}.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}
for i in range(2, 50):
    new_url = url.format(i)
    response = requests.get(url=new_url, headers=headers)
    get_page = response.content.decode('gbk')
    print(get_page)
    tree = etree.HTML(get_page)
    li_list = tree.xpath('//ul[@class="clearfix"]/li')
    for li in li_list:
        img_url = 'http://pic.netbian.com' + li.xpath('./a/@href')[0]
        img_page = requests.get(url=img_url, headers=headers).content.decode('gbk')
        img_tree = etree.HTML(img_page)
        img_src = img_tree.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
        img_src = 'http://pic.netbian.com' + img_src
        img_name = img_tree.xpath('//div[@class="photo-pic"]/a/img/@alt')[0] + '.jpg'
        img_data = requests.get(url=img_src, headers=headers).content
        filename = './images/'+ img_name
        with open(filename, 'wb') as f:
            f.write(img_data)
            print(img_name + ' -> 下载成功!')

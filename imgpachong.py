import requests
from fake_useragent import UserAgent
from lxml import etree


#创建URL列表
url = ['http://nianchina.net/yingshi/12168.html']
for i in range(2,66):
    url_s = 'http://nianchina.net/yingshi/12168_{}.html'.format(i)
    url.append(url_s)

#爬取数据
def faqu(url):
    print("正在爬取"+url)
    headers = {'User-Agent':UserAgent().chrome}
    response = requests.get(url,headers=headers)
    response.encoding='utf-8'
    html = etree.HTML(response.text)
    fanhao = html.xpath('//*[@id="newscontent"]/p[4]/text()')
    dizhi = html.xpath('//*[@id="newscontent"]/p[1]/img/@src')
    img = requests.get(dizhi[0].replace(" ", ""), headers=headers).content
    print('正在下载图片')
    lujing = fanhao[0]+'.jpg'
    with open(lujing, 'wb') as fp:
        fp.write(img)
    print('爬取完成')

for ur in url:
    faqu(ur)

import requests
from fake_useragent import UserAgent
from lxml import etree


#创建URL列表
shuju = []
url = ['http://nianchina.net/yingshi/12168.html']
for i in range(2,66):
    url_s = 'http://nianchina.net/yingshi/12168_{}.html'.format(i)
    url.append(url_s)

#爬取数据
def faqu(url,shuju):
    print("正在爬取"+url)
    headers = {'User-Agent':UserAgent().chrome}
    response = requests.get(url,headers=headers)
    response.encoding='utf-8'
    html = etree.HTML(response.text)
    fanhao = html.xpath('//*[@id="newscontent"]/p[4]/text()')
    shuju.append(fanhao)
    leibie = html.xpath('//*[@id="newscontent"]/p[8]/text()')
    shuju.append(leibie)
    pianming = html.xpath('//*[@id="newscontent"]/p[9]/text()')
    shuju.append(pianming)
    print('爬取完成')

for ur in url:
    faqu(ur,shuju)

#写入文件
k = 0
with open('yonglaiwei.txt','w',encoding='utf-8') as f:
    for i in shuju:
        for j in i:
            k=k+1
            f.write(j)
            f.write('\n')
            if(k%3==0):
                f.write('\n')
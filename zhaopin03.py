# -*- coding: utf-8 -*-
# 调用函数
import  requests
from lxml import etree

# 用列表存储
list=[]
#爬虫函数
def crawl(url):
    # 伪装头部 防止反爬
    headers={
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 81.0.4044.129Safari / 537.36'
    }
    # 获取网页内容
    content=requests.get(url,headers=headers)
    # 初始化函数
    tree=etree.HTML(content.text)
    # 分析网页
    title=tree.xpath('//div[@id="pane-reletive"]/div/div[@class="presentation-item"]')
    # 循环依次提取数据
    print(len(title))
    for a in title:
        # 岗位名称
        gw=a.xpath('./div[@class="fn-clear"]/div[@class="fn-left position"]/text()')

        #公司名称
        gs=a.xpath('./div[@class="fn-clear"]/div[@class="fn-right company"]/text()')
        #城市
        cs=a.xpath('./p[@class="fn-clear"]/span[@class="city fn-left"]/text()')
        #招聘人数
        rs=a.xpath('./p[@class="fn-clear"]/span[@class="num fn-left"]/text()')
        # 用字典归纳每个数据
        item={
            '岗位名称':gw,
            '公司名称':gs,
            '城市':cs,
            '招聘人数':rs

        }
#         列表存储
        list.append(item)
    return list

# 主函数
if __name__ == '__main__':
        url = 'https://xiaoyuan.zhaopin.com/search/jn=2&kw=python&pg=1'
        b=crawl(url)
        # 写入文件中
        with open(r'D:\a罗\zp.txt','w',encoding='utf-8') as f:
            f.write(str(b))


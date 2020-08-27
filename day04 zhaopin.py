# -*- coding: utf-8 -*-
import time
import  requests
from lxml import etree


#爬虫函数

def crawl(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) "
                      "Chrome/10.0.648.133 Safari/534.16"}
    # 构造请求的头信息，防止反爬虫
    contents = requests.get(url, timeout=30, headers=header).text
    tree = etree.HTML(contents)
    gzzw=tree.xpath('//ul[@class="searchResultListUl"]/li//p/a/text()')
    gsmc=tree.xpath('//p[@class="searchResultCompanyname"]/span/text()')
    gsrs=tree.xpath('//span[@class="searchResultKeyval searchResultKeyvalPeopnum"]//em/text()')
    gsdz=tree.xpath('//span[@class="searchResultKeyval"]/span/em[@class="searchResultJobCityval"]/text()')
    for j in range(len(gsrs)):
        print('正在爬取第'+str(j+1)+'个数据')
        zw=gzzw[j]
        mc=gsmc[j]
        rs=gsrs[j]
        dz=gsdz[j]
        time.sleep(0.05)
        
    time.sleep(0.1)

        # 主函数
if __name__ == '__main__':

        i=int(input('你要从第几页开始：'))
        j = int(input('你要从第几页结束：'))
        for a in range(i,j+1):
            url = 'https://xiaoyuan.zhaopin.com/full/538/0_0_160000_1_0_0_0_'+str(a)+'_0'
            crawl(url)


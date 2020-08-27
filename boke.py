# -*- coding: utf-8 -*-

import requests
import time

from bs4 import BeautifulSoup
import codecs
import  requests
import pymysql

import  codecs
# def connectMysql(zwmc,gsmc,zwyx,gzdd):
#     try:
#         conn=pymysql.connect(host='localhost',user='root',passwd='123456',port=3306,db='web8',charset="utf8")
#         cursor=conn.cursor()
#         # cursor.execute("drop table if exists douban")
#         # creat_table = "CREATE TABLE douban(zwmc varchar(255), gsmc varchar(255),zwyx varchar(255), gzdd varchar(255))"
#         # cursor.execute(creat_table)
#         sql="insert  into zhaopin(zwmc,gsmc,zwyx,gzdd) values(%s,%s,%s,%s)"
#         cursor.execute(sql % ("'"+zwmc+"'","'"+gsmc+"'","'"+zwyx+"'","'"+gzdd+"'"))
#         #cursor.execute(sql , ( zwmc ,  gsmc, zwyx ,  gzdd ))
#         conn.commit()from bs4 import BeautifulSoup
#         print('数据库插入成功')
#
#     except pymysql. Error as e:
#         print("mysql Error %d:%s" %(e.args[0],e.args[1]))
#     finally:
#         cursor.close()
#         #conn.commit()
#         conn.close()

#爬虫函数


def crawl(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) "
                      "Chrome/10.0.648.133 Safari/534.16"}
    # 构造请求的头信息，防止反爬虫
    contents = requests.get(url, timeout=30, headers=header)
    contents.encoding = 'utf-8'
    soup = BeautifulSoup(contents.text, "html.parser")
    tag_div = soup.find('div', id="searchList")

    data_dicts = dict()
    num = 1
    data = dict()
    tagg=tag_div.find_all('div',attrs={"class":"jobList"})
    for tag in tagg:
        # a_tag = tag.find('a', target="_blank")
        # if not a_tag:
        #     continue
        # 职位名称
        zwmc =  tag.find(attrs={"class": "e1"}).find('a').get_text()
        data['职位名称'] = zwmc

        # 公司名称
        gsmc = tag.find(attrs={"class": "e3"}).find('a').get_text()
        data['公司名称'] = gsmc

        # 职位月薪
        zwyx = tag.find('span',class_="e2").get_text()
        data['职位月薪'] = zwyx
        print(zwyx)
        # 工作地点
        # gzdd = tag.find(attrs={"class=l2": "class=e1"}).get_text()
        # data['工作地点'] = gzdd

        data_dicts[num] = data
        print(data)
        num += 1
        data.clear()

    with open("Result_dd.txt", 'a', encoding='utf-8') as f:
        f.write(str(data_dicts))
        # connectMysql(zwmc, gsmc, zwyx, gzdd)


# 主函数
if __name__ == '__main__':

    # 翻页执行crawl(url)爬虫
    i = 1
    while i <= 2:
        url = ' http://www.chinahr.com/sou/?city=34%2C398&keyword=java&page='+'str(i)'
        crawl(url)
        time.sleep(1)
        i += 1
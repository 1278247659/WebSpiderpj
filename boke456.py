# -*- coding: utf-8 -*-

import requests
import time

from bs4 import BeautifulSoup
import codecs
import  requests
import pymysql
import json
import  codecs
def connectMysql(zwmc, gsmc, zprs, gzdd):
    try:
        conn=pymysql.connect(host='localhost',user='root',passwd='12345',port=3306,db='my',charset="utf8")
        cursor=conn.cursor()
        # cursor.execute("drop table if exists douban")
        creat_table = "CREATE TABLE if not exists douban(zwmc varchar(255), gsmc varchar(255),zprs varchar(255), gzdd varchar(255))"
        cursor.execute(creat_table)
        sql="insert  into douban(zwmc,gsmc,zprs,gzdd) values(%s,%s,%s,%s)"
        cursor.execute(sql % ("'"+zwmc+"'","'"+gsmc+"'","'"+zprs+"'","'"+gzdd+"'"))
        cursor.execute(sql , ( zwmc ,  gsmc, zprs ,  gzdd ))
        conn.commit()
        print('豆豆，数据库插入成功！')
    except Exception as e:
        print('豆豆，数据库插入失败！')
        print(e)

    except pymysql. Error as e:
        print("mysql Error %d:%s" %(e.args[0],e.args[1]))
    finally:
        cursor.close()
        #conn.commit()
        conn.close()

#爬虫函数


def crawl(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) "
                      "Chrome/10.0.648.133 Safari/534.16"}
    # 构造请求的头信息，防止反爬虫
    contents = requests.get(url, timeout=30, headers=header)
    contents.encoding = 'utf-8'
    soup = BeautifulSoup(contents.text, "html.parser")
    # tag_div = soup.find('ul', class_="searchResultListU1")
    # for tag in soup.find_all(attrs={"class": "searchResultItemSimple clearfix"}):
    data_dicts = dict()
    num = 1
    data = dict()
    ul_tag = soup.find('ul', class_='searchResultListUl')
    for tag in ul_tag.find_all('li'):
        # 职位名称
        zwmc = tag.find('a', target="_blank").get_text()
        data['职位名称'] = zwmc
        # 公司名称
        gsmc = tag.find('span').get_text()
        data['公司名称'] = gsmc

        # 招聘人数
        zprs = tag.find('em', class_="searchResultJobPeopnum").get_text()
        data['招聘人数'] = zprs
        # 工作地点
        gzdd = tag.find('em', class_="searchResultJobCityval").get_text()
        data['工作地点'] = gzdd

        data_dicts[num] = data
        num += 1
        # data.clear()
    #
    # with open("Result_qq.txt", 'a', encoding='utf-8') as f:
    #     f.write(str(data_dicts)+'\n')

        connectMysql(zwmc, gsmc, zprs, gzdd)


# 主函数
if __name__ == '__main__':

    # 翻页执行crawl(url)爬虫

    i = 1
    while i <= 2:
        url = 'https://xiaoyuan.zhaopin.com/full/0/0_0_0_0_0_-1_java%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88,1_'+str(i)+'_0'
        # "https://xiaoyuan.zhaopin.com/full/0/0_0_0_0_0_-1_java软件工程师,1_1_0"
        crawl(url)
        time.sleep(1)

        i += 1
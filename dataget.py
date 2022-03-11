import requests
import re
import csv

#爬取数据
'''（国家能源局）2012年至2021年的 url * 10
url =[
    "http://www.nea.gov.cn/2012-12/14/c_132038797.htm",
    "http://www.nea.gov.cn/2013-12/14/c_132967312.htm",
    "http://www.nea.gov.cn/2014-12/15/c_133856492.htm",
    "http://www.nea.gov.cn/2015-12/16/c_134923765.htm",
    "http://www.nea.gov.cn/2016-12/15/c_135907156.htm",
    "http://www.nea.gov.cn/2017-12/21/c_136842885.htm",
    "http://www.nea.gov.cn/2018-12/20/c_137687422.htm",
    "http://www.nea.gov.cn/2019-12/26/c_138659627.htm",
    "http://www.nea.gov.cn/2020-12/18/c_139600798.htm",
    "http://www.nea.gov.cn/2021-12/17/c_1310378945.htm"
     ]
'''

'''2012年至2021年的 compile，使用正则表达式来获取数据，每一年的格式有变化
compile =[
    #r'<title>(?P<powersupply>.*?)</title>'
    r'<td style=.*?(?:电源基本建设投资完成额|电源工程投资完成).*?'
    r'<td style=.*?亿元.*?<td style=.*?<td style=.*?'
    r'<span style=.*?>.*?(?P<powersupply>\d\d\d\d)(?:\s|| </font>)</span>.*?'
    r'<td style=.*?(?:电网基本建设投资完成额|电网工程投资完成).*?'
    r'<td style=.*?亿元.*?<td style=.*?<td style=.*?'
    r'<span style=.*?>.*?(?P<powergrid>\d\d\d\d)(?:\s|| </font>)</span>.*?'
]
'''
'''置为空列表用来存储数据,其中powersupply作为电源工程投资,powergrid作为电网工程投资'''

'''
powersupply=[]
powergrid=[]
for i in range(10):
    resp=requests.get(url=url[i])               #发送请求
    page_ment=resp.content.decode("utf-8")
    #print(type(page_ment))
    obj=re.compile(compile[0],re.S)             #解析数据
    result=obj.finditer(page_ment)              #开始匹配
    for j in result:
        powersupply.append(int(j.group("powersupply").strip()))
        powergrid.append(int(j.group("powergrid").strip()))
print("powersupply列表作为电源工程投资，数据如下")
print(powersupply)
print("powergrid列表作为电源工程投资，数据如下")
print(powergrid)
powerconstruct=[powersupply[i]+powergrid[i] for i in range(10)]
print("powerconstruct列表作为电力工程总投资，数据如下")
print(powerconstruct)
'''
url ="http://https--data--stats--gov--cn--e4192.proxy.www.stats.gov.cn/easyquery.htm"

resp =requests.post(url=url)
page_ment = resp.text
print(page_ment)
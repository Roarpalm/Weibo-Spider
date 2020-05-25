import requests
import json
import datetime
import xlrd
import xlwt
import os
from concurrent.futures import ThreadPoolExecutor as thp
from xlutils.copy import copy
from lxml import etree

if not os.path.exists('微博热搜.xls'):
    workbook = xlwt.Workbook() # 新建工作簿
    workbook.save('微博热搜.xls')

def getBetweenDay(begin_date,end_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y/%m/%d")
    end_date = datetime.datetime.strptime(end_date, "%Y/%m/%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y/%m/%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list

def write_excel(name, value):
    workbook = xlrd.open_workbook('微博热搜.xls')
    new_workbook = copy(workbook)
    sheet = new_workbook.add_sheet(name) # 新建表格
    index = len(value) # 行数
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])
    new_workbook.save('微博热搜.xls')
    print(f'{name} 写入成功')

def Spider():
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

    cookies = 'JSESSIONID=87A460CA2E5B36A799172D1808F70E36; Hm_lvt_030f908df5513cb0a704c88c5da2bc37=1587949946; Hm_lpvt_030f908df5513cb0a704c88c5da2bc37=1587953413'
    cookie = {}
    for _ in cookies.split(';'):
        name, value = cookies.strip().split('=', 1)
        cookie[name] = value

    date_list = getBetweenDay('2020/04/29', '2020/05/12')
    for n in date_list:
        data = {
            'type': 'realTimeHotSearchList',
            't': '728446790',
            'accessToken': 'MGktCuZRv8pCvXBLswO2e60OP3wPMZ7MAkx57asa73QUmFMp6d6aDcXa7LuGEgJGeTD58jmk/N+tTofghfvZTw==',
            'date': n
        }

        url = 'https://www.enlightent.cn/research/top/getWeiboHotSearchDayAggs.do'
        response = requests.post(url, cookies=cookie, data=data, headers=header)
        if response.status_code != 200:
            print(f'HTTP:{response.status_code}')
            return
        html = response.content.decode('utf-8')
        json_data = json.loads(html)
        values = []
        value_title = ['标题', '排名', '热搜指数']
        values.append(value_title)
        for i in json_data:
            keyword = i['keyword']
            rank = i['rank']
            searchCount = i['searchCount']
            value = [keyword, rank, searchCount]
            values.append(value)
        write_excel(n.replace('/','-'), values)

def list_width():
    workbook = xlrd.open_workbook('微博热搜.xls')
    sheets = workbook.sheet_names()
    new_workbook = copy(workbook)
    for i in range(0, len(sheets)):
        sheet = new_workbook.get_sheet(i)
        first_col = sheet.col(0)
        first_col.width = 256*40 # 设置列宽
    new_workbook.save('微博热搜.xls')

Spider()
list_width()
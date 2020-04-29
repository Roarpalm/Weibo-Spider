import xlrd
import xlwt
import datetime
from xlutils.copy import copy

workbook = xlrd.open_workbook('微博热搜.xls')
sheets = workbook.sheet_names()
values = []
for k in range(0, len(sheets)-1):
    worksheet = workbook.sheet_by_name(sheets[k])
    rows = worksheet.nrows
    for n in range(1, rows):
        title = worksheet.cell_value(n, 0)
        num = worksheet.cell_value(n, 2)
        date = sheets[k]
        values.append([title, num, date])

new_workbook = xlwt.Workbook()
sheet = new_workbook.add_sheet('热搜指数') # 新建表格
first_col = sheet.col(0)
first_col.width = 256*40 # 设置列宽
third_col = sheet.col(2)
third_col.width = 256*10
index = len(values) # 行数
for i in range(0, index):
    for j in range(0, 3):
        sheet.write(i, j, values[i][j])
new_workbook.save('最高热搜.xls')
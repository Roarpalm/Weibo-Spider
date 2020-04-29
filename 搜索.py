import xlrd
import xlwt
from xlutils.copy import copy

workbook = xlrd.open_workbook('微博热搜.xls')
sheets = workbook.sheet_names()
values = []
for k in range(0, len(sheets)-1):
    worksheet = workbook.sheet_by_name(sheets[k])
    rows = worksheet.nrows
    for n in range(1, rows):
        title = worksheet.cell_value(n, 0)
        values.append(title)

for i in values:
    if '特朗普' in i:
        print(i)
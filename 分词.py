import xlrd
import xlwt
from xlutils.copy import copy
import jieba

workbook = xlrd.open_workbook('微博热搜.xls')
sheets = workbook.sheet_names()
keywords = []
for k in range(0, len(sheets)):
    worksheet = workbook.sheet_by_name(sheets[k])
    for i in range(0, worksheet.nrows):
        keywords.append(worksheet.cell_value(i, 0))

cut_words = []
for j in keywords:
    jieba.suggest_freq('周冬雨', True)
    jieba.suggest_freq('易烊千玺', True)
    jieba.suggest_freq('蔡徐坤', True)
    jieba.suggest_freq('何灵', True)
    jieba.suggest_freq('男装周', True)
    jieba.suggest_freq('李天一', True)
    jieba.suggest_freq('李七月', True)
    jieba.suggest_freq('李国庆', True)
    seg_list = jieba.cut(j, cut_all=False)
    for n in seg_list:
        cut_words.append(n)
with open('weibo.txt', 'w', encoding='utf-8') as f:
    for l in cut_words:
        f.write(l + ' ')
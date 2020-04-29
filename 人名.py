import jieba
import jieba.posseg as pseg
with open('weibo.txt', 'r', encoding='utf-8') as f:
    data = f.read()
words = pseg.cut(data) #jieba默认模式
with open('name.txt', 'w', encoding='utf-8') as f:
    for word, flag in words:
        if flag == 'nr':
            f.write(word + ' ')
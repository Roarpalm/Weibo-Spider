## 热搜爬虫.py
爬取[热搜神器](https://www.enlightent.cn/research/rank/weiboSearchRank)的数据并保存在 ```微博热搜.xls```（已爬取2020/01/01-2020/04/28的数据）

注：这个网站需要用cookie进行post，cookie会失效

## 热搜指数.py
把热搜都保存在一个表，通过排序可查

## 分词.py
用 ```jieba```库拆分热搜标题并保存在 ```weibo.txt```

## 人名.py
从 ```weibo.txt``` 中提取人名，并保存在 ```name.txt``` 某些人名需手动添加到库

## 词云.py
用 ```wordcloud``` 库画出词云图

## zhihu.py
基本抄袭了[知乎这篇文章](https://zhuanlan.zhihu.com/p/86755176)给的代码，在此感谢作者

## 我爬取了从2020年1月1日到2020年4月28日的热搜，做出热搜关键词词云和人名词云如下
微博关键词

![微博关键词](weibo.png?raw=true)

人名

![人名](name.png?raw=true)
- - - -

2020年4月29日第一次更新

2020年5月25日第二次更新
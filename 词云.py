import wordcloud

with open('name.txt', 'r', encoding='utf-8') as f:
    data = f.read()
wc = wordcloud.WordCloud(font_path="simkai.ttf",background_color="white",width=800, height=660)
wc.generate(data)
wc.to_file('name.png')
# 导入必要的库
import jieba
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# 读取文本文件
with open('word_data_file.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 使用jieba进行中文分词
word_list = jieba.cut(text)

# 加载停用词表
stopwords = set(STOPWORDS)
with open('stopwords.txt', 'r', encoding='utf-8') as f:
    for line in f:
        stopwords.add(line.strip())

# 生成词云
mask = np.array(Image.open("mask_image.png")) # 遮蔽图片
# wc = WordCloud(background_color="white", max_words=2000, mask=mask, stopwords=stopwords, font_path='simsun.ttf')
wc = WordCloud(background_color="white", max_words=2000, mask=mask, stopwords=stopwords, font_path='SimSun.ttf')
wc.generate_from_text(" ".join(word_list))

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

import jieba
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# 设置停用词
stopwords = set(STOPWORDS)
stopwords.add("云")
stopwords.add("风")

# 导入文本文件并进行分词处理
text = open('word_data_file.txt').read()
words = jieba.cut(text, cut_all=False)

# 创建词频字典
word_dict = {}
for word in words:
    if len(word) > 1 and not word.isdigit() and word not in stopwords:
        word_dict[word] = word_dict.get(word, 0) + 1

# 加载遮蔽图像并生成颜色
mask = np.array(Image.open("mask_image.png"))
image_colors = ImageColorGenerator(mask)

# 创建WordCloud对象并生成词云
# wc = WordCloud(font_path='your_font.ttf', background_color="white", max_words=2000, mask=mask, stopwords=stopwords, contour_width=3, contour_color='steelblue')
wc = WordCloud(background_color="white", max_words=2000, mask=mask, stopwords=stopwords, contour_width=3, contour_color='steelblue')
wc.generate_from_frequencies(word_dict)
wc.recolor(color_func=image_colors)
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.show()

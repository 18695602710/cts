# encoding:utf-8
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import jieba
d = path.dirname(__file__)
text = open(path.join(d, 'cts.txt'),encoding='utf-8').read()
# 结巴分词
stopwords = [line.strip() for line in open(path.join(d, 'ban.txt'), 'r').readlines()]
wordlist = jieba.cut(text)
#wl = " ".join(wordlist)
outstr = ''
for word in wordlist:
    if word not in stopwords:
        if word != '\t':
            outstr += word
            outstr += " "
cloud_mask = np.array(Image.open(path.join(d, "1.png")))
wordcloud = WordCloud(background_color="white",max_words=200,mask=cloud_mask,font_path='HYQiHeiY4-95W.otf').generate(outstr)
image_colors = ImageColorGenerator(cloud_mask)
wordcloud.recolor(color_func=image_colors)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.show()
wordcloud.to_file(path.join(d,"cloud_word.png"))
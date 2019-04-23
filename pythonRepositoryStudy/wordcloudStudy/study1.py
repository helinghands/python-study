from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


# Read the whole text.
text = open(r'test.txt').read()

alice_coloring = np.array(Image.open(r"1.jpg"))
# 设置停用词
stopwords = set(STOPWORDS)
stopwords.add("said")

# 你可以通过 mask 参数 来设置词云形状
wc = WordCloud(background_color="black", max_words=2000,mask=alice_coloring,stopwords=stopwords, max_font_size=40,random_state=42)
wc.generate(text)
# image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")#关闭坐标轴
plt.show()
# # 显示效果一图
# plt.imshow(wc, interpolation="bilinear")
# plt.axis("off")
# plt.figure()#新建一个画图窗口
# plt.show()

# # 显示效果二图
# plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
# plt.axis("off")
# plt.figure()
# plt.show()

# # 显示原图
# plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
# plt.axis("off")
# plt.show()

import jieba
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#读取文件
text = open(r'test.txt','r').read()
#使用结巴截取单词
result_word = jieba.cut(text,cut_all=True)
#存放截取的单词
str = []
#读取截取的单词并存放到str中
for item in result_word:
    if len(item) >= 1 and item != '\r\n':
        str.append(item)
#存放所有的单词-->key:单词、value：单词出现的次数
dict = {}
#统计数组中每个单词出现的次数并将其存放到dict字典中
for key in str:
    dict[key] = dict.get(key, 0) + 1
print(dict)
#我们需要的模板图片
alice_coloring = np.array(Image.open(r"alice_color.png"))
#使用wordcloud的WorldCloud
wc = WordCloud(background_color="white",  max_words=2000,mask=alice_coloring,stopwords=STOPWORDS.add("said"), max_font_size=40,random_state=42)

wc.generate_from_frequencies(dict)
plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file("result.png")
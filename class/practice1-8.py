import jieba
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

#读取文件
f = open(r'test.txt','r')
text = f.read()
#使用结巴截取单词
result_word = jieba.cut(text,cut_all=True)
#存放截取的单词
str = []
#文件关闭
f.close();
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
# 背景颜色，词云显示的最大词数， 设置背景图片，字体最大值
wc = WordCloud(background_color="white",  max_words=2000,mask=alice_coloring,stopwords=STOPWORDS.add("said"), max_font_size=40,random_state=42)
# 生成词云, 可以用generate输入全部文本(中文不好分词),也可以我们计算好词频后使用generate_from_frequencies函数
wc.generate_from_frequencies(dict)
plt.imshow(wc)
#关闭坐标轴刻度
plt.axis("off")
plt.show()
#将结果输出成result.png
wc.to_file("result.png")
import jieba
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

text = open(r'test.txt','r').read()
result_word = jieba.cut(text,cut_all=True)
str = []
for item in result_word:
    if len(item) >= 1 and item != '\r\n':
        str.append(item)
print(str)
dict = {}
for key in str:
    dict[key] = dict.get(key, 0) + 1
print(dict)
alice_coloring = np.array(Image.open(r"alice_color.png"))
wc = WordCloud(background_color="white",  max_words=2000,
                   mask=alice_coloring,
                   stopwords=STOPWORDS.add("said"),
                   max_font_size=40,
                   random_state=42)
wc.generate_from_frequencies(dict)
plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file("result.png")
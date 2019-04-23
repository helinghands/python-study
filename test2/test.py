import jieba
import numpy
import codecs
import pandas
import matplotlib.pyplot as plt
from wordcloud import WordCloud

file = codecs.open(r"test.txt",encoding="UTF-8")
content = file.read()
file.close()
segment=[]
segs=jieba.cut(content)
for seg in segs:
    if len(seg) > 1 and seg != '\r\n':
        segment.append(seg)

words_df = pandas.DataFrame({'segment':segment})
stopwords = pandas.read_csv('stopword.txt',index_col=False,quoting=3,sep='，',names=['stopword'],encoding="utf-8")
words_df=words_df[~words_df.segment.isin(stopwords.stopword)]

words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
words_stat = words_stat.reset_index().sort_values(by=["计数"],ascending=False)
words_df.head()


wordcloud = WordCloud(font_path='simhei.ttf',background_color='black')
words_frequence = {x[0]:x[1] for x in words_stat.values}

#fit_word函数，接受字典类型，其他类型会报类似没有items属性的错误
wordcloud = wordcloud.fit_words(words_frequence)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
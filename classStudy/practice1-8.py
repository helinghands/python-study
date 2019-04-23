"统计单词出现的频率"
import re
from os import path

import imageio as imageio
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

p = path.dirname(__file__)
def Getwords():
    # 存放原始数据列表
    list=[]
    #临时存放单词计数的字典
    result = {}
    #存放单词排序后的结果字典
    result2={}
    try:
        # 文章文件的路径
        # f = open(r"C:\Users\Administrator\Desktop\test.txt", "r+")
        f =open(path.join(p, "text.txt"),"r+")
        txt=f.read().lower()
        f.close()
        words=re.sub('[.?!\']',"" ,txt).split()

        while True:
            #拷贝数组
            list=words.copy()
            a = 0
            k = len(list)
            #循环退出条件数组为0
            if k==0:
                #对字典进行排序
                list2=sorted(result.items(),key=lambda items:items[1],reverse=True)
                for j in list2:
                    result2[j[0]]=j[1]
                break
                #判断词重复的个数
            a=list.count(list[0])
            result[list[0]]=a
            while list[0] in words:
                words.remove(list[0])
                if len(words) == 0:
                    break
        return result2
    except IOError:
        print("文件不存在："+r"test.txt")

def PaintCloud(word):
    #获取当前文件路径
    alice_coloring = imageio.imread(path.join(p, "alice_color.png"))
    # 背景颜色，词云显示的最大词数， 设置背景图片，字体最大值
    wc = WordCloud(background_color="white",  max_words=2000,
                   mask=alice_coloring,
                   stopwords=STOPWORDS.add("said"),
                   max_font_size=40,
                   random_state=42)
    # 生成词云, 可以用generate输入全部文本(中文不好分词),也可以我们计算好词频后使用generate_from_frequencies函数
    wc.generate_from_frequencies(word)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    wc.to_file(path.join(p, "result.png"))

if __name__ == '__main__':
    d=Getwords()
    print(d)
    PaintCloud(d)

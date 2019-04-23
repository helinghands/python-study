"""
import wordcloud
w = wordcloud.WordCloud()
w.generate("python and wordclud")
w.to_file("1.png")#保存文件
"""
import wordcloud
import jieba
f = open("test.txt",'r').read()
print(f)
result_list = jieba.cut(f,cut_all=True)
for item in result_list:
    print(item)
"""
# width,height,margin可以设置图片属性
# generate 可以对全部文本进行自动分词,但是对中文支持不好
# 可以设置font_path参数来设置字体集
#background_color参数为设置背景颜色,默认颜色为黑色
"""
w = wordcloud.WordCloud(background_color="white",width=1000, height=860, margin=2).generate(f)
w.to_file('test.png')


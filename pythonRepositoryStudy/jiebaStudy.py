# encoding=utf-8
import jieba
"""
1、分词
jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的 generator，
可以使用 for 循环来获得分词后得到的每一个词语
"""
#全模式
result_list = jieba.cut("我是陈亮，是成都大学的一名在校大学生",cut_all=True)
print("Full Mode:","/".join(result_list))

#精确模式
result_list = jieba.cut("我是陈亮，是成都大学的一名在校大学生",cut_all=False)
print("Default Mode:"," ".join(result_list))

#默认是精确模式
result_list = jieba.cut("我是陈亮，是成都大学的一名在校大学生")
print("Default Mode:","\t".join(result_list))

#搜索引擎模式
result_list = jieba.cut_for_search("我是陈亮，是成都大学的一名在校大学生")
print("搜索引擎：",",".join(result_list))

"""
用jieba.lcut以及jieba.lcut_for_search直接返回list
"""
result_list = jieba.lcut("我是陈亮，是成都大学的一名在校大学生")
print(result_list)

result_list = jieba.lcut_for_search("我是陈亮，是成都大学的一名在校大学生")
print(result_list)


"""
2、添加自定义的字典
"""

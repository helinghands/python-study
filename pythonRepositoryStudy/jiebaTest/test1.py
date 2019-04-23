#encoding=utf-8
import jieba
import  codecs
import jieba.posseg as pseg
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
#自定义字典
#使用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来。
'''
str='「台中」正确应该不会被切开'
print('/'.join(jieba.cut(str, HMM=False)))
jieba.suggest_freq(('台中'),True)
print('/'.join(jieba.cut(str, HMM=False)))
'''

#使用add_word(word, freq=None, tag=None) 和 del_word(word) 可在程序中动态修改词典。
str = '他以完成总布局、短时间内取得积极成果的原因、未来走向与重点三个角度'
print("未使用add_word:",'/'.join(jieba.cut(str)))
jieba.add_word('总布局')
jieba.add_word('积极成果')
print("使用add_word:",'/'.join(jieba.cut(str)))

jieba.del_word('完成')
print("使用del_word:",'/'.join(jieba.cut(str)))

#将jieba截取数据添加到文件中
file = codecs.open('man_data.txt', 'w', encoding="utf-8")
word=jieba.cut('他以完成总布局、短时间内取得积极成果的原因、未来走向与重点三个角度，向读者传达了“一带一路”现今及未来的发展。')
for item in word:
    file.write(item+"\n")
file.close()


words = pseg.cut("我爱北京天安门")
for word, flag in words:
    print('%s %s' % (word, flag))

result = jieba.tokenize(u'永和服装饰品有限公司')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0], tk[1], tk[2]))

#将jieba.cut截取的词频输入到列表中
result1 = jieba.cut("他以完成总布局、短时间内取得积极成果的原因、未来走向与重点三个角度，向读者传达了“一带一路”现今及未来的发展。他以完成总布局、短时间内取得积极成果的原因、未来走向与重点三个角度，向读者传达了“一带一路”现今及未来的发展。")
seq_result=[]
for item in result1:
    if len(item)>1 and item != "\r\n":
        seq_result.append(item)
print(seq_result)
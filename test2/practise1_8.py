import string
import time

path='E:\\Python\\test2\\test.txt'
with open(path,'r') as text:
    words=[raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index=set(words)
    counts_dict={index:words.count(index) for index in words_index}
for word in sorted(counts_dict,key=lambda x:counts_dict[x],reverse=True):
    time.sleep(2)
    print ('{}--{} times'.format(word,counts_dict[word]))
    file_handle=open('1.txt',mode='a',encoding="UTF-8")
    file_handle.write('{}--{}'.format(word,counts_dict[word]))
    file_handle.write("\n")
file_handle.close()
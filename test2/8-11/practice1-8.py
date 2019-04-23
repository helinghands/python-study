# practice1-8
s = input("输入一串英文短文：")
l = len(s)
vlist = []
vb = {}
left = 0
key = 0
for i in range(l):
    if s[i] < 'a' or s[i] > 'z':  # 若非字母
        if key:  # 若上个是字母
            vlist.append(s[left:i])  # 截取单词
            left = i + 1
            key = 0
        else:  # 若上个不是字母 则left继续后移
            left += 1
    else:  # 若当前是字母 则标记key为一 代表上个字符是字母
        key = 1
        if i == l - 1:  # 若遍历道最后一个字符
            if left != i:  # left!=i代表最后一个单词不是单个字母组成的
                vlist.append(s[left:i])
            else:  # 最后单词为单个字母组成 则取单个字符
                vlist.append(s[left])

print(vlist)
for v in vlist:
    vb.update({v: 0})
for v in vlist:
    if vb[v] != None:
        vb[v] += 1
print(vb)

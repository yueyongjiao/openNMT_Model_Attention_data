# coding:utf-8
import sys
import chardet


def code(path):
    f = open(path, 'rb')
    f_read = f.read()
    f_charInfo = chardet.detect(f_read)
    return f_charInfo

s = sys.argv[1]
wd = {}
print(code('word_dic'))
f = open('word_dic')
wid = 0
for line in f:
    res = line.strip().split(' ')
    wd[res[0]] = wid
    wid += 1
f.close()
wd['<unk>'] = wid
print(len(wd))
wd[''] = 0

f = open(s)
fw = open(s + '_id', 'wb')
for line in f:
    res = line.strip().split(' ')
    for i in range(len(res) - 1):
        # print(wd[res[i].decode('utf-8')])
        if res[i] in wd:
            fw.write(str(wd[res[i]]) + ' ')

    fw.write(str(wd[res[-1]]) + '\n')
fw.close()
f.close()




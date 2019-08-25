# f = open('news.txt','r')
# lines = f.readlines()

# count = 0 
# for line in lines:
#     splited_line = line.split(' ')
#     count = count + len(splited_line)
#     # print(line.strip())
# print(count)


# # print(lines)


f = open('news.txt','r')
lines = f.readlines()

count = 0
d ={}
for line in lines:
    splited_line = line.strip().split()
    for i in splited_line:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1

import json
print(json.dumps(d,indent=2))



wmax = 0
mword = ''
for word in d:
    if d[word] > wmax:
        wmax = d[word]
        mword=word

print("{} : {}".format(mword,wmax))
# 第一种画心形的方式
# print('\n'.join([''.join([('Love'[(x-y) % len('Love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))


# 第二中画心形的方式
'''
import time
# sentence = "Dear, I love you forever!"
sentence = "love"
for char in sentence.split():
   allChar = []
   for y in range(12, -12, -1):
       lst = []
       lst_con = ''
       for x in range(-30, 30):
            formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if formula <= 0:
                lst_con += char[(x) % len(char)]
            else:
                lst_con += ' '
       lst.append(lst_con)
       allChar += lst
   print('\n'.join(allChar))
   time.sleep(1)
'''


# 第三种
char = "love"
for y in range(30, -30, -1):
    value = []
    for x in range(-30, 30):
        if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0:
            value.append(char[(x) % len(char)])
        else:
            value.append(" ")
        s = "".join(value)
    print(s)
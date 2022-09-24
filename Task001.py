# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

from encodings import utf_8

with open("Task001.txt", "r+", encoding = 'utf_8') as f:
    for line in f.readlines():
        print(line)
        line = list(filter(lambda x: 'абв' not in x, line.split()))
        line = ' '.join(line)
print(line)

f = open('Task001.txt','a', encoding = 'utf_8')
f.seek(0)
f.truncate()
f.writelines(line + '\n')
f.close()

# sub_s = 'абв'
# s = 'абвгдейка это не только ценный мехабв, но и 4 кгабв легкоусвояемого мяса'
# print("The original string is : " + s)
# ori_list = s.split()
# print("The original list is : " + str(ori_list))
# print("The substring is : " + sub_s)
#
# res = []
# flag = 1
# for item in ori_list:
#     for i in sub_s:
#         if i not in item:
#             flag = 1
#         else:
#             flag = 0
#             break
#     if (flag == 1):
#         res.append(item)
#
# print("The filtered string is : " + ' '.join(res))
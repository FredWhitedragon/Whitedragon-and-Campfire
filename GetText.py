import os
import pyperclip as pyc

if input('要粘贴的故事为sfw还是nsfw？[0/1]\n') == '0':
    file_path = 'sfw'
else:
    file_path = 'nsfw'

file_list = os.listdir(file_path)
for i in range(len(file_list)):
    print(i, file_list[i], '\n')
num = int(input('想要粘贴的故事角标：\n'))
with open(file_path + '\\' + file_list[num], 'r', encoding = 'utf-8') as file:
    text = ''
    lines = file.readlines()
    for l in lines:
        text += ' ' + l
    pyc.copy(text)
    print(file_list[num] + '复制完成！')
os.system('pause')
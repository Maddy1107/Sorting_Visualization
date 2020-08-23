import random

ele = '[11,2,3,45,5,6,7,8,92]'
text = []
element = ""
for i in ele:
    if i == '[':
        continue
    elif i == ',' or i == ']':
        text.append(int(element))
        element = ""
    else:
        element += i
# text.append(int(element[:-1]))
print(text)

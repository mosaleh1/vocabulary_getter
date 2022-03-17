import re

file = open("transcript", "r")
mylist = []
for line in file:
    words = re.findall("[A-Za-z]+", line)
    for word in words:
        mylist.append(word)
print(len(mylist))


words = set(mylist)
print(words)
print(len(words))
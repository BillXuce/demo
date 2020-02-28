names=[]
with open('names.txt', encoding="utf-8") as a:
    for line in a.readlines():
        name=line.split()
        names.append(name[0])
print(names)
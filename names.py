names=[]
with open('names.txt', encoding="utf-8") as f:
    for line in f.readlines():
        name=line.split()
        names.append(name[0])
print(names)
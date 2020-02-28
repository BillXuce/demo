names=[]
with open('names.txt') as a:
    for line in a.readlines():
        name=line.split()
        names.append(name[0])
print(names)
spisok = ['sanya', 'tema', 'luntik', 19, 13, 26]
a = []
b = []
file = open('dz.txt', 'a')
for i in spisok:
    if type(i) is str:
        a.append(i)
    elif type(i) is int:
        i = int(i)
        b.append(i)
a.sort()
b.sort()
for i in a:
    file.write(i + '\n')
for i in b:
    i = str(i)
    file.write(i + '\n')
file.close()
fileop1 = open('dz.txt')
fileop2 = fileop1.readlines()
print(a)
print(fileop2)
fileop1.close()

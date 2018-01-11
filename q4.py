with open("q4.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = [x.split() for x in content]
content2 = []
for i in content:
    temp = []
    for j in i:
        temp.append(''.join(sorted(j)))
    content2.append(temp)

def func(c):
    valid = 0
    for i in c:
        for j in range(len(i)):
            if i.count(i[j]) > 1:
                break
            if j == (len(i) - 1):
                valid +=1
    return valid



print(func(content))
print(func(content2))

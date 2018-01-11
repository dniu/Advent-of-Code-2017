with open ("q12.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = [x.split(' <-> ') for x in content]

pipe = {}
seen = []
q = ['0']

for i in content:
    if len(i) > 1:
        i[1] = i[1].split(", ")
for i in content:
    pipe[i[0]] = i[1]

def remove():
    while len(q) > 0:
        item = q.pop(0)
        if item not in seen:
            seen.append(item)
        for j in pipe[item]:
            if j not in seen:
                q.append(j)
remove()
print("Number in group {0}: ", len(seen))
groups = 1
while len(pipe) > 0:
    for i in seen:
        del pipe[i]
    seen = []
    if len(pipe) > 0:
        groups += 1
        q.append(list(pipe.keys())[0])
        remove()
print("Groups: ", groups)

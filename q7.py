with open("q7.txt") as f:
          content = f.readlines()
content = [x.strip() for x in content]
content = [x.split(" -> ") for x in content]

def get_val(n):
    return int(n[1:len(n)-1])

def check_eql(lst):
    return lst[1:] == lst[:-1]

tot = {}
updated = {}
kids = {}
for i in content:
    #if len(i) == 1:
    name = i[0].split()[0]
    val = i[0].split()[1]
    if name not in tot:
        tot[name] = get_val(val)
    if len(i) != 1:
        kids[name] = i[1].split(", ")

def get_weight(c):
    if c in updated:
        return updated[c]
    if c not in kids:
        updated[c] = tot[c]
        return updated[c]
    total_weight = tot[c]
    for x in kids[c]:
        total_weight += get_weight(x)
    updated[c] = total_weight
    return updated[c]

def is_balanced(n):
    if n not in kids:
        return True
    lst = []
    for c in kids[n]:
        lst.append(get_weight(c))
    return check_eql(lst)

for j in content:
    name = j[0].split()[0]
    get_weight(name)

    
suspects=[]
for k in content:
    if len(k) != 1:
        name = k[0].split()[0]
        children = kids[name]
        if not is_balanced(name):
            res = [(x, updated[x]) for x in children]
            print(name, updated[name], res)
            suspects.append(name)



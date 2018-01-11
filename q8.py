with open("q8.txt") as f:
          content = f.readlines()
content = [x.strip() for x in content]
content = [x.split() for x in content]
vals = {}
most_big = [0]
def parse(x):
    st_reg = x[0]
    operation = x[1]
    value = int(x[2])
    nd_reg = x[4]
    comparing = x[5]
    value2 = int(x[6])
    do_it = False
    if not st_reg in vals:
        vals[st_reg] = 0
    if not nd_reg in vals:
        vals[nd_reg] = 0

    if comparing == '>':
        if vals[nd_reg] > value2:
            do_it = True
    elif comparing == '>=':
        if vals[nd_reg] >= value2:
            do_it = True
    elif comparing == '==':
        if vals[nd_reg] == value2:
            do_it = True
    elif comparing == '<':
        if vals[nd_reg] < value2:
            do_it = True
    elif comparing == '<=':
        if vals[nd_reg] <= value2:
            do_it = True
    elif comparing == '!=':
        if vals[nd_reg] != value2:
            do_it = True
    else:
        do_it = False
    if do_it:
        if operation == 'inc':
            vals[st_reg] += value
            
        elif operation == 'dec':
            vals[st_reg] -= value
        else:
                 pass
        if vals[st_reg] > most_big[0]:
            most_big[0] = vals[st_reg]
for i in content:
    parse(i)
key = max(vals, key=lambda key: vals[key])
print(most_big)

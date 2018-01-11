with open("q16.txt") as f:
    content = f.readlines()
content = content[0]
content = content.split(",")
cache = []
lis = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']]
#lis = [['a','b','c','d','e']]
cache.append(lis[0][:])
def spin(a):
    n = len(lis) - a - 1
    lis[0] = lis[0][n:] + lis[0][:n]
def exchange(b, c):
    temp = lis[0][b]
    lis[0][b] = lis[0][c]
    lis[0][c] = temp
def partner(d, e):
    b = lis[0].index(d)
    c = lis[0].index(e)
    exchange(b, c)

def parse(n):
    if n[0] == 's':
        spin(int(n[1:]))
    elif n[0] == 'x':
        temp = n[1:].split('/')
        exchange(int(temp[0]), int(temp[1]))
    elif n[0] == 'p':
        temp = n[1:].split('/')
        partner(temp[0], temp[1])
    else:
        pass
    
def dance(n):
    for j in range(n):
        for i in content:
            parse(i)
     
        if lis[0] in cache:
            last_seen = cache.index(lis[0])
            print("repeat at step: ", j+1, " last seen at step: ", last_seen)
            print(lis[0])
            cycle = j + 1 - last_seen
            if cycle == 0:
                return
            more_cycles = (n - j - 1) % cycle
            for k in range(more_cycles):
                for l in content:
                    parse(l)
            return
        cache.append(lis[0][:])
            
dance(1000000000)
result_string = ""
for i in lis[0]:
    result_string += i
print(result_string)

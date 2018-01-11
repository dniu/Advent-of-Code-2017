import math
with open("q23.txt") as f:
          content = f.readlines()
content = [x.strip() for x in content]
content = [x.split() for x in content]
vals = {}
vals['a'] = 0
vals['a'] = 1
vals['b'] = 0
vals['c'] = 0
vals['d'] = 0
vals['e'] = 0
vals['f'] = 0
vals['g'] = 0
vals['h'] = 0
count = [0]
def part2():
    a=b=c=d=e=f=g=h=0
    a = 1
    b = 81
    c = b
    b *= 100
    b += 100000
    c = b
    c += 17000
    # This loop runs 1001 times
    while True:
        f = 1
        d = 2
        e = 2
        while e != b:
            # f is 0 if b is composite
            if d * e == b:
                f = 0
            e += 1
        if f == 0:
            print('a', a,'b', b,'c', c,'d', d,'e', e,'f', f,'g', g,'h', h)
            h += 1
        if b == c:
            return h
        b += 17

def is_composite(n):
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return True
    return False

def part2_fast():
    a=b=c=d=e=f=g=h=0
    a = 1
    b = 81
    c = b
    b *= 100
    b += 100000
    c = b
    c += 17000
    # This loop runs 1001 times
    for i in range(1001):
        if is_composite(b):
            h += 1
        b += 17
    return h
    
def parse(i, x):
    #print(i, x, vals)
    cmd = x[0]
    if x[1] in vals:
        val1 = vals[x[1]]
    else:
        val1 = int(x[1])
    if x[2] in vals:
        val2 = vals[x[2]]
    else:
        val2 = int(x[2])
    if cmd == "set":
        vals[x[1]] = val2
    if cmd == "sub":
        vals[x[1]] -= val2
    if cmd == "mul":
        count[0] += 1
        vals[x[1]] *= val2
    if cmd == "jnz":
        print(i, x, vals)
        if val1 != 0:
            return i + val2
    return i + 1
i = 0
#while i < len(content):
#    i = parse(i, content[i])
#print(count)
#print(vals['h'])

def func(x):
    pos = 0
    n = [0]
    v = 1
    for i in range (1,50000001):
        #print(n, pos)
        #for j in range(1, x+1):
            #abc += n[(pos+j) % len(n)]
        #print("abc is :" ,abc)
        pos += x
        pos = pos % len(n)
        n.insert(pos + 1, i)
        pos = pos + 1
        if v != n[(n.index(0)+1) % len(n)]:
            print(i)
            v = n[(n.index(0)+1) % len(n)]
    return "done"
print(func(304))

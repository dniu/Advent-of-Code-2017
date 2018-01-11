import math
with open("q21.txt") as f:
          content = f.readlines()
content = [x.strip() for x in content]
content = [x.split(' => ') for x in content]
evo = {}
for i in range(len(content)):
    content[i][0] = content[i][0].replace("/","")
    content[i][1] = content[i][1].replace("/","")
def rot90_2(s):
    return s[2]+s[0]+s[3]+s[1]
def flipx_2(s):
    return s[1]+s[0]+s[3]+s[2]
def flipy_2(s):
    return s[2]+s[3]+s[0]+s[1]
def flipxy(s):
    return s[::-1]
def rot90_3(s):
    return s[6]+s[3]+s[0]+s[7]+s[4]+s[1]+s[8]+s[5]+s[2]
def flipx_3(s):
    return s[2]+s[1]+s[0]+s[5]+s[4]+s[3]+s[8]+s[7]+s[6]
def flipy_3(s):
    return s[6]+s[7]+s[8]+s[3]+s[4]+s[5]+s[0]+s[1]+s[2]

for i in content:
    if len(i[0]) == 4:
        rot = rot90_2
        flipx = flipx_2
        flipy = flipy_2
    else:
        rot = rot90_3
        flipx = flipx_3
        flipy = flipy_3
    t = i[0]
    for _ in range(4):
        t = rot(t)
        xt = flipx(t)
        yt = flipy(t)
        xyt = flipxy(t)
        if t not in evo:
            evo[t] = i[1]
        if xt not in evo:
            evo[xt] = i[1]
        if yt not in evo:
            evo[yt] = i[1]
        if xyt not in evo:
            evo[xyt] = i[1]

def split(s):
    n = len(s)
    m = int(math.sqrt(n))
    if m % 2 == 0:
        res = []
        for i in range(0,m,2):
            for j in range(0,m,2):
                res.append(s[i*m+j:i*m+j+2]+s[(i+1)*m+j:(i+1)*m+j+2])
    else:
        res = []
        for i in range(0,m,3):
            for j in range(0,m,3):
                res.append(s[i*m+j:i*m+j+3]+s[(i+1)*m+j:(i+1)*m+j+3]+s[(i+2)*m+j:(i+2)*m+j+3])
        
    return res
def recombine(l):
    #if len(l) == 1:
     #   return l[0]
    n = len(l[0])
    res = ""
    if n == 9:
        m = int(math.sqrt(9*len(l)))
        for x in range(0, m//3):
            for i in range(x * m//3, (x+1) * m//3):
                res+=l[i][0:3]
            for i in range(x * m//3, (x+1) * m//3):
                res+=l[i][3:6]
            for i in range(x * m//3, (x+1) * m//3):
                res+=l[i][6:9]
    else:
        m = int(math.sqrt(16*len(l)))
        for x in range(0, m//4):
            for i in range(x * m//4, (x+1) * m//4):
                res+=l[i][0:4]
            for i in range(x * m//4, (x+1) * m//4):
                res+=l[i][4:8]
            for i in range(x * m//4, (x+1) * m//4):
                res+=l[i][8:12]
            for i in range(x * m//4, (x+1) * m//4):
                res+=l[i][12:16]
    return res

board = ".#...####"
for i in range(18):
    board_list = split(board)
    new_list = [evo[x] for x in board_list]
    board = recombine(new_list)
print("Total count:",board.count('#'))

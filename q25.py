vals = {}

def do_A(pos):
    if pos not in vals:
        vals[pos] = 1
        pos += 1
        return pos, do_B
    else:
        del vals[pos]
        pos -= 1
        return pos, do_D

def do_B(pos):
    if pos not in vals:
        vals[pos] = 1
        pos += 1
        return pos, do_C
    else:
        del vals[pos]
        pos += 1
        return pos, do_F

def do_C(pos):
    if pos not in vals:
        vals[pos] = 1
        pos -= 1
        return pos, do_C
    else:
        pos -= 1
        return pos, do_A

def do_D(pos):
    if pos not in vals:
        pos -= 1
        return pos, do_E
    else:
        pos += 1
        return pos, do_A

def do_E(pos):
    if pos not in vals:
        vals[pos] = 1
        pos -= 1
        return pos, do_A
    else:
        del vals[pos]
        pos += 1
        return pos, do_B

def do_F(pos):
    if pos not in vals:
        pos += 1
        return pos, do_C
    else:
        del vals[pos]
        pos += 1
        return pos, do_E

pos = 0
func = do_A
i = 0
while i < 12317297:
    #print(i, func)
    res = func(pos)
    pos = res[0]
    func = res[1]
    i += 1
print(len(vals))


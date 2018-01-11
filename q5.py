with open("q5.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = [int(x) for x in content]
test = [0, 3, 0, 1, -3]

def func(n):
    pos = 0
    steps = 0
    while pos < len(n):
        old_val = n[pos]
        old_pos = pos
        pos += old_val
        if old_val >= 3:
            n[old_pos] -= 1
        else:
            n[old_pos] += 1
        steps += 1
    return steps

print(func(content))

a = '{}'
b = '{{{}}}'
c = '{{},{}}'
d = '{{{},{},{{}}}}'
e = '{<a>,<a>,<a>,<a>}'
f = '{{<ab>},{<ab>},{<ab>},{<ab>}}'
g = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
h = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
i = '<>'
j = '<random characters>'
k = '<<<<>'
l = '<{!>}>'
m = '<!!>'
n = '<!!!>>'
o = '<[o"i!a,<{i<a>'
with open ("q9.txt") as f:
    content = f.readlines()
real = content[0].strip()

def func(n):
    i = 0
    score = 0
    garbage_count = 0
    depth = 0
    is_garbage = False
    while i < len(n):
        #print(n[i], is_garbage)
        if is_garbage and n[i] != '!' and n[i] != '>':
            garbage_count += 1
        elif n[i] == '<' and not is_garbage:
            is_garbage = True
        elif n[i] == '>' and is_garbage:
            is_garbage = False
        elif n[i] == '{' and not is_garbage:
            depth += 1
        elif n[i] == '}' and not is_garbage:
            score += depth
            depth -= 1
        elif n[i] == '!':
            i += 1
        i += 1
    #return score
    return garbage_count
print(func(real))

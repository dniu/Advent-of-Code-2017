def get_pos_max(n):
    largest_pos = 0
    largest_val = 0
    for i in range(len(n)):
        if n[i] > largest_val:
            largest_pos = i
            largest_val = n[i]
    return (largest_pos, largest_val)

test = [0, 2, 7, 0]
input = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4,1,1,7,1,15,11]

def func(n):
    seen = []
    seen.append(n[:])
    steps = 1
    while True:
        pos = get_pos_max(n)[0]
        val = get_pos_max(n)[1]
        n[pos] = 0
        for i in range(1, val+1):
            n[(pos + i) % len(n)] += 1
        
        if n in seen:
            return steps - seen.index(n)
        seen.append(n[:])
        steps += 1

print(func(input))

with open("q22.txt") as f:
          content = f.readlines()
content = [x.split('\n')[0] for x in content]
status = {}
m = len(content)//2
for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == '#':
            status[(i,j)] = "I"
pos = (m, m)
turn_left = {'u':'l', 'l':'d', 'd':'r', 'r':'u'}
turn_right = {'u':'r', 'r':'d', 'd':'l', 'l':'u'}
reverse = {'u':'d', 'l':'r', 'r':'l', 'd':'u'}
direction = 'u'
infected = 0

for i in range(10000000):
    if pos not in status: #clean
        direction = turn_left[direction]
        status[pos] = "W"
    elif status[pos] == "W":
        status[pos] = "I"
        infected += 1
    elif status[pos] == "I":
        direction = turn_right[direction]
        status[pos] = "F"
    else:
        direction = reverse[direction]
        del status[pos]

    # Move
    if direction == 'u':
        pos = (pos[0]-1, pos[1])
    elif direction == 'r':
        pos = (pos[0], pos[1]+1)
    elif direction == 'd':
        pos = (pos[0]+1, pos[1])
    else: #direction == 'l':
        pos = (pos[0], pos[1]-1)

print(infected)

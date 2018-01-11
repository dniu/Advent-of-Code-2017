with open ("q13.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = [x.split(': ') for x in content]
content = [list(map(int, x)) for x in content]
wall_depth = {}
walls = []
for i in content:
    wall_depth[i[0]] = i[1]
total_layers = content[len(content) - 1][0]

def get_pos(t, length):
    n = length * 2 - 2
    t = t % n
    if t < length:
        return t
    return length - 1 - (t + 1 - length)


for i in range(total_layers+1):
    temp = []
    if i in wall_depth:
        for j in range(wall_depth[i]):
            temp.append([])
    walls.append(temp)
    
def get_alarm(delay):
    alarm = 0
    caught = False
    for i in range(total_layers+1):
        if i in wall_depth:
            if get_pos(delay + i, wall_depth[i]) == 0:
                alarm += (i * wall_depth[i])
                caught = True
    return (alarm, caught)

shortest_delay = 0
while True:
    if not get_alarm(shortest_delay)[1]:
        break
    shortest_delay += 1
print("shortest delay is: ", shortest_delay)

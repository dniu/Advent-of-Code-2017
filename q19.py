with open("q19.txt") as f:
          content = f.readlines()
content = [x.split('\n')[0] for x in content]

def get_start():
    for i in range(len(content[0])):
        if content[0][i] != ' ':
            return i
pos = (0, get_start())
direction = 'down'
step_count = 0
keep_going = True
total_string = ""

while keep_going:
    step_count += 1
    #print (pos)
    if direction == 'down':
        pos = (pos[0]+1, pos[1])
    elif direction == 'up':
        pos = (pos[0]-1, pos[1])
    elif direction == 'left':
        pos = (pos[0], pos[1]-1)
    else:
        pos = (pos[0], pos[1]+1)
    location = content[pos[0]][pos[1]]
    if location == '+':
        if direction == 'up' or direction == 'down':
            if pos[1] == 0 or pos[1] == len(content[0]) - 1 or content[pos[0]][pos[1]-1] == ' ':
                direction = 'right'
            else:
                direction = 'left'
        else:
            if pos[0] == 0 or pos[0] == len(content) - 1 or content[pos[0]+1][pos[1]] == ' ':
                direction = 'up'
            else:
                direction = 'down'
    elif location == ' ':
        keep_going = False
    elif location == '|' or location == '-':
        pass
    else:
        total_string += location
print(total_string, " in ", step_count, " steps")

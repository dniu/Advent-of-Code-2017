with open ("q11.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = [x.split(',') for x in content][0]

def func(x_dim, y_dim):
    x_moves = abs(x_dim)
    total_moves = 0
    for i in range(x_moves):
        total_moves += 1
        if y_dim > 0:
            y_dim -= 0.5
        else:
            y_dim += 0.5
        if y_dim == 0:
            return total_moves
    return total_moves+abs(y_dim)

x_dim = 0
y_dim = 0
max_dist = 0

for i in content:
    if i == "n":
        y_dim += 1
    elif i == "s":
        y_dim -= 1
    elif i == "ne":
        x_dim += 1
        y_dim += 0.5
    elif i == "sw":
        x_dim -= 1
        y_dim -= 0.5
    elif i == "nw":
        x_dim -= 1
        y_dim += 0.5
    elif i == "se":
        x_dim += 1
        y_dim -= 0.5
    else:
        pass
    curr_dist = func(x_dim, y_dim)
    if curr_dist > max_dist:
        max_dist = curr_dist
print ("You are at: ", x_dim, y_dim)


print("total distance traveled: ", func(x_dim, y_dim))
print("farthest distance: ", max_dist)

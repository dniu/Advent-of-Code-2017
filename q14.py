import q10
seen_nodes = {}
nodes = []
def get_bin(n):
    result = ""
    hashed = q10.func(n)
    for i in hashed:
        temp = int(i, 16)
        temp = format(temp, '04b')
        result += temp
    return result


def remove_group(grid, y, x):
    if (y,x) in seen_nodes or x < 0 or y < 0 or x > 127 or y > 127 or grid[y][x] == '0':
        seen_nodes[(y,x)] = 1
        return
    grid[y][x] = '0'
    seen_nodes[(y,x)] = 1
    remove_group(grid, y-1, x)
    remove_group(grid, y+1, x)
    remove_group(grid, y, x-1)
    remove_group(grid, y, x+1)
    return


def func(n):
    grid = []
    groups = 0
    #total_ones = 0
    for i in range(128):
        input_hash = n + '-' + str(i)
        input_hash = get_bin(input_hash)
        temp = []
        for j in range (128):
            if input_hash[j] == '1':
                temp.append('1')
            else:
                temp.append('0')
        #total_ones += input_hash.count('1')
        grid.append(temp)
    for y in range(128):
        for x in range(128):
            if grid[y][x] == '1':
                groups += 1
                remove_group(grid, y, x)
    
    #return total_ones
    return groups

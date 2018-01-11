with open("q24.txt") as f:
          content = f.readlines()
content = [x.strip() for x in content]
content = [x.split('/') for x in content]
doubles = []

starting = [x for x in content if x[0] == '0']
max_score = 0
max_length = 0
def get_score(connector, temp_list):
    temp_score = 0
    for i in temp_list:
        x = 0
        if i[0] == connector:
            tl = temp_list[:]
            tl.remove(i)
            if len(tl) == 0:
                x = int(i[0])
            else:
                x = int(i[0]) + get_score(i[1], tl)
            if x > temp_score:
                temp_score = x
        elif i[1] == connector:
            tl = temp_list[:]
            tl.remove(i)
            if len(tl) == 0:
                x = int(i[1])
            else:
                x = int(i[1]) + get_score(i[0], tl)
        else:
            pass
        if x > temp_score:
            temp_score = x
    return temp_score + int(connector)
"""
for i in starting:
    score = 0
    temp_content = content[:]
    temp_content.remove(i)
    score += get_score(i[1], temp_content)
    if score > max_score:
        max_score = score
print(max_score)
"""
def get_length(connector, temp_list):
    print(connector, temp_list)
    if len(temp_list) == 0:
        return 0
    score = 0
    temp_length = 0
    for i in temp_list:
        x = 0
        if i[0] == connector:
            tl = temp_list[:]
            tl.remove(i)
            x = 1 + get_length(i[1], tl)
        elif i[1] == connector:
            tl = temp_list[:]
            tl.remove(i)
            x = 1 + get_length(i[0], tl)
        else:
            pass
        print("x", x)
        if x > temp_length:
            temp_length = x
    return x

total_paths = []
for i in starting:
    score = 0
    length = 0
    path = [i]
    temp_content = content[:]
    temp_content.remove(i)
    length += get_length(i[1], temp_content)
    if length > max_length:
        print("Path:", length)
        max_length = length
    

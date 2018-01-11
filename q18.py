with open("q18.txt") as f:
          content = f.readlines()
content = [x.strip() for x in content]
content = [x.split() for x in content]
a_vals = {}
a_vals['p'] = 0
b_vals = {}
b_vals['p'] = 1
#sound = [0]
a_to_b = []
a_to_b.append([])

b_to_a = []
b_to_a.append([])

b_to_a_times = [0]
a_to_b_times = [0]
def parse(i, x, which_val):
    #print(i, x, which_val)
    cmd = x[0]
    if which_val == 'a':
        vals = a_vals
    else:
        vals = b_vals
    if len(x) == 2:
        #send or receive
        if cmd == "snd":
            if x[1] in vals:
                num = vals[x[1]]
            else:
                num = int(x[1])

            if which_val == 'a':
                #print("a sent", num)
                a_to_b_times[0] += 1
                a_to_b[0].append(num)
            else:
                #print("b sent", num)
                b_to_a_times[0] += 1
                b_to_a[0].append(num)
        if cmd == "rcv":
            if which_val == 'a':
                num = b_to_a[0].pop(0)
                #print("a received", num)
                vals[x[1]] = num
            else:
                num = a_to_b[0].pop(0)
                #print("b received", num)
                vals[x[1]] = num
    else:
        if x[1] not in vals and cmd != "jgz":
            vals[x[1]] = 0
        if x[2] in vals:
            num = vals[x[2]]
        else:
            num = int(x[2])
            
        if cmd == "set":
            vals[x[1]] = num
        elif cmd == "add":
            vals[x[1]] = vals[x[1]] + num
        elif cmd == "mul":
            vals[x[1]] = vals[x[1]] * num
        elif cmd == "mod":
            vals[x[1]] = vals[x[1]] % num
        elif cmd == "jgz":
            if x[1] in vals:
                if vals[x[1]] > 0:
                    return i + num
            else:
                if int(x[1]) > 0:
                    return i + num
        else:
            pass
    return i + 1
i = 0
j = 0
while i < len(content) or j < len(content):
    #print("i", i,a_to_b[0])
    #print("j", j,b_to_a[0])
    if i < len(content) and (len(b_to_a[0]) > 0 or content[i][0] != "rcv"):
        i = parse(i, content[i], 'a')
    elif j < len(content) and (len(a_to_b[0]) > 0 or content[j][0] != "rcv"):
        j = parse(j, content[j], 'b')
    else:
        i = len(content)
        j = len(content)

print("Program 1 sent", b_to_a_times[0], "values")

        

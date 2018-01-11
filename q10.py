real = '187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216'
a = ""
b = "AoC 2017"
c = "1,2,3"
d = "1,2,4"
def func(input_length):
    skip = 0
    lis = []
    pos = 0
    ascii_length = []
    for i in input_length:
        ascii_length.append(ord(i))
    ascii_length.append(17)
    ascii_length.append(31)
    ascii_length.append(73)
    ascii_length.append(47)
    ascii_length.append(23)
    #print(ascii_length)
    def swap(a, z):
        while a < z:
            temp = lis[a % len(lis)]
            lis[a % len(lis)] = lis[z % len(lis)]
            lis[z % len(lis)] = temp
            a += 1
            z -= 1
    for i in range(256):
        lis.append(i)

    for j in range(64):
        for i in range(len(ascii_length)):
            swap(pos, pos + int(ascii_length[i])-1)
            pos += int(ascii_length[i])
            pos += skip
            skip += 1
        
    #print(lis)
    #print(lis[0] * lis[1])
    hash_result = ""
    hash_16 = []
    for i in range(16):
        temp = 0
        for j in range(16):
            temp ^= lis[16 * i + j]
        hash_16.append(temp)
    #print(hash_16)
    for i in hash_16:
        hash_result += format(i, '02x')
    return hash_result

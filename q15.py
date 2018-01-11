factors = [16807, 48271]
vals = [618, 814]
def check_16(n):
    return bin(n % 65536)

total_matches = 0
for i in range(5000000):
    vals[0] = (vals[0] * factors[0]) % 2147483647
    vals[1] = (vals[1] * factors[1]) % 2147483647
    while vals[0] % 4 != 0:
        vals[0] = (vals[0] * factors[0]) % 2147483647
    while vals[1] % 8 != 0:
        vals[1] = (vals[1] * factors[1]) % 2147483647
    #print(vals)
    if check_16(vals[0]) == check_16(vals[1]):
        total_matches += 1
    
print("Total matches: ", total_matches)

flag = "abcdefgh"
arr = []
for i in range(0, len(flag), 2):
    print(ord(flag[i]), ord(flag[i+1]))
    print(ord(flag[i]) << 8, ord(flag[i+1]))
    temp = chr((ord(flag[i]) << 8) + ord(flag[i+1]))
    print(flag[i], flag[i+1])
    arr.append(temp)
enc = ''.join(arr)

print(enc)

arr = []
enc = open("./enc","r").read()
for char in enc:
    tmp = ord(char) >> 8
    tmp2 = ord(char) - (tmp << 8)
    arr.append(chr(tmp))
    arr.append(chr(tmp2))
    print(tmp, tmp2)
print(''.join(arr))

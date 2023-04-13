lines = open("./toascii.txt").read().splitlines()
flag = "picoCTF{"
for line in lines:
    flag += chr(int(line))
flag += "}"
print(flag)

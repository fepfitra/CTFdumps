from os import replace
import subprocess

command = "nc mercury.picoctf.net 7449"
command = command.split(" ")

output = subprocess.check_output(command).replace(b"\n", b"").decode().split(" ")

flag = ""
for char in output:
    try:
        flag += chr(int(char))
    except:
        pass

print(flag)

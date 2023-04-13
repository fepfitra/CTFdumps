import subprocess

command = "nc jupiter.challenges.picoctf.org 14291"
command = command.split(" ")

output = subprocess.check_output(command).split(b'\n')
for flag in output:
    if flag.find(b"pico") != -1:
        print(flag.decode())


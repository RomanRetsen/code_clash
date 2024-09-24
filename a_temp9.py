from pwn import *

shellcraft.sh()
print(enhex(asm(shellcraft.sh())))
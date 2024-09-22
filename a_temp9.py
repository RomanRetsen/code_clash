from pwn import *

e = ELF('/home/romio/Training_folder/C_PROJECTS/simple')

print(e.address)
print(e.entry)
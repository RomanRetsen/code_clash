import string
import socket
from fernet import Fernet
import os
import base64

'''
hostname = socket.gethostname().encode()
key = hostname[0].to_bytes(32, byteorder='big')

iv = hostname[0].to_bytes(16, byteorder='big')

with open("test_file", 'rb') as f:
    data = f.read()

cipher = Fernet(base64.urlsafe_b64encode(key))
encrypted_data = cipher.encrypt(iv + data)


with open("test_file", 'wb') as f:
    f.write(encrypted_data)

'''
letter = "P"
num = 41
try:
    key = ord(letter).to_bytes(32, byteorder='big')

    iv = ord(letter).to_bytes(16, byteorder='big')
    with open("Project-Jet.png", 'rb') as f:
    # with open("test_file", 'rb') as f:
            data = f.read()

    the_key = base64.urlsafe_b64encode(key)
    print(f"Trying {letter} with id; key_len {len(the_key)}; datalen {len(data)} ")
    cipher = Fernet(the_key)
    print(f"cipher generated {base64.urlsafe_b64encode(key)} ")
    # encrypted_data = cipher.encrypt(iv + data)
    # dencrypted_data = cipher.decrypt(iv + data)
    dencrypted_data = cipher.decrypt(data)
    print(f"data dencrypted")

    with open(f"Project-Jet_{num}", 'wb') as f:
        f.write(dencrypted_data[16:])
except:
    pass

from Crypto.Cipher import AES
from os import urandom
from operator import xor

import CBC

# Using 16-byte / 128 encryption key / iv
key = b'Sixteen byte key'
# iv = urandom(16)
iv = b'\xea\xbd\xf5\xe2}2\xafH\xf4\xediy\xdd\xc5\xe6\xeb'

def submit(input):
    prev = bytes(iv)
    print(input)

def verify(imput):
    prev = bytes(iv)
    return

# Cipher used with code in instructions
cipher = AES.new(key, AES.MODE_ECB)
new_string = submit("Hey does :admin=true?")

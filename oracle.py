
from Crypto.Cipher import AES
from os import urandom
from operator import xor
import urllib.parse

import CBC

# Using 16-byte / 128 encryption key / iv
key = b'Sixteen byte key'
# iv = urandom(16)
iv = b'\xea\xbd\xf5\xe2}2\xafH\xf4\xediy\xdd\xc5\xe6\xeb'

def submit(input : str) -> bytes:
    url_encoded = urllib.parse.quote(input, safe='')
    # print(url_encoded)

    padded = CBC.pkcs7_padding(url_encoded.encode("utf-8"), 16)
    # print(padded)
    
    prev = bytes(iv)

def verify(input : bytes) -> str:
    prev = bytes(iv)

# Cipher used with code in instructions
cipher = AES.new(key, AES.MODE_ECB)

new_string = submit("Hey does :admin=true?")
print(new_string)

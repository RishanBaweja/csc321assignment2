
from Crypto.Util.Padding import unpad
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
    mod = "userid=456; userdata=" + input + ";session-id=31337"
    url_encoded = mod.replace(";", "%3B").replace("=", "3D")
    # print(url_encoded)

    padded = CBC.pkcs7_padding(url_encoded.encode("utf-8"), 16)
    # print(padded)
    
    prev = bytes(iv)
    encrypted = b''
    while len(prev) != 0:
        encrypted += CBC.CBC_encryption(padded[:16], prev)
        print(encrypted)
        padded = padded[:16]
        prev = encrypted[16:]
    return encrypted

def verify(input : bytes) -> bool:
    decrypted = b''

    return False

# Cipher used with code in instructions
cipher = AES.new(key, AES.MODE_ECB)

new_data = submit("Hey does :admin=true?")
print(new_data)

print(verify(new_data))

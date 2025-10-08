
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
from os import urandom
from operator import xor
import urllib.parse

import CBC


def submit(input : str) -> bytes:

    #URL Encoding
    url_encoded = input.replace(";", "%3B").replace("=", "3D")

    #Tagging with prefix and suffix
    mod = "userid=456; userdata=" + url_encoded + ";session-id=31337"

    padded = CBC.pkcs7_padding(mod.encode("utf-8"), 16)

    # Typically use iv = urandom(16), but instructions said to used fixed iv
    iv = b'\xea\xbd\xf5\xe2}2\xafH\xf4\xediy\xdd\xc5\xe6\xeb'
    prev = bytes(iv)
    encrypted = b''

    while len(prev) != 0:
        ct = CBC.CBC_encryption(padded[:16], key, prev)
        encrypted += ct
        prev = ct
        padded = padded[16:]

    return encrypted

def verify(input: bytes) -> bool:
    new_cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(new_cipher.decrypt(input), AES.block_size)
    
    return b";admin=true;" in plaintext

#Global variables
# Using 16-byte / 128 encryption key
key = b'Sixteen byte key'
iv = b'\xea\xbd\xf5\xe2}2\xafH\xf4\xediy\xdd\xc5\xe6\xeb'

new_data = submit("Hey does :admin=true?")

#use xor to tamper
print(new_data)

print(verify(new_data))




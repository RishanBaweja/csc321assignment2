
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
from os import urandom
from operator import xor
import urllib.parse

import CBC


def submit(input : str) -> bytes:
    url_encoded = input.replace(";", "%3B").replace("=", "3D")
    mod = "userid=456; userdata=" + url_encoded + ";session-id=31337"
    # print(url_encoded)

    padded = CBC.pkcs7_padding(mod.encode("utf-8"), 16)
    # print(padded)
    
    prev = bytes(iv)
    encrypted = b''
    for i in range(0, len(padded), 16):
        encrypted += encrypt(padded[:16], prev)
        padded = padded[16:]
        prev = encrypted[i:]
    return encrypted

def verify(input: bytes) -> bool:
    prev = bytes(iv)
    decrypted = b''
    for i in range(0, len(input), 16):
        decrypted += decrypt(input[i:i+16], prev)
        prev = input[i:i+16]
        # print(decrypted)

    unpadded = CBC.pkcs7_strip(decrypted, 16)
    plaintext = unpadded.decode("utf-8")
    return ";admin=true;" in plaintext

def encrypt(data, cross):
    # XOR data with random bits before going through the cipher
    new_data = bytes(map(xor, data, cross))

    # Encrypt the data and then return it
    encrypted_data = cipher.encrypt(new_data)
    return encrypted_data

def decrypt(data, cross):
    decrypted_data = cipher.decrypt(data)

    new_data = bytes(map(xor, decrypted_data, cross))
    return new_data

# Using 16-byte / 128 encryption key / iv
key = b'Sixteen byte key'
# Cipher used with code in instructions
cipher = AES.new(key, AES.MODE_ECB)
# iv = urandom(16)
iv = b'\xea\xbd\xf5\xe2}2\xafH\xf4\xediy\xdd\xc5\xe6\xeb'
new_data = submit("Hey does :admin=true?")

print(new_data)

print(verify(new_data))

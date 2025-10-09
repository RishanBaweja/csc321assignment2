
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
from os import urandom
from operator import xor
import urllib.parse

import CBC


def submit(input : str) -> bytes:
    #URL Encoding
    url_encoded = input.replace(";", "%3B").replace("=", "%3D")
    #Tagging with prefix and suffix
    mod = "userid=456; userdata=" + url_encoded + ";session-id=31337"

    padded = CBC.pkcs7_padding(mod.encode("utf-8"), 16)

    # Typically use iv = urandom(16), but instructions said to used fixed iv
    iv = b'\xea\xbd\xf5\xe2}2\xafH\xf4\xediy\xdd\xc5\xe6\xeb'
    prev = bytes(iv)
    encrypted = b''
    for i in range(0, len(padded), 16):
        block = encrypt(padded[:16], prev)
        encrypted +=block
        print(f"Block {i/16}: {block}\n")
        padded = padded[16:]
        prev = encrypted[i:]
        
    return encrypted

def verify(input: bytes) -> bool:
    try:
        prev = bytes(iv)
        decrypted = b''
        for i in range(0, len(input), 16):
            block = decrypt(input[i:i+16], prev)
            print(f"DECRYPTED Block {i/16}: {block}\n")
            decrypted += block
            prev = input[i:i+16]

        #print(decrypted)
        unpadded = CBC.pkcs7_strip(decrypted, 16)
        plaintext = unpadded.decode("utf-8")
        print(f"Plaintext: {plaintext}")
    except:
        print("whoops")
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

new_data = submit("Hey friend does ?admin?true")

# use xor to tamper
#print(f"\n\nData to tamper: {new_data}\n\n")

print(verify(new_data))

barr = bytearray(new_data)
print(barr)

xor_block = ord(";") ^ ord("?")
barr[21] = barr[21] ^ xor_block
barr[27] = barr[27] ^ xor_block


print("MODIFIED,",barr)

print(verify(bytes(barr)))

# b'userid%3D456%3B userdata%3DHey does :admin)true?%3Bsession-id%3D31337\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b'
# userid%3D456%3B 
# userdata%3DHey d
# oes :admin)true?
# %3Bsession-id%3D
# 31337\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b
# There are five blocks in data without changes


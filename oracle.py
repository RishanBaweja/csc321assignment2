
from Crypto.Cipher import AES
from os import urandom
from operator import xor

def submit(sentence):
    print(sentence)

# Using 16-byte / 128 encryption key
key = b'Sixteen byte key'
randbits = urandom(16)

# Cipher used with code in instructions
cipher = AES.new(key, AES.MODE_ECB)
new_string = submit("Hey does :admin=true?")
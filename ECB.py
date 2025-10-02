from Crypto.Cipher import AES

def ECB_encryption(data):
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_EAX)

    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest()
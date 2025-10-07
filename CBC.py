from Crypto.Cipher import AES
from os import urandom
from operator import xor

def CBC_encryption(data : bytes, cross : bytes) -> bytes:
    # Using 16-byte / 128 encryption key
    key = b'Sixteen byte key'
    # randbits = urandom(16)

    # XOR data with random bits before going through the cipher
    new_data = bytes(map(xor, data, cross))

    # Cipher used with code in instructions
    cipher = AES.new(key, AES.MODE_ECB)

    # Encrypt the data and then return it
    encrypted_data = cipher.encrypt(new_data)

    # Not recommended to update value of cross in function as it only applies locally

    return encrypted_data

def pkcs7_padding(plain : bytes, size : int) -> bytes:
    byte_len = size - (len(plain) % size)
    if byte_len == 0:
        byte_len = size
    plain += bytes([byte_len]) * byte_len
    return plain

def pkcs7_strip(padded : bytes, size : int):
    return padded[:-padded[-1]]

def file_parser(input_file : str) -> None:

    with open(input_file, "rb") as i:

        #save header for reattatchment later
        header = i.read(54)

        #move file header
        i.seek(54)

        #iv created
        prev = urandom(16)

        output_file = "CBC_" +input_file
        # open output file as o and write the header
        with open(output_file, "wb") as o:
            o.write(header)

            # loop until we get to the end of the file, encrypting by 16 bytes each time
            while True:
                data = i.read(16)
                if len(data) != 16:
                    break

                encrypted = CBC_encryption(data, prev)

                # update value of prev, initially from iv then to subsequent encrypted blocks
                prev = encrypted

                o.write(encrypted)
                
            pad = 16 - (len(data) % 16)
            data += bytes([pad]) * pad

            encrypted = CBC_encryption(data, prev)
            o.write(encrypted)
        

file_parser("mustang.bmp")
file_parser("cp-logo.bmp")

# pkcs7 testing
# print("\nPKCS7 padding implementation:\n")
# Unpadded = b"Something"
# Test_len = 16
# Padded = pkcs7_padding(Unpadded, Test_len)
# print(Padded)
# Undone = pkcs7_strip(Padded, Test_len)
# print(Undone)
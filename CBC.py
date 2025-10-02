from Crypto.Cipher import AES
from os import urandom
from operator import xor

def CBC_encryption(data):
    # Using 16-byte / 128 encryption key
    key = b'Sixteen byte key'
    randbits = urandom(16)

    #xor data with random bits before going through the cipher
    new_data = bytes(map(xor, data, randbits))

    # Cipher used with code in instructions
    cipher = AES.new(key, AES.MODE_ECB)

    #encrypt the data and then return it
    encrypted_data = cipher.encrypt(new_data)

    return encrypted_data

def file_parser(input_file):

    with open(input_file, "rb") as i:

        #save header for reattatchment later
        header = i.read(54)

        #move file header
        i.seek(54)

        output_file = "CBC_" +input_file
        # open output file as o and write the header
        with open(output_file, "wb") as o:
            o.write(header)

            # loop until we get to the end of the file, encrypting by 16 bytes each time
            while True:
                data = i.read(16)
                if len(data) != 16:
                    break

                encrypted = CBC_encryption(data)

                o.write(encrypted)
                
            pad = 16 - (len(data) % 16)
            data += bytes([pad]) * pad

            encrypted = CBC_encryption(data)
            o.write(encrypted)
        

file_parser("mustang.bmp")
file_parser("cp-logo.bmp")
from Crypto.Cipher import AES
import struct

def ECB_encryption(data):
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_ECB)

    encrypted_data = cipher.encrypt(data)


    return encrypted_data

def file_parser(input_file):

    with open(input_file, "rb") as i:

        #save header for reattatchment later
        header = i.read(54)

        #move file header
        i.seek(54)

        output_file = "ECB_" +input_file
        # open output file as o and write the header
        with open(output_file, "wb") as o:
            o.write(header)

            # loop until we get to the end of the file, encrypting by 16 bytes each time
            while True:
                data = i.read(16)
                if len(data) != 16:
                    break

                encrypted = ECB_encryption(data)

                o.write(encrypted)
                
            pad = 16 - (len(data) % 16)
            data += bytes([pad]) * pad

            encrypted = ECB_encryption(data)
            o.write(encrypted)
        

file_parser("mustang.bmp")
file_parser("cp-logo.bmp")
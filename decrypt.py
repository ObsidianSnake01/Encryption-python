import os
from Crypto.Cipher import AES

# Read the AES key from the key file
key_file = open('key.txt', 'rb')
key = key_file.read()
key_file.close()

# Decrypt the file
def decrypt_file(key, input_file, output_file):
  # Read the nonce, tag, and ciphertext from the input file
  nonce, tag, ciphertext = [ input_file.read(x) for x in (16, 16, -1) ]

  # Create an AES cipher and decrypt the data
  cipher = AES.new(key, AES.MODE_EAX, nonce)
  data = cipher.decrypt_and_verify(ciphertext, tag)

  # Write the decrypted data to the output file
  output_file.write(data)

# Prompt the user for the input and output filenames

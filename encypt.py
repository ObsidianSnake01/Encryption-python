import os
import random
from Crypto.Cipher import AES

# AES key size must be either 16, 24, or 32 bytes long
KEY_SIZE = 32

# Create a random AES key
def generate_key():
  return os.urandom(KEY_SIZE)

# Encrypt the file
def encrypt_file(key, input_file, output_file):
  # Read the input file and pad it with random bytes
  # so that its length is a multiple of 16 (AES block size)
  data = input_file.read()
  padding_length = AES.block_size - (len(data) % AES.block_size)
  data += os.urandom(padding_length)

  # Create an AES cipher and encrypt the data
  cipher = AES.new(key, AES.MODE_EAX)
  ciphertext, tag = cipher.encrypt_and_digest(data)

  # Write the encrypted data to the output file
  output_file.write(cipher.nonce)
  output_file.write(tag)
  output_file.write(ciphertext)

# Prompt the user for the input and output filenames
input_filename = input('Enter the name of the file to encrypt: ')
output_filename = input('Enter the name of the output file: ')

# Generate an AES key and save it to a file
key = generate_key()
key_file = open('key.txt', 'wb')
key_file.write(key)
key_file.close()

# Open the input and output files
input_file = open(input_filename, 'rb')
output_file = open(output_filename, 'wb')

# Encrypt the input file and write it to the output file
encrypt_file(key, input_file, output_file)

# Close the files
input_file.close()
output_file.close()

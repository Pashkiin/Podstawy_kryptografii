import os
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter
import random

# Define file sizes in bytes
file_sizes = [10**6, 10**7, 10**8]  # 1MB, 10MB, 100MB

#Define file names
file_names = ['rzepka.txt', 'hamlet.txt']

# Define modes
modes = ['ECB', 'CBC', 'OFB', 'CFB', 'CTR']

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def encrypt_cbc(plain_text, key, iv):
    cipher = AES.new(key, AES.MODE_ECB)  # We will use this for the actual encryption
    blocks = [plain_text[i:i+16] for i in range(0, len(plain_text), 16)]  # Break the plaintext into 16-byte blocks
    encrypted_blocks = []
    previous_block = iv
    for block in blocks:
        # XOR the current block with the previous ciphertext block (or IV for the first block), then encrypt it
        encrypted_block = cipher.encrypt(xor_bytes(pad(block, AES.block_size), previous_block))
        encrypted_blocks.append(encrypted_block)
        previous_block = encrypted_block
    return b''.join(encrypted_blocks)

def decrypt_cbc(cipher_text, key, iv):
    cipher = AES.new(key, AES.MODE_ECB)  # We will use this for the actual decryption
    blocks = [cipher_text[i:i+16] for i in range(0, len(cipher_text), 16)]  # Break the ciphertext into 16-byte blocks
    decrypted_blocks = []
    previous_block = iv
    for block in blocks:
        # Decrypt the current block, then XOR it with the previous ciphertext block (or IV for the first block)
        decrypted_block = xor_bytes(cipher.decrypt(block), previous_block)
        decrypted_blocks.append(decrypted_block)
        previous_block = block
    return unpad(b''.join(decrypted_blocks), AES.block_size)

def flip_random_bit_in_ciphertext(ciphertext):
    # Convert the ciphertext to a bytearray
    data = bytearray(ciphertext)

    # Choose a random byte in the first 16 bytes (128 bits) and a random bit in that byte
    byte_index = random.randint(0, min(15, len(data) - 1))
    bit_index = random.randint(0, 7)

    # Flip the chosen bit
    data[byte_index] ^= (1 << bit_index)

    print(f"Flipped bit {bit_index} in byte {byte_index}")

    return bytes(data)

    
def count_differences(file1_path, file2_path):
    # Open both files in binary mode
    with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2:
        # Read the content of each file
        file1_content = file1.read()
        file2_content = file2.read()

    # Compare the characters from both files
    differences = sum(c1 != c2 for c1, c2 in zip(file1_content, file2_content))

    # Check if one file has more characters than the other
    if len(file1_content) > len(file2_content):
        differences += len(file1_content) - len(file2_content)
    elif len(file1_content) < len(file2_content):
        differences += len(file2_content) - len(file1_content)

    return differences

# Function to generate a random file
def generate_file(size= None, file_path=None):
    if file_path is None:
        with open('testfile', 'wb') as f:
            f.write(get_random_bytes(size))
        return 'testfile'
    else:
        return file_path

# Function to encrypt and decrypt a file, and measure time
def measure_time(mode, file_size=None, file_path=None, error=False):
    file_path = generate_file(file_size, file_path)
    key = get_random_bytes(16)
    initial = get_random_bytes(16)
    encrypted_file_path = f"{file_path}_encrypted"
    decrypted_file_path = f"{file_path}_decrypted{mode}"

    # Measure encryption time
    if mode == 'ECB':
        cipher = AES.new(key, getattr(AES, f'MODE_{mode}'))  # No IV for ECB
    elif mode == 'CBC':
        ciphertext = encrypt_cbc(open(file_path, 'rb').read(), key, initial)
    elif mode == 'CTR':
        ctr = Counter.new(128, initial_value=1)  # Create a counter for CTR
        cipher = AES.new(key, getattr(AES, f'MODE_{mode}'), counter=ctr)  # Use counter for CTR
    else:
        cipher = AES.new(key, getattr(AES, f'MODE_{mode}'), iv=initial)  # Use IV for other modes
    start = time.time()
    if mode != 'CBC':
        with open(file_path, 'rb') as f:
            ciphertext = cipher.encrypt(pad(f.read(), AES.block_size))
    encryption_time = time.time() - start

    # Save encrypted file
    with open(encrypted_file_path, 'wb') as f:
        f.write(ciphertext)

    # Flip a random bit in the encrypted file if true
    if error:
        ciphertext = flip_random_bit_in_ciphertext(ciphertext)

    # Measure decryption time
    if mode == 'ECB':
        cipher = AES.new(key, getattr(AES, f'MODE_{mode}'))  # No IV for ECB
    elif mode == 'CBC':
        decrypted_content = decrypt_cbc(ciphertext, key, initial)
    elif mode == 'CTR':
        ctr = Counter.new(128, initial_value=1)  # Create a counter for CTR
        cipher = AES.new(key, getattr(AES, f'MODE_{mode}'), counter=ctr)  # Use counter for CTR
    else:
        cipher = AES.new(key, getattr(AES, f'MODE_{mode}'), iv=initial)  # Use IV for other modes
    start = time.time()
    if mode != 'CBC':
        decrypted_content = unpad(cipher.decrypt(ciphertext), AES.block_size)
    decryption_time = time.time() - start

    # Save decrypted file
    with open(decrypted_file_path, 'wb') as f:
        f.write(decrypted_content)

    # Check if the decrypted file is the same as the original file
    if error:
        differences = count_differences(file_path, decrypted_file_path)
        print(f"{mode} Number of differences: {differences}")
  
    return encryption_time, decryption_time

# Loop over each file size and each mode
results = {}
# for size in file_sizes:
#     for mode in modes:
#         results[(size, mode)] = measure_time(mode, size)

# Print results
# for (size, mode), (encryption_time, decryption_time) in results.items():
#     print(f'File size: {size/1000000} MB, Mode: {mode}, Encryption time: {encryption_time} seconds, Decryption time: {decryption_time} seconds')

for file in file_names:
        for mode in modes:
            results[(file,mode)] = measure_time(mode = mode, file_path=file,error=True)

for (file, mode), (encryption_time, decryption_time) in results.items():
    print(f'File: {file}, Mode: {mode}, Encryption time: {encryption_time} seconds, Decryption time: {decryption_time} seconds')


import hashlib
import time
import itertools
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def hash_data(data, algorithm):
    start_time = time.time()
    if algorithm == 'md5':
        hashed_data = hashlib.md5(data.encode()).hexdigest()
    elif algorithm == 'sha1':
        hashed_data = hashlib.sha1(data.encode()).hexdigest()
    elif algorithm == 'sha224':
        hashed_data = hashlib.sha224(data.encode()).hexdigest()
    elif algorithm == 'sha256':
        hashed_data = hashlib.sha256(data.encode()).hexdigest()
    elif algorithm == 'sha384':
        hashed_data = hashlib.sha384(data.encode()).hexdigest()
    elif algorithm == 'sha512':
        hashed_data = hashlib.sha512(data.encode()).hexdigest()
    elif algorithm == 'sha3_224':
        hashed_data = hashlib.sha3_224(data.encode()).hexdigest()
    elif algorithm == 'sha3_256':
        hashed_data = hashlib.sha3_256(data.encode()).hexdigest()
    elif algorithm == 'sha3_384':
        hashed_data = hashlib.sha3_384(data.encode()).hexdigest()
    elif algorithm == 'sha3_512':
        hashed_data = hashlib.sha3_512(data.encode()).hexdigest()
    else:
        return "Invalid algorithm"
    end_time = time.time()
    elapsed_time = end_time - start_time
    return hashed_data, elapsed_time

def check_sac(algorithm):
    input_data = 'abcd'
    original_hash, _ = hash_data(input_data, algorithm)
    for i in range(len(input_data)):
        flipped_data = input_data[:i] + chr(ord(input_data[i]) ^ 1) + input_data[i+1:]
        flipped_hash, _ = hash_data(flipped_data, algorithm)
        diff_count = sum(a != b for a, b in zip(original_hash, flipped_hash))
        if diff_count / len(original_hash) < 0.5:
            return False
    return True

# Get user input
data = input("Enter data length: ")
data = generate_random_string(int(data))
print(f"Data: {data}")
algorithms = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512']
for algorithm in algorithms:
    hashed_data, elapsed_time = hash_data(data, algorithm)
    print(f"Algorithm: {algorithm}, Hash: {hashed_data}, Time: {elapsed_time} seconds")
    print(f"SAC criterion met: {check_sac(algorithm)}")
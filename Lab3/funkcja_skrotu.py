import hashlib
import time
import random
import string
import random
import string
from collections import defaultdict

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def check_md5_collisions(num_passwords, password_length, bit_lengths,algorithm):
    # Generate random passwords
    passwords = [generate_random_string(password_length) for _ in range(num_passwords)]

    # Hash passwords and keep track of collisions
    collisions = {bit_length: defaultdict(int) for bit_length in bit_lengths}
    for password in passwords:
        hashed_password = hash_data(password, algorithm)[0]
        hashed_password_bin = bin(int(hashed_password, 16))[2:].zfill(128)  # Convert to binary
        for bit_length in bit_lengths:
            hashed_password_bits = hashed_password_bin[:bit_length]
            collisions[bit_length][hashed_password_bits] += 1

    # Count collisions
    collision_counts = {bit_length: sum(1 for count in bit_counts.values() if count > 1)
                        for bit_length, bit_counts in collisions.items()}
    return collision_counts

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
    input_data = 'abcdefghij'
    original_hash, _ = hash_data(input_data, algorithm)
    for i in range(len(input_data)):
        flipped_data = input_data[:i] + chr(ord(input_data[i]) ^ 1) + input_data[i+1:]
        flipped_hash, _ = hash_data(flipped_data, algorithm)
        original_bits = ''.join(format(ord(x), 'b') for x in original_hash)
        flipped_bits = ''.join(format(ord(x), 'b') for x in flipped_hash)
        diff_count = sum(a != b for a, b in zip(original_bits, flipped_bits))
        print(f"SAC diff count: {diff_count/len(original_bits)}")
        if diff_count / len(original_bits) > 0.46 or diff_count / len(original_bits) < 0.54:
            return True
    return False

# Get user input
data = input("Enter data length: ")
data = generate_random_string(int(data))
#print(f"Data: {data}")
algorithms = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512']
bit_lengths = [12, 20, 50, 100]
for algorithm in algorithms:
    hashed_data, elapsed_time = hash_data(data, algorithm)
    #print(f"Algorithm: {algorithm}, Hash: {hashed_data} bytes ,\n Time: {elapsed_time} seconds")
    print(f"Algorithm: {algorithm}, SAC criterion met: {check_sac(algorithm)}")
collision_counts = check_md5_collisions(10000, 10, bit_lengths, 'md5')
#print("Collisions for md5 algorithm",collision_counts)

# Pytanie 4 - Funkcja MD5 nie jest uznawana juz za bezpieczna, poniewaz udalo sie znalezc wiele kolizji dla tej funkcji skrotu.
#Jest ona używana do spraqwdzania integralności plików, ale nie do haszowania haseł. Rekomendowane jest używanie nowszych i bezpieczniejszych algorytmow takich jak SHA-256 czy SHA-512.


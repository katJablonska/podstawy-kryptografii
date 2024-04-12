import hashlib
import time
import random

def generate_hashes(input_text):
    hash_algorithms = {
        "MD5": hashlib.md5,
        "SHA-1": hashlib.sha1,
        "SHA-256": hashlib.sha256,
        "SHA3-512": hashlib.sha3_512
    }

    hashes = {}
    for algorithm_name, algorithm in hash_algorithms.items():
        start_time = time.time()
        hash_obj = algorithm()
        hash_obj.update(input_text.encode('utf-8'))
        hashed_value = hash_obj.hexdigest()
        execution_time = time.time() - start_time
        hashes[algorithm_name] = {"hash": hashed_value, "time": execution_time}
    return hashes

input_data = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Hello World!",
    "1234567890",
    "gepard",
    "a"
]

# Generowanie skrótów i pomiar czasu
for data in input_data:
    print(f"Input: {data}")
    hashes = generate_hashes(data)
    for algorithm_name, info in hashes.items():
        print(f"{algorithm_name}: {info['hash']} (Time: {info['time']:.6f} sec)")
    print()

word = "gprd"
md5_hash = generate_hashes(word)["MD5"]["hash"]
print(f"MD5 hash for '{word}': {md5_hash}")

# Badanie kolizji na pierwszych 12 bitach skrótu
# wygeneruj 1000 losowych wiadomosci, wygeneruj ich skróty i wtedy sprawdz kolizje
def check_collisions():
    to_check = 12
    tests = 1_000
    collision_count = 0

    base_hash = hashlib.sha256(rand_str(30).encode()).hexdigest()
    base_hash_bits = str_to_bits(base_hash)

    for i in range(tests):
        s = rand_str(30)
        s_hash = hashlib.sha256(s.encode()).hexdigest()
        s_hash_bits = str_to_bits(s_hash)
        if s_hash_bits[:to_check] == base_hash_bits[:to_check]:
            collision_count += 1

    print("Collision probability in first 12 bits:", collision_count / tests)

def rand_str(length):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length))

def str_to_bits(s):
    return ''.join(format(ord(c), '08b') for c in s)

check_collisions()

# SAC
def check_sac(hash_algorithm):
    text1 = generate_hashes("co z ala ktora ma kota")["SHA-256"]["hash"]
    text2 = generate_hashes("do z ala ktora ma kota")["SHA-256"]["hash"]

    hashed_text1 = bin(int(text1, 16)).removeprefix("0b").zfill(256)
    hashed_text2 = bin(int(text2, 16)).removeprefix("0b").zfill(256)

    count = 0
    for x in range(256):
        if hashed_text1[x] == hashed_text2[x]:
            count += 1

    return round(count / len(hashed_text1), 4)


sac_score = check_sac("SHA-256")
print(f"SAC score for SHA-256: {sac_score}")

import random

def is_prime(n):
    if n > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(n/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False

def generate_prime():
    while True:
        p = random.randint(1000, 9999)  # Liczby 4-cyfrowe
        if p % 4 == 3 and is_prime(p):
            return p

def greatest_common_divider(a, b):
    while b:
        a, b = b, a % b
    return a

# wybranie w sposób losowy takiej liczby x, że x i N są względnie pierwze
def generate_x(N):
    while True:
        x = random.randint(2, N - 1)
        if greatest_common_divider(x, N) == 1:
            return x

# wyznaczenie wartości pierwotnej generatora
def generate_x0(N):
    x = generate_x(N)
    x0 = (x**2) % N
    return x0

def lsb(x):
    return x & 1

def generate_next_x(x, N):
    return (x**2) % N

def generate_key(N, length):
    generator = generate_x0(N)
    key = ""
    for i in range(length):
        generator = generate_next_x(generator, N)
        key += str(lsb(generator))
    return key

# Main program
p = generate_prime()
q = generate_prime()
N = p * q
x = generate_x(N)
x0 = generate_x0(N)

length = 20000
key = generate_key(N, length)

# Zapis klucza do pliku
with open("output.txt", "w") as file:
    file.write(key)

print("Saved to file: output.txt")

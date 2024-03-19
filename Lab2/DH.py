import random


# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Function to find the closest prime number to a given number
def closest_prime(n):
    if is_prime(n):
        return n
    while not is_prime(n):
        n -= 1
    return n


# Function to find a primitive root for a given number n
def find_primitive(n):
    for r in range(1, n):
        li = []
        for x in range(n - 1):
            val = (r ** x) % n
            if val not in li:
                li.append(val)
            else:
                break
        if len(li) == n - 1:
            return r


# Function to perform the Diffie-Hellman key exchange
def diffie_hellman():
    # Publicly known numbers
    print("Podaj 4-cyfrowa wartość p")
    p = int(input())
    while p < 1000 or p > 9999:
        print("Liczba p nie jest 4-cyfrowa, podaj poprawna wartość p")
        p = int(input())
    if not is_prime(p):
        print("Liczba p nie jest liczbą pierwszą")
        p = closest_prime(p)
        print("Najbliższa liczba pierwsza to: ", p)
    g = find_primitive(p)  # A primitive root of p

    # Asia generates a private key a
    a = random.randint(999, p)
    # Asia calculates her public key A
    A = (g ** a) % p
    print("Wartość A to: ", A)

    # Bartek generates a private key b
    b = random.randint(999, p)
    # Bartek calculates his public key B
    B = (g ** b) % p
    print("Wartość B to: ", B)

    # Asia and Bartek exchange their public keys and calculate the shared secret
    shared_secret_Asia = (B ** a) % p
    shared_secret_Bartek = (A ** b) % p

    # Both shared secrets should be equal
    assert shared_secret_Asia == shared_secret_Bartek

    return shared_secret_Asia


def main():
    session_key = diffie_hellman()
    print("Wspólny sekret to: ", session_key)

if __name__ == "__main__":
    main()

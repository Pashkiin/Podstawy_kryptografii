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


# Function to calculate the Greatest Common Divisor of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Function to generate the public key exponent
def generate_e(phi, mine):
    for e in range(mine, phi):
        if gcd(e, phi) == 1 and is_prime(e):
            return e
    return -1


# Function to generate the private key exponent
def generate_d(e, phi):
    d = 1
    while (d * e) % phi != 1:
        d += 1
    return d


# Main function to run the RSA algorithm
def main():
    print("Podaj p i q ktore sa liczbami pierwszymi")
    p = int(input())
    if not is_prime(p):
        print("Liczba p nie jest liczbą pierwszą")
        p = closest_prime(p)
        print("Najbliższa liczba pierwsza to: ", p)
    q = int(input())
    if not is_prime(q):
        print("Liczba q nie jest liczbą pierwszą")
        q = closest_prime(q)
        print("Najbliższa liczba pierwsza to: ", q)
    n = p * q
    print("n = ", n)
    phi = (p - 1) * (q - 1)
    print("phi = ", phi)
    print("Podaj mininalna wartość e")
    mind = int(input())
    e = generate_e(phi, mind)
    print("e = ", e)
    d = generate_d(e, phi)
    print("d = ", d)
    print("Sprawdzenie: (e * d - 1) % phi = ", (e * d - 1) % phi)
    print("Klucz publiczny: (", e, ",", n, ")")
    print("Klucz prywatny: (", d, ",", n, ")")
    print("Podaj wiadomość do zaszyfrowania")
    message = input()
    message_parts = [ord(char) for char in message]
    encrypted_message = []
    decrypted_message = []
    for part in message_parts:
        encrypted = pow(part, e, n)
        encrypted_message.append(encrypted)
        decrypted = pow(encrypted, d, n)
        decrypted_message.append(chr(decrypted))
    print("Zaszyfrowana wiadomość: ", encrypted_message)
    print("Odszyfrowana wiadomość: ", ''.join(decrypted_message))


if __name__ == "__main__":
    main()

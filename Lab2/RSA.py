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

def closest_prime(n):
    if is_prime(n):
        return n
    while not is_prime(n):
        n -= 1
    return n
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def generate_e(phi, min):
    for e in range(min, phi):
        if gcd(e, phi) == 1 and is_prime(e):
            return e
    return -1

def generate_d(e, phi):
    d = 0
    while (d * e) % phi != 1:
        d += 1
    return d
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
    message = 78987654321123456789876543212345678987654321234567
    message_parts = [int(i) for i in message.split()]
    encrypted_message = []
    decrypted_message = []
    for part in message_parts:
        encrypted = (part ** e) % n
        encrypted_message.append(encrypted)
        decrypted = (encrypted ** d) % n
        decrypted_message.append(decrypted)
    encrypted = (message ** e) % n
    print("Zaszyfrowana wiadomość: ", encrypted)
    decrypted = (encrypted ** d) % n
    print("Odszyfrowana wiadomość: ", decrypted)



if __name__ == "__main__":
    main()
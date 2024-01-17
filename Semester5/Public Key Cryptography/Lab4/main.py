import random


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime(min_val, max_val):
    primes = [i for i in range(min_val, max_val) if is_prime(i)]
    return random.choice(primes)


def mod_exp(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m
    return result


def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('The modular inverse does not exist')
    else:
        return x % m


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x


def generate_keys():
    p = generate_prime(1000, 10000)
    g = random.randint(1, p - 1)
    a = random.randint(1, p - 2)
    public_key = (p, g, mod_exp(g, a, p))
    private_key = a
    return public_key, private_key


def encrypt(plaintext, public_key):
    p, g, ga = public_key
    for char in plaintext:
        if char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
            raise ValueError(f"Invalid character in plaintext: {char}")

    ciphertext = []
    for char in plaintext:
        m = ord(char) % p
        k = random.randint(1, p - 2)
        alpha = mod_exp(g, k, p)
        beta = (m * mod_exp(ga, k, p)) % p
        ciphertext.append((alpha, beta))
    return ciphertext


def decrypt(ciphertext, public_key, private_key):
    p, _, ga = public_key
    a = private_key
    decrypted_chars = [chr((mod_inverse(mod_exp(alpha, a, p), p) * beta) % p) for alpha, beta in ciphertext]

    for char in decrypted_chars:
        if char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ":
            raise ValueError(f"Invalid character in decrypted plaintext: {char}")

    return ''.join(decrypted_chars)


# Example usage
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
plaintext = "HELLO"
print(f'Original Plaintext: {plaintext}')

public_key, private_key = generate_keys()
print(f'Public Key: {public_key}')
print(f'Private Key: {private_key}')

ciphertext = encrypt(plaintext, public_key)
print(f'Ciphertext: {ciphertext}')

decrypted_plaintext = decrypt(ciphertext, public_key, private_key)
print(f'Decrypted Plaintext: {decrypted_plaintext}')
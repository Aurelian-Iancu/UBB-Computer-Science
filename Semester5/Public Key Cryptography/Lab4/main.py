import random

ALPHABET = ' abcdefghijklmnopqrstuvwxyz'
CHUNK_LENGTH = 3
ALPHABET_LENGTH = len(ALPHABET)


def validate(message):
    for char in message:
        if char not in ALPHABET:
            return False
    return True


def get_int_less_than(p):
    return random.randint(1, p - 2)


def sieve(bound):
    ans = []
    marked = [False for _ in range(bound + 1)]
    for i in range(2, bound + 1):
        if not marked[i]:
            ans.append(i)
            for j in range(i + i, bound + 1, i):
                marked[j] = True
    return ans[10000:]


def get_random_prime(bound):
    primes = sieve(bound)
    return random.choice(primes)


def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

def generators(n):
    gens = []
    for g in range(2, n):
        if gcd(g, n) == 1:
            gens.append(g)
    return gens


def get_random_generator(n):
    return random.choice(generators(n))


def modular_exp(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    # bit shifting is safer for large numbers, when possible
    while y > 0:
        if (y & 1) == 1:
            res = res * x % p
        y = y >> 1  # y = y//2
        x = x * x % p

    return res


def keys_generator():
    p = get_random_prime(10 ** 7)
    print("generated prime is=" + str(p))
    g = get_random_generator(p)
    print("generator g is=" + str(g))
    a = get_int_less_than(p)  # private key
    ga = modular_exp(g, a, p)
    print("g^a is=" + str(ga))
    public_key = (p, g, ga)
    return public_key, a


def convert_characters_to_number(characters):
    number = 0
    power = 1
    for char in reversed(characters):
        number += power * (ALPHABET.find(char) + 1)
        power *= (ALPHABET_LENGTH+1)
    return number


def convert_number_to_characters(number):
    characters = ""
    while number:
        characters = ALPHABET[number % (ALPHABET_LENGTH+1) - 1]+characters
        number//=(ALPHABET_LENGTH+1)
    return characters


def generate_random_text():
    tests = []
    for i in range(25):
        length = random.randint(5, 10)
        message = ""
        for _ in range(length):
            message += random.choice(ALPHABET)
        tests.append(message)
    return tests


def test():
    test_cases = generate_random_text()
    print(test_cases)
    public_key, private_key = keys_generator()
    print("public key=" + str(public_key))
    print("private key=" + str(private_key))
    p = public_key[0]
    g = public_key[1]
    ga = public_key[2]
    a = private_key
    for test_message in test_cases:

        decrypted_text = ""
        chunks = [test_message[i:i + CHUNK_LENGTH] for i in range(0, len(test_message), CHUNK_LENGTH)]
        for c in chunks:
            nr = convert_characters_to_number(c)

            k = get_int_less_than(p)
            alpha = modular_exp(g, k, p)
            beta = nr * modular_exp(ga, k, p) % p

            decrypted_number = modular_exp(alpha, p - 1 - a, p) * beta % p
            decrypted_text += convert_number_to_characters(decrypted_number)

        print(test_message, decrypted_text)
        assert decrypted_text == test_message


def main():

    print("el gamal tests starting")
    test()
    print("el gamal tests passed")

    initial_message = "fara"
    print("-----------------------------------------")
    print("message:" + initial_message)

    if not validate(initial_message):
        print("Invalid characters in input message. Please only use lowercase alphabet and spaces.")
        assert False

    public_key, private_key = keys_generator()
    print("public key=" + str(public_key))
    print("private key=" + str(private_key))
    p = public_key[0]
    g = public_key[1]
    ga = public_key[2]
    a = private_key

    decrypted_text = ""
    chunks = [initial_message[i:i + CHUNK_LENGTH] for i in range(0, len(initial_message), CHUNK_LENGTH)]
    for c in chunks:
        nr = convert_characters_to_number(c)
        k = get_int_less_than(p)
        alpha = modular_exp(g, k, p)
        beta = nr * modular_exp(ga, k, p) % p

        decrypted_number = modular_exp(alpha, p - 1 - a, p) * beta % p
        decrypted_text += convert_number_to_characters(decrypted_number)

    print("decrypted message:" + decrypted_text)
    assert decrypted_text == initial_message

main()

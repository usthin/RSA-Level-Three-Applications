# rsa_utils.py

import hashlib


# --------- BASIC RSA ---------
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y


def mod_inverse(e, phi):
    gcd_val, x, _ = extended_gcd(e, phi)
    return x % phi


def generate_keys(p=61, q=53):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 17
    d = mod_inverse(e, phi)

    return (n, e), (n, d)


# --------- HASHING ---------
def hash_message(message):
    return int(hashlib.sha256(message.encode()).hexdigest(), 16)


# --------- SIGN ---------
def sign(message, private_key):
    n, d = private_key
    h = hash_message(message)
    signature = pow(h, d, n)
    return signature


# --------- VERIFY ---------
def verify(message, signature, public_key):
    n, e = public_key

    h_original = hash_message(message)
    h_from_signature = pow(signature, e, n)

    return h_original == h_from_signature
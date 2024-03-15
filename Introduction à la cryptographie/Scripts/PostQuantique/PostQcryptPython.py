#!/usr/bin/env python3
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hmac
import os
import pyspx.shake_128f as sphincs
import secrets
from getpass import getpass

def generate_key_iv(password, salt, iterations=100000):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt,
        iterations=iterations,
        length=32,
        backend=default_backend()
    )
    key = kdf.derive(password)
    iv = os.urandom(16)
    return key, iv

def generate_key_pair():
    seed = secrets.token_bytes(48)
    public_key, private_key = sphincs.generate_keypair(seed)
    return public_key, private_key

def encrypt_and_sign_message(message, key, iv, private_key):
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message) + encryptor.finalize()

    h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
    h.update(ciphertext)
    tag = h.finalize()

    signature = sphincs.sign(ciphertext, private_key)

    return ciphertext, tag, signature

def verify_and_decrypt_message(ciphertext, tag, signature, key, iv, public_key):
    valid = sphincs.verify(ciphertext, signature, public_key)
    print("Signature valid?", valid)

    h = hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
    h.update(ciphertext)
    h.verify(tag)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

def main():
    # Entrée utilisateur
    message_to_encrypt = input("Entrez votre message à chiffrer : ").encode('utf-8')
    password = getpass("Entrez votre mot de passe : ").encode('utf-8')

    # Génération des clés
    salt = os.urandom(16)
    key, iv = generate_key_iv(password, salt)
    public_key, private_key = generate_key_pair()

    # Chiffrement, signature et affichage du résultat
    encrypted_message, tag, signature = encrypt_and_sign_message(message_to_encrypt, key, iv, private_key)
    print(f"Message chiffré: {encrypted_message.hex()}")
    print(f"Signature: {signature.hex()}")

    # Vérification et déchiffrement
    decrypted_message = verify_and_decrypt_message(encrypted_message, tag, signature, key, iv, public_key)
    print(f"Message déchiffré: {decrypted_message.decode('utf-8')}")

if __name__ == "__main__":
    main()
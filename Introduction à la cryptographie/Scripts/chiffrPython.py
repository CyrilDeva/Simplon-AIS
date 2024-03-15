from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def generer_cle_asymetrique():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def signer_chiffrer(message, private_key, public_key):
    # Chiffrer le message avec la clé publique
    message_chiffre = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Signer le message chiffré avec la clé privée
    signature = private_key.sign(
        message_chiffre,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    return message_chiffre, signature

# Entrée utilisateur
message_original = input("Entrez votre message : ")

# Générer une paire de clés
private_key, public_key = generer_cle_asymetrique()

# Signer et chiffrer le message
message_original_bytes = message_original.encode()
message_chiffre, signature = signer_chiffrer(message_original_bytes, private_key, public_key)

# Convertir les clés en chaînes de caractères
public_key_str = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
).decode()

private_key_str = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
).decode()

# Enregistrer les résultats dans des fichiers à la racine du script
with open("public_key.pem", "wb") as fichier_public_key:
    fichier_public_key.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

with open("private_key.pem", "wb") as fichier_private_key:
    fichier_private_key.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("message_chiffre.bin", "wb") as fichier_message_chiffre:
    fichier_message_chiffre.write(message_chiffre)

with open("signature.bin", "wb") as fichier_signature:
    fichier_signature.write(signature)

# Afficher les résultats
print("Message original:", message_original)
print("Message chiffré:", message_chiffre.hex())
print("Clé publique:\n", public_key_str)
print("Clé privée:\n", private_key_str)
print("Signature:", signature.hex())

# Attendre que l'utilisateur appuie sur une touche avant de fermer la fenêtre
input("Appuyez sur Entrée pour quitter...")

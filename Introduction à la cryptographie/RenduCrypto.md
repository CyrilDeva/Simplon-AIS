# Cryptographie

# Générer et partager une clé de chiffrement AES256 ainsi que les IV avec le destinataire
![Powershell output](https://raw.githubusercontent.com/CyrilDeva/Simplon-AIS/main/Introduction%20%C3%A0%20la%20cryptographie/Scrennshots/scriptPowershell.png?raw=true)
![Powershell2 output](https://raw.githubusercontent.com/CyrilDeva/Simplon-AIS/main/Introduction%20%C3%A0%20la%20cryptographie/Scrennshots/scriptPowershell2.png?raw=true)


## Comment générer une clé de chiffrement de manière sure ? Quel est le risque si les IV sont toujours les mêmes ?

- Utilisez des bibliothèques de chiffrement bien établies dans des langages sécurisés comme Python avec la bibliothèque cryptography.
- Les clés doivent être générées avec un générateur de nombres aléatoires cryptographiquement sécurisé.
- Les IV ne doivent jamais être constants. Le réutiliser avec la même clé compromet la sécurité, car cela peut conduire à des attaques par analyse fréquentielle.

## Comment pourrait-on s'assurer de l'intégrité du message ? Ajouter cette fonctionnalité à l'aide d'un script ou d'un outil en CLI.
- En verifiant le HASH

## Comment pourrait-on s'assurer de l'authenticité de ce message ? Ajouter cette fonctionnalité à l'aide d'un script ou d'un outil en CLI.
- En ajoutant une signature

### Script de cryptage en python

````python
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
````

### Script de decryptage en python

````python
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

def charger_cle_privee():
    """Charge la clé privée depuis le fichier."""
    with open("private_key.pem", "rb") as fichier_cle_privee:
        cle_privee = serialization.load_pem_private_key(
            fichier_cle_privee.read(),
            password=None,
            backend=default_backend()
        )
    return cle_privee

def dechiffrer_et_verifier(message_chiffre, signature, cle_privee, cle_publique):
    """Déchiffre et vérifie le message en utilisant la clé privée et la clé publique."""
    try:
        # Vérifier la signature
        cle_publique.verify(
            signature,
            message_chiffre,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        # Déchiffrer le message
        message_original = cle_privee.decrypt(
            message_chiffre,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return True, message_original.decode()

    except Exception as e:
        return False, str(e)

# Charger la clé privée
cle_privee = charger_cle_privee()

# Charger la clé publique
with open("public_key.pem", "rb") as fichier_cle_publique:
    cle_publique = serialization.load_pem_public_key(
        fichier_cle_publique.read(),
        backend=default_backend()
    )

# Entrée utilisateur : message chiffré et signature
message_chiffre_hex = input("Entrez le message chiffré (en hexadécimal) : ")
message_chiffre = bytes.fromhex(message_chiffre_hex)

signature_hex = input("Entrez la signature (en hexadécimal) : ")
signature = bytes.fromhex(signature_hex)

# Déchiffrer et vérifier le message
signature_correcte, message_original = dechiffrer_et_verifier(message_chiffre, signature, cle_privee, cle_publique)

# Afficher le résultat
if signature_correcte:
    print("Signature correcte. Message déchiffré :", message_original)
else:
    print("Signature incorrecte :", message_original)


# Attendre que l'utilisateur appuie sur une touche avant de fermer la fenêtre
input("Appuyez sur Entrée pour quitter...")
````

#### Output
![script Python output](https://raw.githubusercontent.com/CyrilDeva/Simplon-AIS/main/Introduction%20%C3%A0%20la%20cryptographie/Scrennshots/scriptPython.png?raw=true)
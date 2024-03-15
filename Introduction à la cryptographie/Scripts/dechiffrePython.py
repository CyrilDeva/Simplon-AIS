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
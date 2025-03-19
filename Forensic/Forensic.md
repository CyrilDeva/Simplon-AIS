# Rapport d'Investigation

**Auteur :** Cyril D.  
**Date :** 19/03/2024  

## Objectifs
- Retracer la timeline des événements.
- Déterminer si le serveur a été compromis.
- Fournir des recommandations.

## Analyse des Preuves

### Hash SHA256 des éléments transmis
- infected.zip : 3D24ABC43FD9C1F7A35F1FA92C18E0E756887FCDD1B5F4BDD63309D6035D7333

### Chronologie des Événements
| Date & Heure         | Source (Log) | Événement                               | Détails complémentaires                  |
|----------------------|--------------|-----------------------------------------|------------------------------------------|
| N/A  | Server.log     | Vol de token      | via la request POST {"user":"'or '1'='1", "passwd":"'or '1'='1" dans https://192.168.42.129:3000/Login|
| N/A  | Server.log       | Lance une commande whoami      | via GET https://192.168.42.129:3000/LocalDNSResolver?i=google.com;whoami|
| 02/10/2024 13:17:49  | Server.log     | création d’un nouvel utilisateur "bob"      |  via https://192.168.1.200:3000/LocalDNSResolver?i=google.com;useradd+bob               |
| 02/10/2024 13:35:55  | Server.log    | Modification du mdp de bob      | GET https://192.168.1.200:3000/LocalDNSResolver?i=google.com;echo+"azerty123456"+|+sudo+passwd+--stdin+bob   |
| 02/10/2024 13:36:07  | auth.log   | Connexion SSH réussie juste après le changement de mot de passe de 192.168.1.176      | Oct  2 13:36:07 michael-u2204 sshd[5650]: Accepted password for bob from 192.168.1.176 port 58814 ssh2   |


---

## Conclusion
Plusieurs attaques via des requetes web on été effectué, certaine ont réussi en creer un utilisateur qui a pu avoir accés au serveur.

---

## Recommandations
- Limiter l'exposition des services : Fermer tous les ports non nécessaires
- Installer et configurer fail2ban pour bloquer les IP effectuant des scans répétitifs
- Corriger les vulnerabilité de l’application web
- Changer les tokens compromis, et stocker les nouveaux de manière sécurisé
- Utiliser des mot de passe fort, voir la double authentification



## Fichiers logs
- [log.zip](log.zip)

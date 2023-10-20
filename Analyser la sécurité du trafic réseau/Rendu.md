# Analyser la sécurité du trafic réseau

## Capturer le processus DORA du protocole DHCP
Le processus DORA représente les étapes du protocole DHCP, signifiant Discover, Offer, Request, et Acknowledge.
![Wireshark DORA](https://github.com/CyrilDeva/Simplon-AIS/blob/main/Analyser%20la%20s%C3%A9curit%C3%A9%20du%20trafic%20r%C3%A9seau/Screenshots/WiresharkDHCP.png?raw=true)


## Qu’est-ce que le DHCP Starvation / Snooping ? Rogue DHCP ?
- **DHCP Starvation :** Attaque où un attaquant inonde le serveur DHCP avec de nombreuses demandes, épuisant le pool d'adresses IP.
- **DHCP Snooping :** Mesure de sécurité qui filtre les trames DHCP pour éviter les attaques. Un Rogue DHCP est un serveur DHCP non autorisé sur le réseau.

## Que se passe-t-il lors du « ipconfig /release » (Windows) ? Enjeux de sécurité ?
La commande libère l'adresse IP, pouvant conduire à une usurpation d'identité si un attaquant attribue une adresse IP malveillante.

## Quelle fonctionnalité propose CISCO pour se prémunir de ce type d’attaque ?
Cisco propose DHCP Snooping pour surveiller et filtrer le trafic DHCP, prévenant ainsi les attaques.

## Capturer une requête DNS et sa réponse
- **DNS Spoofing :** Attaque où de fausses informations DNS sont introduites pour rediriger les requêtes.
- **Protection :** Utiliser DNSSEC, un ensemble de mécanismes de sécurité, et renforcer la confiance dans les informations DNS.

## Qu’est-ce que DNS Sec ? DNS over TLS / HTTPS ?
- **DNS Sec :** Chaque réponse DNS est signée numériquement, établissant une chaîne de confiance avec des clés de cryptographie asymétrique.
- **DNS over TLS :** Chiffre les requêtes DNS dans une connexion TLS.
- **DNS over HTTPS :** Chiffre les requêtes DNS dans des requêtes et réponses HTTPS.

## Dans quels cas trouve-t-on du DNS sur TCP ?
- Réponses DNS trop volumineuses pour un paquet UDP.
- Serveurs DNS configurés pour désactiver la mise en cache ou limiter la durée de la mise en cache.

## Capturer un flux HTTP
- **HTTP Smuggling :** Technique d'attaque exploitant les différences dans l'interprétation des en-têtes HTTP par les serveurs web et les passerelles.
- **Exemple CVE :** CVE-2019-9513, vulnérabilité liée à l'attaque "HTTP Desync".

## Comment mettre en place la confidentialité pour ce service ?
- Utiliser HTTPS (SSL/TLS).
- Utilisation de Content Security Policy (CSP).
- Mise en Place de Web Application Firewall (WAF).

## Qu’est-ce qu’une PKI ?
PKI (Public Key Infrastructure) : Ensemble de ressources, processus, et protocoles pour gérer les clés cryptographiques et assurer la sécurité des communications électroniques.

## Capturer un mot de passe FTP ou Telnet (mettre en place les services si nécessaire)
- **Confidentialité :** Utiliser FTPS (FTP sécurisé) qui utilise SSL/TLS pour chiffrer les données.

## Capturer un handshake TLS – puis déchiffrer le trafic avec votre certificat
- **Autorité de Certification (AC) racine :** Entité de confiance émettant et vérifiant les certificats numériques.
- **Chaine de confiance :** Connectez-vous sur https://taisen.fr et affichez la chaîne de confiance du certificat.

## Capturer une authentification Kerberos (mettre en place le service si nécessaire)
- Essayez sur IPv6 (activé par défaut sur Windows Server).

## Capturer une authentification RDP (mettre en place le service si nécessaire)
- Attaques connues sur NetLM.

## Capturer une authentification WinRM (Vous pouvez utiliser EvilWinRM si nécessaire côté client.)
- Capture d'une authentification SSH ou SFTP (mettre en place le service si nécessaire).

## Intercepter un fichier au travers du protocole SMB
Comment protéger l'authenticité et la confidentialité d'un partage SMB ?

# Analyser la sécurité du trafic réseau

## 1. Capturer le processus DORA du protocole DHCP
Le processus DORA représente les étapes du protocole DHCP, signifiant Discover, Offer, Request, et Acknowledge.
![Wireshark DORA](https://github.com/CyrilDeva/Simplon-AIS/blob/main/Analyser%20la%20s%C3%A9curit%C3%A9%20du%20trafic%20r%C3%A9seau/Screenshots/WiresharkDHCP.png?raw=true)


## 2. Qu’est-ce que le DHCP Starvation / Snooping ? Rogue DHCP ?
- **DHCP Starvation :** Attaque où un attaquant inonde le serveur DHCP avec de nombreuses demandes, épuisant le pool d'adresses IP.
- **DHCP Snooping :** Mesure de sécurité qui filtre les trames DHCP pour éviter les attaques. Un Rogue DHCP est un serveur DHCP non autorisé sur le réseau.
- **Rogue DHCP:** Serveur DHCP non autorisé qui opère sur un réseau local, souvent de manière malveillante

## 3. Que se passe-t-il lors du « ipconfig /release » (Windows) ? Enjeux de sécurité ?
La commande libère l'adresse IP, pouvant conduire à une usurpation d'identité si un attaquant attribue une adresse IP malveillante.

## 4. Quelle fonctionnalité propose CISCO pour se prémunir de ce type d’attaque ?
Cisco propose DHCP Snooping pour surveiller et filtrer le trafic DHCP, prévenant ainsi les attaques.

## 5. Capturer une requête DNS et sa réponse
![Wireshark DNS](https://github.com/CyrilDeva/Simplon-AIS/blob/main/Analyser%20la%20s%C3%A9curit%C3%A9%20du%20trafic%20r%C3%A9seau/Screenshots/WiresharkDNS.png?raw=true)

## 6. Qu’est-ce que le DSN Spoofing ? Comment s’en protéger ?
- **DNS Spoofing :** Attaque où de fausses informations DNS sont introduites pour rediriger les requêtes.
- **Protection :** Utiliser DNSSEC, un ensemble de mécanismes de sécurité, et renforcer la confiance dans les informations DNS.

## 7. Qu’est-ce que DNS Sec ? DNS over TLS / HTTPS ?
- **DNS Sec :** Chaque réponse DNS est signée numériquement, établissant une chaîne de confiance avec des clés de cryptographie asymétrique.
- **DNS over TLS :** Chiffre les requêtes DNS dans une connexion TLS.
- **DNS over HTTPS :** Chiffre les requêtes DNS dans des requêtes et réponses HTTPS.

## 8. Dans quels cas trouve-t-on du DNS sur TCP ?
- Réponses DNS trop volumineuses pour un paquet UDP.
- Serveurs DNS configurés pour désactiver la mise en cache ou limiter la durée de la mise en cache.

## 9. Capturer un flux HTTP
![Wireshark HTTP](https://github.com/CyrilDeva/Simplon-AIS/blob/main/Analyser%20la%20s%C3%A9curit%C3%A9%20du%20trafic%20r%C3%A9seau/Screenshots/WiresharkHTTP.png?raw=true)

## 10. Dans quels cas trouve-t-on du DNS sur TCP
- **HTTP Smuggling :** Technique d'attaque exploitant les différences dans l'interprétation des en-têtes HTTP par les serveurs web et les passerelles.
- **Exemple CVE :** CVE-2019-9513, vulnérabilité liée à l'attaque "HTTP Desync".

## 11. Comment mettre en place la confidentialité pour ce service ?
- Utiliser HTTPS (SSL/TLS).
- Utilisation de Content Security Policy (CSP).
- Mise en Place de Web Application Firewall (WAF).

## 12. Qu’est-ce qu’une PKI ?
PKI (Public Key Infrastructure) : Ensemble de ressources, processus, et protocoles pour gérer les clés cryptographiques et assurer la sécurité des communications électroniques.

## 13. Capturer un mot de passe FTP ou Telnet (mettre en place les services si nécessaire)
![Wireshark FTP](https://github.com/CyrilDeva/Simplon-AIS/blob/main/Analyser%20la%20s%C3%A9curit%C3%A9%20du%20trafic%20r%C3%A9seau/Screenshots/WiresharkFTP.png?raw=true)

## 14. Comment mettre en place la confidentialité pour ce service ?
- **Confidentialité :** Utiliser FTPS (FTP sécurisé) qui utilise SSL/TLS pour chiffrer les données.

## 15. Capturer un handshake TLS – puis déchiffrer le trafic avec votre certificat
![Wireshark TLS](https://github.com/CyrilDeva/Simplon-AIS/blob/main/Analyser%20la%20s%C3%A9curit%C3%A9%20du%20trafic%20r%C3%A9seau/Screenshots/WireSharkeTLS.png?raw=true)

## 16. Qu’est-ce qu’une autorité de certification (AC) racine ? Qu'est qu'une AC intermediaire ?
- **Autorité de Certification (AC) racine :** Entité de confiance émettant et vérifiant les certificats numériques.
- **Chaine de confiance :** Connectez-vous sur https://taisen.fr et affichez la chaîne de confiance du certificat.

## 17. Connectez-vous sur https://taisen.fr et affichez la chaine de confiance du certificat
![Certif Taisen](https://github.com/CyrilDeva/Simplon-AIS/blob/main/Analyser%20la%20s%C3%A9curit%C3%A9%20du%20trafic%20r%C3%A9seau/Screenshots/CertifTaisen.png?raw=true)


## 18. Capturer une authentification Kerberos (mettre en place le service si nécessaire)
![Kerberos](https://github.com/CyrilDeva/Simplon-AIS/blob/main/Analyser%20la%20s%C3%A9curit%C3%A9%20du%20trafic%20r%C3%A9seau/Screenshots/Kerberos.png?raw=true)

## Essayez sur IPv6 (activé par défaut sur Windows Server)

## 20. Capturer une authentification RDP (mettre en place le service si nécessaire)
![RDP](https://github.com/CyrilDeva/Simplon-AIS/blob/main/Analyser%20la%20s%C3%A9curit%C3%A9%20du%20trafic%20r%C3%A9seau/Screenshots/Rdp.png?raw=true)

## 21. Quelles sont les attaques connues sur NetLM ?
Les attaques par relais NTLM sont l’un des types d’attaques les plus courants contre Active Directory (AD).
PetitPotam est une attaque par relais NTLM qui exploite le mécanisme de défi-réponse NTLM et permet de contraindre les serveurs Windows, y compris les contrôleurs de domaine, à s’authentifier auprès d’une destination malveillante, ce qui permet à des adversaires de potentiellement prendre le contrôle d’un domaine Windows entier. Il est recommandé de restreindre l’authentification NTLM et NTLMv2 pour minimiser les risques d’attaques.

## 22. Capturer une authentification WinRM (Vous pouvez utiliser EvilWinRM si nécessaire côté client.)
![winRM](https://github.com/CyrilDeva/Simplon-AIS/blob/main/Analyser%20la%20s%C3%A9curit%C3%A9%20du%20trafic%20r%C3%A9seau/Screenshots/winrm.png?raw=true)

## 23. Capturer une authentification SSH ou SFTP (mettre en place le service si nécessaire)
![SSH](https://github.com/CyrilDeva/Simplon-AIS/blob/main/Analyser%20la%20s%C3%A9curit%C3%A9%20du%20trafic%20r%C3%A9seau/Screenshots/ssh.png?raw=true)

## 24. Intercepter un fichier au travers du protocole SMB
![SMB](https://github.com/CyrilDeva/Simplon-AIS/blob/main/Analyser%20la%20s%C3%A9curit%C3%A9%20du%20trafic%20r%C3%A9seau/Screenshots/smb.png?raw=true)

## 25. Comment proteger l'authenticité et la confidentialité d'un partage SMB ?
Ne pas utiliser d'ancienne version smb sans chiffrement. Utiliser SMB3.0 ou plus
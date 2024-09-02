# Rapport de Veille Technologique : Détection des Intrusions

## 1. Mesures de Sécurité Défensive en Entreprise

En tant qu'administrateur système, réseau et sécurité, la mise en œuvre de mesures de sécurité défensive est cruciale pour protéger l'infrastructure IT d'une entreprise contre les menaces. Voici les principales mesures de sécurité défensive mises en place en entreprise :

- **Pare-feu** : Filtre le trafic entrant et sortant pour empêcher les accès non autorisés.
- **Antivirus/Antimalware** : Détecte et supprime les logiciels malveillants sur les systèmes d'information.
- **Systèmes de Détection et de Prévention d'Intrusions (IDS/IPS)** : Identifie et prévient les tentatives d'intrusion sur le réseau.
- **Contrôle d'accès** : Limite l'accès aux ressources réseau en fonction des rôles et des autorisations des utilisateurs.
- **Chiffrement des données** : Protège les données sensibles en les rendant illisibles sans une clé de décryptage.
- **Authentification multi-facteurs (MFA)** : Renforce la sécurité de l'accès aux systèmes en combinant plusieurs méthodes d'authentification.
- **Sauvegardes régulières** : Assure la continuité des opérations en cas de compromission des données.

## 2. Analyse de Trafic

L'analyse de trafic consiste à examiner le flux de données sur un réseau pour identifier des comportements anormaux ou malveillants. Cette analyse est cruciale pour la détection d'intrusions et la gestion des incidents de sécurité.

- **Bénéfices** :
  - Détection précoce des menaces.
  - Identification des failles de sécurité.
  - Surveillance de l'efficacité des politiques de sécurité.
  - Amélioration de la gestion du réseau.

- **Techniques principales** :
  - **Analyse de flux (Flow Analysis)** : Surveille le flux de données entre les points de communication sur le réseau. Elle utilise des outils comme NetFlow pour agréger les données et identifier les anomalies.
  - **Analyse de paquets (Packet Analysis)** : Examine les paquets de données individuels qui traversent le réseau. Cette technique permet une inspection approfondie du contenu du trafic pour détecter des signatures malveillantes spécifiques.

## 3. Notion d'IDS (Intrusion Detection System)

Un IDS est un système qui surveille le réseau ou les systèmes pour détecter des activités suspectes pouvant indiquer une intrusion. Les IDS peuvent alerter les administrateurs, mais ne bloquent pas automatiquement les menaces.

- **Sous-catégories d'IDS** :
  - **IDS basé sur le réseau (NIDS)** : Surveille le trafic réseau pour détecter des activités anormales ou malveillantes.
  - **IDS basé sur l'hôte (HIDS)** : Surveille les activités d'un seul hôte ou serveur, en analysant les journaux système, les fichiers et autres sources de données internes.

## 4. Notion d'IPS (Intrusion Prevention System)

Un IPS est similaire à un IDS, mais avec une capacité supplémentaire de bloquer ou prévenir activement les intrusions détectées. Un IPS agit en temps réel pour empêcher les menaces de compromettre le réseau.

- **Sous-catégories d'IPS** :
  - **IPS basé sur le réseau (NIPS)** : Bloque les menaces au niveau du trafic réseau, en interrompant les connexions malveillantes.
  - **IPS basé sur l'hôte (HIPS)** : Protège les hôtes spécifiques en empêchant l'exécution de comportements malveillants sur le système.

## 5. Techniques de Détection et de Prévention

Les systèmes IDS et IPS utilisent plusieurs techniques pour détecter et prévenir les intrusions :

- **Détection basée sur les signatures** : Compare le trafic réseau ou les activités système avec une base de données de signatures connues d'attaques pour détecter des menaces.
- **Détection basée sur les anomalies** : Utilise des modèles de comportement normal pour identifier des écarts ou anomalies qui pourraient indiquer une menace.
- **Détection basée sur l'état (Stateful Protocol Analysis)** : Surveille les séquences d'événements réseau pour détecter des déviations par rapport au comportement attendu des protocoles.

## 6. Présentation Succincte de Snort

Snort est un IDS/IPS open source largement utilisé pour la détection des intrusions. Développé par Martin Roesch en 1998, il est capable de réaliser une analyse en temps réel du trafic réseau, d'enregistrer les paquets et de déclencher des alertes pour des activités suspectes.

- **Caractéristiques** :
  - Supporte la détection basée sur les signatures.
  - Peut fonctionner en mode IDS (détection) ou IPS (prévention).
  - Offre une flexibilité via un langage de règles pour la création de signatures personnalisées.
  - Compatible avec de nombreux systèmes d'exploitation et plateformes réseau.

## Conclusion

La mise en place de systèmes de détection et de prévention des intrusions est essentielle pour la sécurité des infrastructures IT en entreprise. L'analyse de trafic, les IDS et les IPS, ainsi que les outils comme Snort, offrent des solutions robustes pour anticiper et contrer les menaces en constante évolution. Une veille technologique continue est indispensable pour rester à jour sur les nouvelles techniques et outils dans ce domaine.

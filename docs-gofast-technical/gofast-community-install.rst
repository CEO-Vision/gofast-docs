********************************************
GoFAST Community :  Installation
********************************************

.. note:: En cas de problème vous pouvez poser vos questions sur les forums : https://community.ceo-vision.com

Instructions (par conteneurs)
===============================

Étape 1 : Rendez-vous sur https://gofast-ng.ceo-vision.com/
---------------------------------------------------------------

Lorsque vous vous rendez sur l'interface de téléchargement, une page de configuration fait son apparition, elle est constituée de 4 étapes:

– La configuration du nom de domaine

– La configuration du certificat SSL

– La configuration du serveur SMTP 

– La configuration du compte administrateur de la plateforme


Étape 2 : Configuration du nom de domaine
-------------------------------------------
Sur cet écran vous configurez le nom et le domaine de votre GoFAST Community :

   1. **Nom du site** : C'est le nom qui apparaîtra dans les onglets par exemple
   2. **Nom de domaine complet** : C'est le nom du domaine habituel de votre organisation ex. ``gofast.entreprise-xyz.com`` 
  

Étape 3 : Configuration du Certificat SSL  
----------------------------------------------
Vous devez charger des certificats au format x509 encodé en base64 correspondant au nom de domaine renseigné précédemment.

Vous devez fournir :
   1. **la clé publique de votre certificat** (.pem ou .crt)
   2. **la clé privée correspondant au certificat** (.key)
   
.. NOTE:: Si vous ne savez pas de quoi il s'agit, ces certificats prennent la forme de deux fichiers à demander à votre département IT

.. WARNING:: Pour le moment cette interface ne permet pas de générer des certificats autosignés, si vous souhaitez en générer un **pour un usage de test uniquement**, vous pouvez utiliser un outil en ligne comme https://regery.com/en/security/ssl-tools/self-signed-certificate-generator

Étape 4 : Configuration Serveur SMTP  
------------------------------------------
Cette 4ème étape permet de configurer le serveur SMTP utilisé par GoFAST pour envoyer des emails. Les champs nécessaires sont:

   1. **SMTP Server** :  Le nom de domaine ou l'IP de votre serveur SMTP
   2. **Username** : Si une authentification est nécessaire, le nom d'utilisateur
   3. **Password** : Si une authentification est nécessaire, le mot de passe
   4. **Security** : A renseigner selon le protocole de sécurité utilisé
   5. **SMTP Port** : Le port de votre serveur SMTP
   
.. NOTE:: Si vous ne possedez pas de serveur SMTP, vous pouvez renseigner un serveur SMTP qui n'existe pas (Exemple : smtp.example.org)
   
Étape 5 : Création de l'utilisateur administrateur
--------------------------------------------------------

Configuration Administrateur Fonctionnel
``````````````````````````````````````````````

La partie **Configuration compte Administrateur** permets de renseigner les identifiants du premier compte crée sur GoFAST que vous utiliserez pour vous connecter.

Vous devez choisir l'identifiant, le mot de passe et l'adresse email de ce compte.

.. WARNING:: Il n'est pas possible de choisier 'admin' pour l'identifiant qui est un compte réservé pour le compte administrateur technique (voir ci-dessous).

Configuration Administrateur Technique
````````````````````````````````````````````

La partie **Mot de passe Technique** est réservée au compte administrateur technique de la plateforme. Il est possible de paramétrer chaque mot de passe en décochant **Utiliser le mot de passe technique pour tout les services**.

En tant qu'utilisateur vous n'aurez normalement pas à utiliser ce compte technique.

Etape 6 : Confirmation de la configuration 
---------------------------------------------

.. WARNING::
   Avant de cliquer sur "Obtenir le Compose", bien vérifier tous les champs avant de passer au téléchargement.
   

Une fois ces étapes effectuées, une page apparait avec un récapitulatif. Si tout est correct, validez la configuration.

Après avoir validé le téléchargement, cela téléchargera deux fichiers dans une archive au format .zip :

- Un .env qui contient toutes les variables renseignées
- Un fichier compose.yaml contenant la description de l'application GoFAST en conteneurs

.. NOTE:: Il sera possible prochainnement de re charger ces fichiers pour obtenir les mises à jour de votre plateforme GoFAST Community

Etape 7 : Instancier votre plateforme
----------------------------------------

.. CAUTION:: GoFAST est une application d'entreprise et nécessite un serveur (mini 4vcpu,12GB RAM,SSD recommandé). L'utilisation sur un simple PC sous Docker Desktop est donc déconseillée.

.. NOTE:: Pour pouvoir accéder à l'application, déclarez son nom de domaine (renseigné lors de l'étape 2) avec son adresse IP dans le fichier ``hosts`` de votre ordinateur (https://www.digdeo.fr/articles/sys-admin/modifier-fichier-etc-hosts-windows-mac-linux) ou dans le DNS de l'entreprise
   
.. NOTE:: De nombreuses opérations techniques vont être effectuées ainsi que des démarrages de service, ceci pouvant être plus ou moins long suivant les capacités du serveur. Le temps estimé du premier démarrage se situe entre 10 et 30 min.

Sur une machine Linux - RedHat (Recommandé : AlmaLinux ou CentOS)
`````````````````````````````````````````````````````````````````````
- Installer les paquets podman, podman-compose et unzip en utilisant le gestionnaire de paquets approprié (yum ou dnf selon votre version)

.. code-block:: bash

   dnf install podman-compose podman unzip
   yum install podman-compose podman unzip

- Déziper et copier les fichiers .env et compose.yaml dans le dossier de votre choix

.. code-block:: bash

   mkdir /opt/gofast
   cd /opt/gofast
   unzip gofast-community.zip

- Instanciez votre GoFAST Community

.. code-block:: bash

   podman-compose up -d

- Suivez le déroulement de votre installation

.. code-block:: bash

   podman logs -f gofast-ng-drupal
   podman logs -f gofast-ng-alfresco
   podman logs -f gofast-ng-mysql
   podman logs -f gofast-ng-....

.. NOTE:: Une fois que la commande "podman logs -f gofast-ng-drupal" vous rends la main, cela signifie que l'installation est terminée.

Sur Windows avec Docker Desktop
``````````````````````````````````
Documentation en cours de rédaction

Instructions (pour AWS)
==================================
Cette méthode d'installation reviendra bientôt.

Instructions (par image)
==================================
Cette méthode d'installation reviendra bientôt.

Démarrons ! 
==============

Rendez-vous sur le nom de domaine que vous avez choisi ``https://gofast.entreprise-xyz.com``.

Vous devez créer quelques utilisateurs et des espaces collaboratifs (et sous-espaces).

Les espaces peuvent être de différents types, "Organisation" (départements, ...), "Groupes" (projets, ...), "Extranet" (partenaires, clients, ...). Voir la documentation en ligne ici : https://gofast-docs.readthedocs.io/fr/latest/docs-gofast-users/doc-gofast-guide-utilisateurs.html#gerer-un-espace-collaboratif-groupe

Dans les sous-espaces créés, ajouter des membres qui pourront avoir accès au contenu de cet espace. Ajoutez des sous-espaces si nécessaire.

Ajoutez du contenu en utilisant le glisser-déposer dans le "GoFAST File Browser" (explorateur de fichiers)

Vous êtes prêt pour démarrer !


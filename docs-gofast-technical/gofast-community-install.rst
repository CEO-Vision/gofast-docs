********************************************
GoFAST Community :  Installation et Mise à Jour
********************************************

.. note:: En cas de problème vous pouvez poser vos questions sur les forums : https://community.ceo-vision.com

Installation (par conteneurs)
===============================

.. Note:: Si vous accédez à cette page via le formulaire de GoFAST Community, vous pouvez passer directement à l'étape 2

Étape 1 : Rendez-vous sur: https://gofast-ng.ceo-vision.com/ (Option "Installation")
---------------------------------------------------------------
Une fois que vous avez complété le formulaire du lien ci-dessus et cliqué sur le lien qui vous a été envoyé par e-mail, veuillez procéder comme suit :

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
   2. **Le certificat de l'autorité intermédiaire (CA)** (.pem ou .crt)
   3. **la clé privée correspondant au certificat** (.key)
   
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

Etape 7 : Instancier votre plateforme
----------------------------------------

.. CAUTION:: GoFAST est une application d'entreprise et nécessite un serveur (mini 4vcpu,12GB RAM,SSD recommandé). L'utilisation sur un simple PC sous Podman Desktop ou Docker Desktop est donc déconseillée.

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

Sur Windows avec Docker Desktop et Portainer
````````````````````````````````````````````````
- Créer un dossier sur le PC et déziper gofast-community.zip à l'intérieur

- Installer l'application Docker Desktop : https://www.docker.com/products/docker-desktop/

.. NOTE:: Lors de l'installation garder les paramètres par défaut, notamment l'utilisation de WSL 2. Un redémarrage de Windows sera nécessaire.

.. CAUTION:: Après le redémarrage de Windows à l'ouverture de Docker Desktop, si un message "Docker Desktop requires a newer WSL kernel version" s'affiche, suivez la procédure "Mise à jour du Kernel WSL" dans la rubrique "Problèmes connus".

- Dans Docker Desktop cliquez sur "Add Extensions" dans le menu de gauche et installez l'extension "Portainer". Cette extension vous permettra d'initialiser GoFAST Community de manière simple.

- Ouvrez l'extension "Portainer" dans le menu de gauche et cliquez sur "Get started"

- Dans Portainer sélectionner l'environnement "local" en cliquant ci-dessus 

- Dans Portainer cliquez sur le menu "Stacks" (Dans le petit menu vertical entre le menu de gauche et la fenetre principale)

- Ajouter un nouveau stack à l'aide du bouton "+ Add Stack"

- Donnez lui un nom, par exemple "gofast-community"

- Sélectionnez la méthode "Upload"

- Dans "Upload", chargez votre compose.yaml

- Dans "Environment variables" cliquez sur "Load variables from .env file"

- Pour finaliser l'instanciation, cliquez tout en bas sur "Deploy the stack"

.. CAUTION:: Ce processus une fois lancé va télécharger toutes les images des applications de GoFAST, ce processus peut prendre du temps. Ne pas quitter ou changer de menu tant que vous voyez "Deployment in progress..."

Mise à jour (par conteneurs)
===============================

Étape 1 : Rendez-vous sur: https://gofast-ng.ceo-vision.com/ (Option 'Mise à jour')
---------------------------------------------------------------
Récupérez votre fichier .env généré lors de l'installation de GoFAST Community, puis chargez le dans l'interface.


Étape 2 : Valider les paramètres récupérés
-------------------------------------------
Sur les prochains écrans de configuration, vous pourrez confirmer les paramètres récupérés depuis votre fichier d'environnement .env

Certains paramètres sont modificables, comme : 

   1. **Nom du site** : C'est le nom qui apparaîtra dans les onglets par exemple
   2. **la clé publique de votre certificat** (.pem ou .crt)
   3. **Le certificat de l'autorité intermédiaire (CA)** (.pem ou .crt)
   4. **la clé privée correspondant au certificat** (.key)
   
.. NOTE:: Si vous ne savez pas de quoi il s'agit, ces certificats prennent la forme de deux fichiers à demander à votre département IT

.. WARNING:: Pour le moment cette interface ne permet pas de générer des certificats autosignés, si vous souhaitez en générer un **pour un usage de test uniquement**, vous pouvez utiliser un outil en ligne comme https://regery.com/en/security/ssl-tools/self-signed-certificate-generator

Une fois ces étapes effectuées, une page apparait avec un récapitulatif. Si tout est correct, validez la configuration.

Après avoir validé le téléchargement, cela téléchargera deux fichiers dans une archive au format .zip :

- Un .env qui contient toutes les variables renseignées
- Un fichier compose.yaml contenant la description de l'application GoFAST en conteneurs

Etape 3 : Mettre à jour votre plateforme
----------------------------------------

.. CAUTION:: GoFAST est une application d'entreprise et nécessite un serveur (mini 4vcpu,12GB RAM,SSD recommandé). L'utilisation sur un simple PC sous Podman Desktop ou Docker Desktop est donc déconseillée.

.. NOTE:: Pour pouvoir accéder à l'application, déclarez son nom de domaine (renseigné lors de l'étape 2) avec son adresse IP dans le fichier ``hosts`` de votre ordinateur (https://www.digdeo.fr/articles/sys-admin/modifier-fichier-etc-hosts-windows-mac-linux) ou dans le DNS de l'entreprise
   
.. NOTE:: De nombreuses opérations techniques vont être effectuées ainsi que des démarrages de service, ceci pouvant être plus ou moins long suivant les capacités du serveur. Le temps estimé du premier démarrage se situe entre 10 et 30 min.

Sur une machine Linux - RedHat (Recommandé : AlmaLinux ou CentOS)
`````````````````````````````````````````````````````````````````````
- Arrêter votre GoFAST Community

.. code-block:: bash

   cd /opt/gofast #(Ou votre dossier d'installation)
   podman-compose down

- Déziper et remplacer les fichiers .env et compose.yaml dans le même dossier que votre installation précédente

.. code-block:: bash

   cd /opt/gofast #(Ou votre dossier d'installation)
   unzip gofast-community.zip

- Redémarrer votre GoFAST Community

.. code-block:: bash

   podman-compose up -d

- Suivez le déroulement de votre installation

.. code-block:: bash

   podman logs -f gofast-ng-drupal
   podman logs -f gofast-ng-alfresco
   podman logs -f gofast-ng-mysql
   podman logs -f gofast-ng-....

.. NOTE:: Une fois que la commande "podman logs -f gofast-ng-drupal" vous rends la main, cela signifie que l'installation est terminée.

Sur Windows avec Docker Desktop et Portainer
````````````````````````````````````````````````
Documentation en cours de rédaction

Installation (pour AWS)
==================================
Cette méthode d'installation reviendra bientôt.

Mise à jour (pour AWS)
==================================
Cette méthode d'installation reviendra bientôt.

Démarrons ! 
==============

Rendez-vous sur le nom de domaine que vous avez choisi ``https://gofast.entreprise-xyz.com``.

Vous devez créer quelques utilisateurs et des espaces collaboratifs (et sous-espaces).

Les espaces peuvent être de différents types, "Organisation" (départements, ...), "Groupes" (projets, ...), "Extranet" (partenaires, clients, ...). Voir la documentation en ligne ici : https://gofast-docs.readthedocs.io/fr/latest/docs-gofast-users/doc-gofast-guide-utilisateurs.html#gerer-un-espace-collaboratif-groupe

Dans les sous-espaces créés, ajoutez des membres qui pourront avoir accès au contenu de cet espace. Ajoutez des sous-espaces si nécessaire.

Ajoutez du contenu en utilisant le glisser-déposer dans le "GoFAST File Browser" (explorateur de fichiers)

Vous êtes prêt pour démarrer !

Problèmes connus
===================

Mise à jour du Kernel WSL
-----------------------------
Si une mise à jour du kernel WSK est requise, rendez vous sur https://docs.microsoft.com/windows/wsl/wsl2-kernel

Téléchargez le "Package de mise à jour du noyeau Linux WSL2" proposé  et executez le.

Vous pouvez ensuite relancer Docker Desktop.

Changement de nommage et migration en GoFAST 4.3.0
-----------------------------------------------------
La version 4.3.0 de GoFAST NG a introduit un changement de nommage des conteneurs dans le cadre du début d'exploitation en GoFAST Enterprise.

Ce changement de nommage crée de nouveaux volumes, si vous souhaitez ne pas repartir d'une instance vierge, vous pouvez suivre la procédure suivante

.. CAUTION:: Avant de suivre cette procédure, vous devez avoir mis à jour votre instance en 4.3.0 ou supérieur.

.. CAUTION:: Cette procédure est à suivre uniquement si vous mettez à jour une instance existante de GoFAST Community < 4.3.0 vers GoFAST Community >= 4.3.0

.. NOTE:: Cette procédure s'applique pour les installations par conteneurs sur une machine Linux type RedHat, pour les autres type d'installation, vous pouvez faire une demande sur les forums : https://community.ceo-vision.com

Sur une machine Linux - RedHat (Recommandé : AlmaLinux ou CentOS)
`````````````````````````````````````````````````````````````````````
- Vérifier que les volumes existent avec l'ancien et le nouveau nommage

.. code-block:: bash

   podman volume ls

Vous devriez observer une liste de volumes en 'gofast-ng-community' et 'gofast-ng-main-community' : 

.. code-block:: bash

   DRIVER      VOLUME NAME
   local       gofast-ng-community_gofast-ng-mysql_data
   local       gofast-ng-community_gofast-ng-share_data
   local       gofast-ng-community_gofast-ng-www_data
   local       gofast-ng-community_gofast-ng-drupal_data
   local       gofast-ng-community_gofast-ng-ldap_data
   local       gofast-ng-community_gofast-ng-alfresco_data
   local       gofast-ng-community_gofast-ng-solr_data
   local       gofast-ng-community_gofast-ng-clamav_data
   local       gofast-ng-main-community_gofast-ng-mysql_data
   local       gofast-ng-main-community_gofast-ng-share_data
   local       gofast-ng-main-community_gofast-ng-www_data
   local       gofast-ng-main-community_gofast-ng-ldap_data
   local       gofast-ng-main-community_gofast-ng-alfresco_data
   local       gofast-ng-main-community_gofast-ng-solr_data
   local       gofast-ng-main-community_gofast-ng-keycloak_data
   local       gofast-ng-main-community_gofast-ng-saslauthd_sock

Nous allons donc migrer les données des anciens volumes vers les nouveaux volumes.

Avant de procéder au changement, vérifiez que l'initialisation de votre GoFAST Community est bien terminée. La commande suivante doit vous rendre la main : 

.. code-block:: bash

   podman logs -f gofast-ng-drupal

Vous pouvez également vérifier que le container gofast-ng-drupal a bien terminé son initialisation (Il doit être en état Exited) : 

.. code-block:: bash

   podman ps -a | grep gofast-ng-drupal

- Arrêter votre GoFAST Community

.. code-block:: bash

   podman-compose down

- Migrer les volumes

.. code-block:: bash

   podman run --rm -it -v gofast-ng-community_gofast-ng-mysql_data:/from:z -v gofast-ng-main-community_gofast-ng-mysql_data:/to:z alpine ash -c 'cd /from ; rm -Rf /to/* ; cp -aRf ./* /to/'
   podman run --rm -it -v gofast-ng-community_gofast-ng-www_data:/from:z -v gofast-ng-main-community_gofast-ng-www_data:/to:z alpine ash -c 'cd /from ; rm -Rf /to/* ; cp -aRf ./* /to/'
   podman run --rm -it -v gofast-ng-community_gofast-ng-ldap_data:/from:z -v gofast-ng-main-community_gofast-ng-ldap_data:/to:z alpine ash -c 'cd /from ; rm -Rf /to/* ; cp -aRf ./* /to/'
   podman run --rm -it -v gofast-ng-community_gofast-ng-alfresco_data:/from:z -v gofast-ng-main-community_gofast-ng-alfresco_data:/to:z alpine ash -c 'cd /from ; rm -Rf /to/* ; cp -aRf ./* /to/'
   podman run --rm -it -v gofast-ng-community_gofast-ng-solr_data:/from:z -v gofast-ng-main-community_gofast-ng-solr_data:/to:z alpine ash -c 'cd /from ; rm -Rf /to/* ; cp -aRf ./* /to/'

- Redémarrer votre GoFAST Community

.. code-block:: bash

   podman-compose up -d

- Une fois votre instance démarrée, vous pouvez vous y connecter et vérifier que l'installation a bien été réinitialisée à l'état souhaité. Si tout est conforme, vous pouvez procéder à la suppression des anciens volumes : 

.. code-block:: bash

   podman volume rm gofast-ng-community_gofast-ng-mysql_data
   podman volume rm gofast-ng-community_gofast-ng-share_data
   podman volume rm gofast-ng-community_gofast-ng-www_data
   podman volume rm gofast-ng-community_gofast-ng-drupal_data
   podman volume rm gofast-ng-community_gofast-ng-ldap_data
   podman volume rm gofast-ng-community_gofast-ng-alfresco_data
   podman volume rm gofast-ng-community_gofast-ng-solr_data
   podman volume rm gofast-ng-community_gofast-ng-clamav_data


Sur Windows avec Docker Desktop et Portainer
````````````````````````````````````````````````
Faire une demande sur les forums : https://community.ceo-vision.com
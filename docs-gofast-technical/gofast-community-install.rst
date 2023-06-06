********************************************
GoFAST Community :  Installation
********************************************

.. note:: En cas de problème vous pouvez poser vos questions sur les forums : https://community.ceo-vision.com

Instructions (par conteneurs)
=============================

Étape 1 : Rendez-vous sur https://gofast-ng.ceo-vision.com/
------------------------------

Téléchargement de la configuration
------------------------------

Lorsque vous vous rendez sur l'interface de téléchargement, une page de configuration fait son apparition, elle est constituée de 4 étapes:

–La configuration du nom de domaine

–La configuration du certificat SSL

–La configuration du serveur SMTP 

–La configuration du compte administrateur de la plateforme


Étape 2 : Configuration du nom de domaine
------------------------------
Sur cet écran vous configurez chaque partie du FQDN de GoFAST, ex. ``gofast.ceo-vision.com`` :

   1. **Nom du site** : C'est le nom qui apparaîtra dans les onglets par exemple
   2. **Nom de domaine complet** : C'est le nom du domaine habituel de votre organisation ex. ``gofast-ceovision.com`` 
  

Étape 3 : Configuration du Certificat SSL  
------------------------------
Vous devez chargez des certificats correspondant au nom de domaine chargé précédemment.

Vous devez fournir :
   1. **la clé publique de votre certificat**
   2. **la clé privée**

Étape 4 : Configuration Serveur SMTP  
------------------------------
Cette 4ème étape permet de configurer le serveur SMTP utilisé par GoFAST pour envoyer des emails. Les champs nécessaires sont:

   1. **SMTP Server** :  
   2. **Username** : 
   3. **Password** : 
   4. **Security** : None (without security), TLS (....), SSL (....)
   5. **SMTP Port** : 
 
   
Étape 5 : Création de l'utilisateur administrateur
------------------------------

Configuration Administrateur Fonctionnel
````````````````````````````````````````

La partie **Configuration compte Administrateur** est réservée au compte administrateur fonctionnel de la plateforme.

Cette étape définit le compte administrateur qui a accès à plusieurs configurations supplémentaires une fois l'instance GoFAST démarrée. Vous devez choisir l'identifiant, le mot de passe et l'adresse email de ce compte administrateur.

.. WARNING:: Il n'est pas possible de choisier 'admin' pour l'identifiant qui est un compte réservé pour le compte administrateur fonctionnel

Configuration Administrateur Technique
``````````````````````````````````````

La partie **Mot de passe Technique** est réservée au compte administrateur technique de la plateforme et est liée à l'architecture de celle-ci. Il est possible de paramétrer chaque mot de passe en décochant **Utiliser le mot de passe technique pour tout les services**.




Etape 5 : Confirmation de la configuration 
````````````````````````````````````````````
Vérifiez attentivement tous les champs et validez.

.. WARNING::
   Avant de cliquer sur "Obtenir le Compose", bien vérifier tous les champs avant de passer au téléchargement.
   

Une fois ces 4 étapes effectuées, une page apparait avec un récapitulatif. Si tout est correct, validez la configuration.

Si tout est correct blabla telecharge deux fichiers 

Un .env contient toutes les variables renseignées et un fichier compose.yaml contient la description de l'application en conteneurs

Démarrage de la plateforme
Vague ?

.. CAUTION:: GoFAST est une application d'entreprise et nécessite un serveur (mini 4vcpu,12GB RAM,SSD recommandé). L'utilisation sur un simple PC sous Docker Desktop est donc déconseillée.

.. NOTE:: Pour pouvoir utiliser l'adresse complète (FQDN), déclarer la avec son adresse IP dans le fichier ``hosts`` ou dans le DNS
   
.. NOTE:: De nombreuses opérations techniques vont être effectuées ainsi que des démarrages de service, ceci pouvant être plus ou moins long suivant les capacités du serveur

TODO donner les commandes à executer et la procédure

Instructions (pour AWS)
------------------------

A faire

Instructions (par image)
------------------------

A faire

Démarrons ! 
-------------

–Étape 4: Se rendre sur ``https://votre_nomdedomaine``

Vous devez créer quelques utilisateurs et des espaces collaboratifs (et sous-espaces).

Les espaces peuvent être de différents types, "Organisation" (départements, ...), "Groupes" (projets, ...), "Extranet" (partenaires, clients, ...). Voir la documentation en ligne ici : https://gofast-docs.readthedocs.io/fr/latest/docs-gofast-users/doc-gofast-guide-utilisateurs.html#gerer-un-espace-collaboratif-groupe

Dans les sous-espaces créés, ajouter des membres qui pourront avoir accès au contenu de cet espace. Ajoutez des sous-espaces si nécessaire.

Ajoutez du contenu en utilisant le glisser-déposer dans le "GoFAST File Browser" (explorateur de fichiers)

Vous êtes prêt pour démarrer !


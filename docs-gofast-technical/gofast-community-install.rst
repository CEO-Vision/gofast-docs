********************************************
GoFAST Community :  Installation
********************************************
.. note:: For english instruction please follow this link: https://ceo-vision.readthedocs.io/en/latest/docs/en/doc-gofast-community-install.html

.. note:: En cas de problème vous pouvez poser vos questions sur les forums : https://community.ceo-vision.com

.. caution:: Après l'installation, ne pas oublier de vérifier qu'il existe des mises à jour dans le menu (votre environnement doit avoir accès à internet) ou directement https://votre_adresse_ip/admin/config/gofast/update


Instructions (pour AWS)
------------
https://aws.amazon.com/marketplace/pp/B07NPZHPG3

Instancier GoFAST et aller au paragraphe `La Configuration`_

.. caution:: Ne pas oublier de choisir ``default`` pour "Security Group" pour permettre le traffic entrant 22 (ssh) et 443 (https) 
Instructions (par image)
------------

–Étape 1: Télécharger l’image sur le site https://www.ceo-vision.com/fr/content/gofast-community-ged-plateforme-collaborative-opensource (.ova, ...)

–Étape 2: Instancier l'image dans votre logiciel de virtualisation (VMWare, ...)

.. caution:: GoFAST est une application d'entreprise et nécessite un serveur (mini 2vcpu,6GB RAM,SSD recommandé). L'utilisation sur un simple PC sous VirtualBox est donc déconseillée et il est possible de subir des timeouts au premier accès et ensuite à la fin de la configuration. Un simple rafraichissement de la page suffit.

-Étape 3: Se connecter à la machine virtuelle en mode console et lancer ``nmtui`` pour configurer le réseau (adresse IP fixe, passerelle ...). Voir https://gofast-docs.readthedocs.io/fr/latest/docs-gofast-technical/gofast-docs-prerequis-installation-serveur.html#configuration-du-reseau-par-lexploitant

.. NOTE:: Pour vous connecter à votre VM : Le login utilisateur est ``root`` et le mot de passe ``@C0mmunity!`` (avec un ``0`` et non ``O``). 
.. WARNING:: Le clavier est initialement en mode FR ce qui peut poser problème lorsque vous entrez le mot de passe si vous utilisez un clavier QWERTY. 
.. WARNING:: Le mot de passe root sera changé par celui défini lors du processus de configuration (voir ci-dessous)

–Étape 4: Se rendre sur ``https://votre_adresse_ip`` ce qui lance la configuration de la plate-forme.

.. NOTE:: Pour pouvoir utiliser l'adresse complète (FQDN), déclarer la avec son adresse IP dans le fichier ``hosts`` ou dans le DNS


La configuration
-------------

Lorsque vous vous rendez sur l'adresse IP , une page de configuration fait son apparition, elle est constituée de 4 étapes:

–La configuration du nouveau nom de domaine

–La configuration du certificat SSL

–La configuration du serveur SMTP 

–La configuration du compte administrateur de la plateforme

Une fois ces 4 étapes effectuées, une page apparait avec un récapitulatif. Si tout est correct, validez la configuration.

Etape 1 : Configuration du nom de domaine
`````````````
Sur cet écran vous configurez chaque partie du FQDN de GoFAST, ex. ``gofast.ceo-vision.com`` :

   1. **Nouveau sous-domaine** : C'est le sous-domaine GoFAST, ex. ``gofast``
   2. **Nouveau domaine** : Le domaine habituel de votre organisation ex. ``ceo-vision`` 
   3. **Extension** : Ceci est le TLD, la dernière partie de l'URL ex. ``com``

Etape 2 : Configuration du Certificat SSL  
`````````````
2 possibilités à ce stade, utiliser vos certificats (recommandé) ou en créer des auto-signés.

Pour la 1ère option vous devez fournir :
   1. **la clef publique de votre certificat**
   2. **la clef privée**

Pour la 2ème option vous devez fournir : 
   1. **Country**
   2. **State or Province**
   3. **City**
   4. **Company** 
   5. **Organization unit** 
   6. **Web site name**
   7. **E-mail address** 
.. caution:: Si vous avez généré un certificat SSL auto-signé, il vous faudra ouvrir une autre page avec la meme adresse IP pour de nouveau ajouter l'exception au navigateur

Etape 3 : Configuration Serveur SMTP  
`````````````
Cette 3ème étape permet de configurer le serveur SMTP utilisé par GoFAST pour envoyer des emails. Les champs nécessaires sont:

   1. **SMTP Server** :  
   2. **Username** : 
   3. **Password** : 
   4. **Security** : None (without security), TLS (....), SSL (....)
   5. **SMTP Port** : 
   6. **Recipient address** : 
   
Etape 4 : Creation de l'utilisateur administrateur
`````````````
Cette étape définit le compte administrateur qui a accès à plusieurs configurations supplémentaires une fois l'instance GoFAST démarrée. Vous devez choisir l'identifiant, le mot de passe et l'adresse email de ce compte administrateur.

.. WARNING:: Il n'est pas possible de choisier 'admin' qui est un compte réservé

Etape 5 : Confirmation de la configuration 
`````````````
Vérifiez attentivement tous les champs et validez.

.. WARNING::
   Après avoir cliqué sur "Terminer la configuration" vous ne pouvez plus revenir aux étapes précédantes, bien vérifier tous les champs avant de passer à l'étape suivante
   
.. NOTE:: De nombreuses opérations techniques vont être effectuées ainsi que des démarrages de service, ceci pouvant être plus ou moins long suivant les capacités du serveur

Démarrons ! 
-------------

Vous devez créer quelques utilisateurs et des espaces collaboratifs (et sous-espaces).

Les espaces peuvent être de différents types, "Organisation" (départements, ...), "Groupes" (projets, ...), "Extranet" (partenaires, clients, ...). Voir la documentation en ligne ici : https://gofast-docs.readthedocs.io/fr/latest/docs-gofast-users/doc-gofast-guide-utilisateurs.html#gerer-un-espace-collaboratif-groupe

Dans les sous-espaces créés, ajouter des membres qui pourront avoir accès au contenu de cet espace. Ajoutez des sous-espaces si nécessaire.

Ajoutez du contenu en utilisant le glisser-déposer dans le "GoFAST File Browser" (explorateur de fichiers)

Vous êtes prêt pour démarrer !


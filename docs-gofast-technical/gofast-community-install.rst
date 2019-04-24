********************************************
GoFAST Community :  Installation
********************************************
.. note:: For english instruction please follow this link: https://ceo-vision.readthedocs.io/en/latest/docs/en/doc-gofast-community-install.html

.. note:: En cas de problème vous pouvez poser vos questions sur les forums : https://community.ceo-vision.com

.. caution:: Après l'installation, ne pas oublier de vérifier qu'il existe des mises à jour dans le menu (votre environnement doit avoir accès à internet) 


Instructions (pour AWS)
------------

https://aws.amazon.com/marketplace/pp/B07NPZHPG3

Instancier GoFAST et aller au paragraphe `La Configuration`_

.. caution:: Ne pas oublier de choisir ``default`` pour "Security Group" pour permettre le traffic entrant 22 (ssh) et 443 (https) 
Instructions (par image)
------------

–Étape 1: Télécharger l’image sur le site https://www.ceo-vision.com/fr/content/gofast-community-ged-plateforme-collaborative-opensource (.ova, ...)

–Étape 2: Instancier l'image dans votre logiciel de virtualisation

.. caution:: GoFAST est une application d'entreprise et nécessite un serveur (mini 2vcpu,4GB RAM,SSD recommandé). L'utilisation sur un simple PC sous VirtualBox est donc déconseillée et il est possible de subir des timeouts au premier accès et ensuite à la fin de la configuration. Un simple rafraichissement de la page suffit.

-Étape 3: Se connecter à la machine virtuelle et lancer ``nmtui`` pour configurer le réseau (adresse IP fixe, passerelle ...). Voir https://gofast-docs.readthedocs.io/fr/latest/docs-gofast-technical/gofast-docs-prerequis-installation-serveur.html#configuration-du-reseau-par-lexploitant

.. note:: Pour vous connecter en SSH à votre VM : Le login utilisateur est ``root`` et le mot de passe ``@C0mmunity!`` (avec un ``0`` et non ``O``)

–Étape 4: Se rendre sur ``https://votre_adresse_ip`` et faire la configuration de la plate-forme.

-Étape 5: Pour pouvoir utiliser l'adresse complète, déclarer la avec son adresse IP dans le fichier hosts ou dans le DNS



La configuration
-------------

Lorsque vous vous rendez sur l'adresse IP , une page de configuration fait son apparition, elle est constituée de 4 étapes:

–La configuration du nouveau nom de domaine

–La configuration du certificat SSL

–La configuration du serveur SMTP 

–La configuration du compte administrateur de la plateforme


Une fois ces 4 étapes effectuées, une page apparait avec un récapitulatif. Si tout est correct appuyez sur "Terminer la configuration".

.. caution:: Si vous avez généré un certificat SSL, il vous faudra ouvrir une autre page avec la meme adresse IP pour de nouveau ajouter l'exception au navigateur

Démarrons ! 
-------------

Vous devez créer quelques utilisateurs et des espaces collaboratifs (et sous-espaces).

Les espaces peuvent être de différents types, "Organisation" (départements, ...), "Groupes" (projets, ...), "Extranet" (partenaires, clients, ...). Voir la documentation en ligne ici : https://gofast-docs.readthedocs.io/fr/latest/docs-gofast-users/doc-gofast-guide-utilisateurs.html#gerer-un-espace-collaboratif-groupe

Dans les sous-espaces créés, ajouter des membres qui pourront avoir accès au contenu de cet espace. Ajoutez des sous-espaces si nécessaire.

Ajoutez du contenu en utilisant le glisser-déposer dans le "GoFAST File Browser" (explorateur de fichiers)

Vous êtes prêt pour démarrer !


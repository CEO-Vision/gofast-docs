********************************************
GoFAST Community :  Installation
********************************************
.. note:: For english instruction please follow this link: https://ceo-vision.readthedocs.io/en/latest/docs/en/doc-gofast-community-install.html

.. note:: En cas de problème vous pouvez poser vos questions sur les forums : https://community.ceo-vision.com


Instructions (pour AWS)
------------

https://aws.amazon.com/marketplace/pp/B07NPZHPG3

.. caution:: Ne pas oublier de choisir ``default`` pour "Security Group" pour permettre le traffic entrant 22 (ssh) et 443 (https) 
Instructions (par image)
------------

–Étape 1: Télécharger l’image sur le site https://www.ceo-vision.com/fr/content/gofast-community-ged-plateforme-collaborative-opensource (.ova, ...)

–Étape 2: Instancier l'image dans votre logiciel de Virtualisation 

-Étape 3: Se connecter à la machine virtuelle et lancer ``nmtui`` pour configurer le réseau (adresse IP fixe, passerelle ...). Voir https://gofast-docs.readthedocs.io/fr/latest/docs-gofast-technical/gofast-docs-prerequis-installation-serveur.html#configuration-du-reseau-par-lexploitant

–Étape 4: Se rendre sur ``https://votre_adresse_ip`` et faire la configuration de la plate-forme.

-Étape 5: Pour pouvoir utiliser l'adresse complète, déclarer la avec son adresse IP dans le fichier hosts ou dans le DNS

.. note:: Pour vous connecter en SSH à votre machine : Le login utilisateur est ``root`` et le mot de passe correspond au mot de passe technique que vous avez configuré. ( Par défaut avant la configuration du mot de passe technique : ``@C0mmunity!`` ).

Démarrons ! 
-------------

Vous devez créer quelques utilisateurs et des espaces collaboratifs (et sous-espaces).

Les espaces peuvent être de différents types, "Organisation" (départements, ...), "Groupes" (projets, ...), "Extranet" (partenaires, clients, ...). Voir la documentation en ligne ici : https://gofast-docs.readthedocs.io/fr/latest/docs-gofast-users/doc-gofast-guide-utilisateurs.html#gerer-un-espace-collaboratif-groupe

Dans les sous-espaces créés, ajouter des membres qui pourront avoir accès au contenu de cet espace. Ajoutez des sous-espaces si nécessaire.

Ajoutez du contenu en utilisant le glisser-déposer dans le "GoFAST File Browser" (explorateur de fichiers)

Vous êtes prêt pour démarrer !


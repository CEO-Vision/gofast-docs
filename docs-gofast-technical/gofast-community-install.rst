********************************************
GoFAST Community :  Installation
********************************************
.. note:: For english instruction please follow this link: https://ceo-vision.readthedocs.io/en/latest/docs/en/doc-gofast-community-install.html

Instructions (par image)
------------

(METHODE OBSELETE : < v352r5-05022019 ) 
–Étape 1: Télécharger l’image sur le site https://www.ceo-vision.com/fr/content/gofast-community-ged-plateforme-collaborative-opensource (.ova, ...)

–Étape 2: Instancier l'image dans votre logiciel de Virtualisation 

–Étape 3: Se connecter à cette instance à l’aide des identifiants suivants 

``login : root`` ``password : @C0mmunity!`` ( c’est un zero et non un O) 

–Etape 4: Configurer l'adresse IP par exemple dans  ``/etc/sysconfig/network-scripts/ifcfg-enp0s3`` et rentrer IPADDR  =  Adresse souhaitée à la place de “192.168.8.212”

–Étape 5: Déclarer l'adresse complète ex. ``mygf-community.ceo-vision.com`` correspondant à l'IP dans votre fichier hosts ou dans le DNS

–Étape 6: Se rendre sur ``https://mygf-community.ceo-vision.com`` et faire la configuration de la plate-forme.

-Étape 7: Changer la déclaration du DNS dans le fichier hosts


(NOUVELLE METHODE : >= v352r5-05022019 ) 
–Étape 1: Télécharger l’image sur le site https://www.ceo-vision.com/fr/content/gofast-community-ged-plateforme-collaborative-opensource (.ova, ...)

–Étape 2: Instancier l'image dans votre logiciel de Virtualisation 

-Étape 3: Configurer une adresse IP sur votre machine virtuelle

–Étape 4: Se connecter à cette instance à l’aide des identifiants suivants 

``login : root`` ``password : @C0mmunity!`` ( c’est un zero et non un O) 

–Étape 5: Se rendre sur ``https://votre_adresse_ip`` et faire la configuration de la plate-forme.

-Étape 6: Pour pouvoir utiliser le DNS, déclarer l'adresse complète correspondant à l'adresse IP dans le fichier hosts

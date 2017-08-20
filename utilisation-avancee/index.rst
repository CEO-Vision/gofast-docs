Introduction
============

Ce document a pour but de donner les instructions de configuration de
logiciels tiers fonctionnant avec la plate-forme GoFAST.

Ces outils complémentaires permettent :

-  Des outils complémentaires en mobilité

   -  Une synchronisation de GoFAST avec un PC pour travailler en mode «
      déconnecté » (type DropBox)

   -  L'accès à GoFAST sur les terminaux mobiles (tablettes,…) par
      explorateur de fichiers

   -  La visualisation et l'édition en ligne de documents Office sur
      tablette GalaxyTab (et visualisation seulementsur iOS)

   -  La messagerie instantanée (« chat ») sur mobile

   -  La vidéoconférence sur mobile

-  Des outils de dématérialisation

-  Des outils de signature

Synchronisation locale (GoFAST hors-ligne)
==========================================

CMISSync est un outil puissant qui permet une synchronisation sur un PC
d'un ou plusieurs espaces collaboratifs de GoFAST.

Si vous n'avez plus de réseau ou si vous êtes en déplacement, les
fichiers de GoFAST sont accessibles sur le disque dur de votre
ordinateur.

Si vous les modifiez ils seront directement synchronisés une fois le
réseau disponible.

    **ATTENTION : Cet application est consomatrice de ressources coté
    GoFAST. Elle ne doit être déployée que sur les postes en ayant
    besoin, sur les espaces collaboratifs indispensables et avec une
    fréquence de synchronisation modérée**

|image0|\ |image1|

Installation CMISSync
---------------------

L'outil est disponible pour Windows, Mac(beta) et Linux et peut être
téléchargé ici : https://bitbucket.org/aegif/cmissync/downloads

La version actuelle Windows recommandée\* est la **2.5.6.0 (1 Sept
2015)**

Voici les étapes pour configurer l'outil (**myorg** est à remplacer par
le nom de votre organisation)

L'adresse à utiliser :
`https://gofast. <https://gofast.myorg.com/alfresco/api/-default-/public/cmis/versions/1.1/atom>`__\ `**myorg** <https://gofast.myorg.com/alfresco/api/-default-/public/cmis/versions/1.1/atom>`__\ `.com/alfresco/api/-default-/public/cmis/versions/1.1/atom <https://gofast.myorg.com/alfresco/api/-default-/public/cmis/versions/1.1/atom>`__

.. figure:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image008.jpg
   :alt: 

A cette étape il est possible de choisirl'espace collaboratif que l'on
souhaite synchroniser. Bien sûr si cet espacecollaboratif contient des
sous-espaces ceux-ci sont synchronisés et donc levolume de données à la
1ère synchronisation peut être très important. Compterpar exemple 30
minutes de synchronisation pour 1700 fichiers / 1.2 Go.

Si vous voulez donc tout synchroniser,choisir l'espace 'racine', ici
'Main Repository'

+----+------------+
+====+============+
|    | |image2|   |
+----+------------+

Une fois configuré il est possible de faireplusieurs actions comme
ouvrir le dossier local de synchronisation, mettre enpause la
synchronisation ou changer les paramètres.

+----+------------+
+====+============+
|    | |image3|   |
+----+------------+

Note:Dansles paramètres il est possible de baisser la fréquence de
synchronisation,option utile si CMISSync est largement diffusé dans
l'organisation ceci pouvantcharger la plateforme GoFAST. En effet
CMISSync consomme de la bande passantecoté serveur et du CPU

.. figure:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image014.jpg
   :alt: 

Fonctionnement

Lorsque l'ordinateur est connecté au réseau,CMISSync vérifie
périodiquement si des documents ont été changés sur laplateforme GoFAST.
Si oui ces documents sont copiés localement.

.. figure:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image016.gif
   :alt: 

Note:si vous faites des modifications en mode déconnecté (offline), lors
de lareconnexion sur le serveur GoFAST, votre version sera téléchargée
et versionnéesauf si un utilisateur a fait des modifications entre-temps
sur la GoFAST. Dansce cas une « gestion des conflits » se déclenche
(voir ci dessous)

+----+------------+
+====+============+
|    | |image4|   |
+----+------------+

Exemple denotification (version anglaise)

1) UserA et UserB ont le fichier **courrier.doc** synchronisésur leur
poste

2) UserA et UserBse déconnectent (offline), et chacun édite
**courrier.doc** en local

3) UserA redevientconnecté (online). CmisSync télécharge la version de
UserA de **courrier.doc** sur le serveur GoFAST (quiversionne
automatiquement).

4) UserB redevientconnecté. CmisSync essaie de télécharger la version de
UserB de **courrier.doc** sur le serveurGoFAST, mais constate que le
fichier a déjà été modifié par UserA.

5) Sur le PC deUserB, CmisSync renomme la version de UserB
**courrier.doc** en courrier.doc\_UserB-version et télécharge
**courrier.doc** de UserA sur le PC

6) UserB amaintenant 2 versions, et doit faire une des 3 actions:

a) Garder laversion de UserA : Effacer **courrier.doc\_UserB-version**

b) Garder laversion de UserB : Effacer **courrier.doc** (UserA)
etretirer le suffix de **courrier.doc** **\_UserB-version** è dans ce
cas la version de B va être écrasée sur leserveur GoFAST après
versionnage

c) Fusionner les 2versions dans **courrier.doc**, puis effacer
**courrier.doc\_UserB-version**

| 

    **IMPORTANT: si vous effacez un répertoire en local dans
    l'arborescence synchronisée, lesrépertoires distants seront
    supprimés. Par mesure de précaution, il estpréférable d'éviter de
    supprimer un répertoire en local dans l'arborescence synchronisée.**

La GoFAST ne supprime pas définitivement lesdocuments mais une procédure
de « republication » doit être faite.

Accès aux fichiers de la GoFAST sur Tabletteet Smartphone

Il est possible d'accéder à la plateformeGoFAST à partir de tablettes
Android (ex. GalaxyTab), iOS (iPAD) et smartphonesdont Blackberry.

Pour cela vous devez installer le logicielgratuit **« Webdav Navigator
»** sur iTunes, GooglePlay ouBlackberry AppWorld.

Le site de l'éditeur se trouve à l'adressesuivante :
http://seanashton.net/webdav/

A noter qu'une version payante incluant lasynchronisation locale est
disponible sous le nom **« Webdav Nav+ »**

.. figure:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image021.jpg
   :alt: 

.. figure:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image023.jpg
   :alt: 

.. figure:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image025.jpg
   :alt: 

Éditer des fichiers Office sur Tablette

Tablette Android

Pour ce type de tablette nous recommandonsd'utiliser la suite Office «
**WPS Office** » disponible surGooglePlay.

Vous pourrez configurer un espace destockage directement sur la GoFAST
par « Ouvrir/Ajouter un stockage en nuage » puis choisir « Webdav » et
entrer l'adresse« https://gofast.mycomp.com/alfresco/webdav » ou vous
devez remplacer mycomp.com par l'adresse de votreorganisation.

|image5|\ |image6|\ L'applicationva vous demander ensuite votre
identifiant et mot de passe sur la GoFAST.

Il est ensuite possible d'ouvrir un documentdirectement sur la GoFAST.
Certaines polices de caractère n'existent pas sousAndroid, la mise en
page peut être différente de celle sous PC.

La sauvegarde peut de même changerlégèrement la mise en page.

Important: Lorsqu'on sauvegarde ledocument, celui-ci est d'abord
sauvegardé en local sur la tablette. Une foisque l'application est
fermée (X), la synchronisation est effectuée avec laGoFAST

Tablette iPad

Si vous souhaitez uniquement consulter lesdocuments Office, nous vous
conseillons également « **WPS Office** ».

Néanmoins il existe actuellement unelimitation sur la version iPad pour
sauvegarder un document qui a été ouvertsur la GoFAST il est nécessaire
de reparcourir tout l'espace de stockage ce quin'est pas très pratique.
L'éditeur est notifié de ce bug et un correctifdevrait être produit.

Dans l'attente de ce correctif, il estpossible d'utiliser la suite «
**Citrix ShareFile QuickEdit** »

+----+------------+
+====+============+
|    | |image7|   |
+----+------------+

+----+------------+
+====+============+
|    | |image8|   |
+----+------------+

|  

Messagerie instantanée (« chat »)sur mobiles

.. figure:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image035.gif
   :alt: 

Avec GoFAST vous avez une messagerieinstantanée privée, équivalent de «
WhatsApp » pour votreOrganisation, fonctionnant sur le standard ouvert
XMPP.

Vous pouvez donc utiliser une applicationpour votre téléphone suivant ce
standard. Par exemple :

-  Android : Xabber, FreeLab Messenger

-  iOS : à déterminer

Pour configurer ces clients il suffitd’entrer dans la gestion des
comptes :

**Identifiant** : identifiant\_gofast@gofast-comm.xxxxx.yyy

Dématérialiser vers GoFAST

Dématérialiser à partir d’un smartphone

Il est possible de dématérialiser des notesde frais directement à partir
d’un smartphone et de les envoyer directementdans GoFAST.

Pour cela vous devez avoir 2applications :

-  CamScanner

-  Webdavnav (voir sectionprécédente)

--------------

[`1] <#_ftnref1>`__ A partir de la 2.4.6CMISync corrige un bug majeur
signalé par CEO-Vision concernant le fonctionnement avec les
multi-emplacements avecun entrepôt Alfresco

.. |image0| image:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image002.gif
.. |image1| image:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image004.gif
.. |image2| image:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image010.jpg
.. |image3| image:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image012.gif
.. |image4| image:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image018.gif
.. |image5| image:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image027.gif
.. |image6| image:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image029.gif
.. |image7| image:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image031.gif
.. |image8| image:: /C:/Users/cpotter/AppData/Local/Temp/msohtmlclip1/01/clip_image033.gif

**Introduction\***\ \*\*\*

Ce document a pour but de donner les instructions de configuration de
logiciels tiers fonctionnant avec la plate-forme GoFAST.

Ces outils complémentaires permettent :

1. Une synchronisation de la GoFAST avec un PC pour travailler en mode «
   déconnecté » (équivalent de DropBox)

2. L'accès à la GoFAST sur les terminaux mobiles (tablettes,…) par
   explorateur de fichiers

3. La visualisation et l'édition en ligne de documents Office sur
   tablette GalaxyTab (et visualisation seulement sur iOS)

4. La messagerie instantanée (« chat ») sur mobiles

5. La vidéoconférence sur mobile

**Synchronisation locale (CMISSync)\***\ \*\*\*

CMISSync est un outil puissant et fiable qui permet une synchronisation
sur un PC d'un ou plusieurs espaces collaboratifs de la GoFAST.

Si vous n'avez plus de réseau ou si vous êtes en déplacement, les
fichiers de la GoFAST sont accessibles sur le disque dur de votre
ordinateur.

Si vous les modifiez ils seront directement synchronisés une fois le
réseau disponible.

|image0|\ |image1|\ |image2|

**Installation\***\ \*\*\*

L'outil est disponible pour Windows, Mac (beta) et Linux et peut être
téléchargé ici : https://bitbucket.org/aegif/cmissync/downloads

La version actuelle Windows recommandée\* est la **2.5.6.0 (1 Sept
2015)**

Voici les étapes pour configurer l'outil (**myorg** est à remplacer par
le nom de votre organisation)

L'adresse à utiliser :
`https://gofast. <https://gofast.myorg.com/alfresco/api/-default-/public/cmis/versions/1.1/atom>`__\ `**myorg** <https://gofast.myorg.com/alfresco/api/-default-/public/cmis/versions/1.1/atom>`__\ `.com/alfresco/api/-default-/public/cmis/versions/1.1/atom <https://gofast.myorg.com/alfresco/api/-default-/public/cmis/versions/1.1/atom>`__

+----+------------+
+====+============+
|    | |image3|   |
+----+------------+

A cette étape il est possible de choisir l'espace collaboratif que l'on
souhaite synchroniser. Bien sûr si cet espace collaboratif contient des
sous-espaces ceux-ci sont synchronisés et donc le volume de données à la
1ère synchronisation peut être très important. Compter par exemple 30
minutes de synchronisation pour 1700 fichiers / 1.2 Go.

Si vous voulez donc tout synchroniser, choisir l'espace 'racine', ici
'Main Repository'

+----+------------+
+====+============+
|    | |image4|   |
+----+------------+

Une fois configuré il est possible de faire plusieurs actions comme
ouvrir le dossier local de synchronisation, mettre en pause la
synchronisation ou changer les paramètres.

+----+------------+
+====+============+
|    | |image5|   |
+----+------------+

**Note\***\ \*:\ ***Dans les paramètres il est possible de baisser la
fréquence de synchronisation, option utile si CMISSync est largement
diffusé dans l'organisation ceci pouvant charger la plateforme GoFAST.
En effet CMISSync consomme de la bande passante coté serveur et du
CPU***\ \*\*

|image6|

**Fonctionnement\***\ \*\*\*

Lorsque l'ordinateur est connecté au réseau, CMISSync vérifie
périodiquement si des documents ont été changés sur la plateforme
GoFAST. Si oui ces documents sont copiés localement.

|image7|

**Note\***\ \*:\ **** si vous faites des modifications en mode
déconnecté (offline), lors de la reconnexion sur le serveur GoFAST,
votre version sera téléchargée et versionnée sauf si un utilisateur a
fait des modifications entre-temps sur la GoFAST. Dans ce cas une «
gestion des conflits » se déclenche (voir ci dessous)\ **\*\***

+----+------------+
+====+============+
|    | |image8|   |
+----+------------+

Exemple de notification (version anglaise)

1) UserA et UserB ont le fichier **courrier.doc** synchronisé sur leur
poste

2) UserA et UserB se déconnectent (offline), et chacun édite
**courrier.doc** en local

3) UserA redevient connecté (online). CmisSync télécharge la version de
UserA de **courrier.doc** sur le serveur GoFAST (qui versionne
automatiquement).

4) UserB redevient connecté. CmisSync essaie de télécharger la version
de UserB de **courrier.doc** sur le serveur GoFAST, mais constate que le
fichier a déjà été modifié par UserA.

5) Sur le PC de UserB, CmisSync renomme la version de UserB
**courrier.doc** en courrier.doc\_UserB-version et télécharge
**courrier.doc** de UserA sur le PC

6) UserB a maintenant 2 versions, et doit faire une des 3 actions:

a) Garder la version de UserA : Effacer **courrier.doc\_UserB-version**

b) Garder la version de UserB : Effacer **courrier.doc** (UserA) et
retirer le suffix de **courrier.doc\_UserB-version** è dans ce cas la
version de B va être écrasée sur le serveur GoFAST après versionnage

c) Fusionner les 2 versions dans **courrier.doc**, puis effacer
**courrier.doc\_UserB-version**

**Important\***\ \*: si vous effacez un répertoire en local dans
l'arborescence synchronisée, les répertoires distants seront supprimés.
Par mesure de précaution, il est préférable d'éviter de supprimer un
répertoire en local dans l'arborescence synchronisée.\ **\*\***

**La GoFAST ne supprime pas définitivement les documents mais une
procédure de « republication » doit être faite.\***\ \*\*\*

**Accès aux fichiers de la GoFAST sur Tablette et Smartphone\***\ \*\*\*

Il est possible d'accéder à la plateforme GoFAST à partir de tablettes
Android (ex. GalaxyTab), iOS (iPAD) et smartphones dont Blackberry.

Pour cela vous devez installer le logiciel gratuit **« Webdav Navigator
»** sur iTunes, GooglePlay ou Blackberry AppWorld.

Le site de l'éditeur se trouve à l'adresse suivante :
http://seanashton.net/webdav/

A noter qu'une version payante incluant la synchronisation locale est
disponible sous le nom **« Webdav Nav+ »**

|image9|

|image10|

**Éditer des fichiers Office sur Tablette\***\ \*\*\*

**Tablette Android\***\ \*\*\*

Pour ce type de tablette nous recommandons d'utiliser la suite Office «
**WPS Office** » disponible sur GooglePlay.

Vous pourrez configurer un espace de stockage directement sur la GoFAST
par « Ouvrir/Ajouter un stockage en nuage » puis choisir « Webdav » et
entrer l'adresse « https://gofast.mycomp.com/alfresco/webdav » ou vous
devez remplacer mycomp.com par l'adresse de votre organisation.

|image11|\ |image12|\ L'application va vous demander ensuite votre
identifiant et mot de passe sur la GoFAST.

Il est ensuite possible d'ouvrir un document directement sur la GoFAST.
Certaines polices de caractère n'existent pas sous Android, la mise en
page peut être différente de celle sous PC.

La sauvegarde peut de même changer légèrement la mise en page.

**Important\***\ \*: Lorsqu'on sauvegarde le document, celui-ci est
d'abord sauvegardé en local sur la tablette. Une fois que l'application
est fermée (X), la synchronisation est effectuée avec la
GoFAST\ **\*\***

**Tablette iPad\***\ \*\*\*

Si vous souhaitez uniquement consulter les documents Office, nous vous
conseillons également « **WPS Office** ».

Néanmoins il existe actuellement une limitation sur la version iPad pour
sauvegarder un document qui a été ouvert sur la GoFAST il est nécessaire
de reparcourir tout l'espace de stockage ce qui n'est pas très pratique.
L'éditeur est notifié de ce bug et un correctif devrait être produit.

Dans l'attente de ce correctif, il est possible d'utiliser la suite «
**Citrix ShareFile QuickEdit** »

+----+-------------+
+====+=============+
|    | |image13|   |
+----+-------------+

+----+-------------+
+====+=============+
|    | |image14|   |
+----+-------------+

**Messagerie instantanée (« chat ») sur mobiles \*\***\ \*\*

|image15|

Avec GoFAST vous avez une messagerie instantanée privée, équivalent de «
WhatsApp » pour votre Organisation, fonctionnant sur le standard ouvert
XMPP.

Vous pouvez donc utiliser une application pour votre téléphone suivant
ce standard. Par exemple :

-  Android : Xabber, FreeLab Messenger

-  iOS : à déterminer

Pour configurer ces clients il suffit d’entrer dans la gestion des
comptes :

**Identifiant** : identifiant\_gofast@gofast-comm.xxxxx.yyy

**Dématérialiser vers GoFAST\***\ \*\*\*

**Dématérialiser à partir d’un smartphone\***\ \*\*\*

Il est possible de dématérialiser des notes de frais directement à
partir d’un smartphone et de les envoyer directement dans GoFAST.

Pour cela vous devez avoir 2 applications :

-  CamScanner

-  Webdavnav (voir section précédente)

.. |image0| image:: img/mobilite/wps7DA7.tmp.jpg
.. |image1| image:: img/mobilite/wps7DB8.tmp.jpg
.. |image2| image:: img/mobilite/wps7DB9.tmp.jpg
.. |image3| image:: img/mobilite/wps7DBA.tmp.jpg
.. |image4| image:: img/mobilite/wps7DBB.tmp.jpg
.. |image5| image:: img/mobilite/wps7DBC.tmp.jpg
.. |image6| image:: img/mobilite/wps7DBD.tmp.jpg
.. |image7| image:: img/mobilite/wps7DBE.tmp.jpg
.. |image8| image:: img/mobilite/wps7DBF.tmp.jpg
.. |image9| image:: img/mobilite/wps7DC0.tmp.jpg
.. |image10| image:: img/mobilite/wps7DC1.tmp.jpg
.. |image11| image:: img/mobilite/wps7DC2.tmp.png
.. |image12| image:: img/mobilite/wps7DD2.tmp.jpg
.. |image13| image:: img/mobilite/wps7DD3.tmp.jpg
.. |image14| image:: img/mobilite/wps7DD4.tmp.jpg
.. |image15| image:: img/mobilite/wps7DD5.tmp.jpg

--------------

**Exploitation GoFast**

--------------

--------------

--------------

--------------

--------------

--------------

--------------

--------------

--------------

+--------+------------------------------------------------------+
| V1.0   | - Version initiale                                   |
+========+======================================================+
| V1.1   | - Ajout d'une partie détaillée sur les sauvegardes   |
+--------+------------------------------------------------------+
| V1.2   | - Ajout de la structure des répertoires (annexe 1)   |
+--------+------------------------------------------------------+

--------------

--------------

--------------

.. contents::

Process
=======

La plateforme GoFast est un ensemble technologique dontles principaux
composants sont les suivants :

A noter que l’ensemble de ces services sont configuréspour démarrer
automatiquement lors du boot du serveur. Pour cela la ligne«
/opt/ceo-vision/startup.sh » a été ajoutée dans le fichier«
/etc/rc.local »

Serveur Web Apache
------------------

Afin que la partie «Portail » de GoFast, qui est basésur une technologie
PHP et notamment le CMS Drupal, puisse fonctionner, il fautqu’elle soit
hébergée sur un serveur Apache

En production, de nombreux processus sont créés afin derépondre à
chacune des requêtes http effectuées par les clients. Ces processussont
nommés «/usr/sbin/httpd »

.. figure:: img\exploit\clip_image002.jpg
   :alt: 

 
~

Serveurs Web Tomcat
-------------------

La partie «Entrepôt documentaire » est assurée par lelogiciel Alfresco,
qui est une application développée en Java, ce qui nécessiteun serveur
web Tomcat pour fonctionner.

De même la partie «Gestion de processus » est assuréepar le logiciel
Bonitasoft, qui est une application développée en Java, ce quinécessite
également un serveur web Tomcat pour fonctionner

.. figure:: img\exploit\clip_image004.jpg
   :alt: 

 
~

Base de données MySQL
---------------------

Les deux composants précédents (Drupal et Alfresco)nécessitent chacun de
posséder une base de données permettant leur bonfonctionnement.

Ces bases de données sont hébergées par MySQL.

La base de données utilisée par Drupal possède le nom«drupal »

La base de données utilisée par Alfresco se nomme« alfresco »

En production, cela se traduit par deuxprocessus :

1)

# /bin/sh/usr/bin/mysqld\_safe –datadir=/var/lib/mysql
--socket=/var/lib/mysql/mysql.sock--pid-file=/var/run/mysqld/mysqld.pid
--basedir=/usr --user=mysql

2)

# /usr/libexec/mysqld--basedir=/usr --datadir=/var/lib/mysql
--plugin-dir=/usr/lib64/mysql/plugin--user=mysql
--log-error=/var/log/mysqld.log--pid-file=/var/run/mysqld/mysqld.pid
--socket=/var/lib/mysql/mysql.sock

.. figure:: img\exploit\clip_image006.jpg
   :alt: 

Moteur de recherche Solr
------------------------

L’indexation et la recherche au sein de la plateformeGoFast sont
assurées par Apache Solr.

En production, cela se traduit par un processus qui senomme «java –jar
start.jar »

.. figure:: img\exploit\clip_image008.jpg
   :alt: 

Serveur LDAP
------------

Les différents Utilisateurs et Espaces collaboratifs de laplateforme
GoFast sont stockés au sein d’un annuaire LDAP, utilisé par
lesdifférents composants de la plateforme.

En production, cela se traduit par un processus « /usr/sbin/slapd »

.. figure:: img\exploit\clip_image010.jpg
   :alt: 

Composant de prévisualisation de documents
------------------------------------------

Tous les documents (compatibles) stockés dans laplateforme GoFast
possèdent une prévisualisation au format PDF.

Cette transformation est assurée par le logicielLibreOffice.

En production cela setraduit par un processus nommé
/opt/libreoffice4.1/program/soffice.bin

+----+------------+
+====+============+
|    | |image0|   |
+----+------------+

Supervision
===========

 
-

Monitoringdu serveur
--------------------

Chez tous nos clients, nous installons automatiquement uncomposant
chargé de monitorer les informations principales du serveur.

Ce composant est « Newrelic »
(`https://newrelic.com/ <smb://newrelic.com/>`__)

Les principales informations supervisées sont lessuivantes :

-  Charge CPU

-  Disk IO

-  Utilisation RAM

-  Place disque disponible

-  Utilisation Réseau

En production, cela setraduit par deux processus « /usr/sbin/nrsysmond
»qui effectuent des requêtes vers internet toutes les 3 minutes.

.. figure:: img\exploit\clip_image014.jpg
   :alt: 

.. figure:: img\exploit\clip_image016.jpg
   :alt: 

--------------

Sécurisation des données (sauvegarde, DR,...)
=============================================

La plateforme GoFAST regroupe le contenu stratégique del'organisation.
La sécurité des données doit s'appuyer sur une couche'architecture'
(RAID+SAN double ou clustering) doublée d'une stratégie
desauvegarde.\ ****

**La sauvegarde est donc primordiale de même que lestests de
restauration. **

La question de la perte admissible doit être posée, toutcomme le délai
de restauration. Ceci permet de déterminer une stratégie desauvegarde.

**A) Sauvegarde distante de la plateforme dans sonintégralité : **

- Par snapshot de VM\ ****

--------------

**B) Sauvegardedistante des données uniquement : **

- Par sauvegarde des donnéesapplicatives

- Par réplication totale desdonnées sur un serveur distant (Disaster
Recovery)

- Par sauvegarde des fichiersuniquement

Sauvegarde par snapshot de VM
-----------------------------

Dans ce cas, l’ensemble de la machine virtuelle estsauvegardée.

Il est recommandé de faire un snapshot quotidien de la VMest dehors des
heures d’activité car il y a un impact sur les
performances(entrées/sorties ou I/O). De plus afin d’assurer l’intégrité
du snapshotl'application peut devoir ‘geler’ la VM pendant un certain
temps, ceci étantdépendant des technologies utilisées.\ ****

**Lorsque CEO-Visionfournit l'hébergement auprès d'un de ses
partenaires, ce type de sauvegarde estautomatiquement incluse.**

 
-

`Sauvegarde desdonnées applicatives <>`__
-----------------------------------------

Une fois par jour à 23h31, toutes les informationsnécessaires au
fonctionnement de la plateforme GoFast sont sauvegardées dans
unrépertoire local.

Pour cela, en utilisant le mécanisme de « cron »Linux, la commande «
/usr/bin/rsnapshotdaily » est exécutée une fois par jour. Ce mécanisme
appel unscript de backup crée par CEO-Vision
(/opt/ceo-vision/backup.sh)qui enregistre les données nécessaires dans
le dossier **/var/backup**

Si une durée de rétention est mise en place, il estpossible de retrouver
les données de 1 ou plusieurs jours auparavant dans cedossier
/var/backup

Les données sauvegardées sont les suivantes :

-  la base Mysql drupal

-  la base Mysql alfresco

-  l’’annuaire ldap

-  les fichiers de l’entrepôt documentaire

-  les sources Drupal

**Il est fortement recommandé àl’infogérant de monter /var/backup sur un
stockage distant\***\ \*\*\*

--------------

**A l'heure actuelle, l'index (Apache Solr) n'est passauvegardé**

`ANNEXE 1 <>`__ : Arborescence GoFAST
=====================================

+--------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| /opt/ceo-vision/                                                                                       | Application & Scripts CEO-Vision/GoFAST          |
+========================================================================================================+==================================================+
| /opt/bonita /opt/libreoffice4.2 /opt/solr /opt/alfresco                                                | Applications                                     |
+--------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| /var/backup                                                                                            | Espace de sauvegarde (mysql,openldap,alfresco)   |
+--------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| /var/lib/mysql /var/lib/ldap /var/www/drupal /var/alfresco                                             | Données des applications                         |
+--------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| /etc/openldap /etc/httpd /etc/extra/browscap.ini /etc/php.ini /etc/my.cnf /etc/crontab /etc/newrelic   | Fichiers de configuration                        |
+--------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| /etc/pki                                                                                               | Certificats                                      |
+--------------------------------------------------------------------------------------------------------+--------------------------------------------------+
+--------------------------------------------------------------------------------------------------------+--------------------------------------------------+

 
-

`ANNEXE II: Sauvegarde par vacations desdonnées sur un serveur distant (Disaster Recovery « Minimal») <>`__
===========================================================================================================

\*Nb : Ceci est une extension (option) de l'abonnement GoFAST, couvrant
la mise à jour d’un environnement supplémentaire.\*

Dans ce cas de DR Minimal, le principe est de remonter lessauvegardes
crées par les scripts GoFAST (voir “Sauvegarde des
donnéesapplicatives”), dans un environnement distant dit de stand-by.

La machine de ‘standby’ est une installation GoFAST en tant que telle.
Lors des mises à jour de l’environnement de production, l’environnement
de DR est mis à jour par CEO-Vision.

**Nb :Afin de garantir l’intégrité d’Alfresco sur le DR, la date des
fichierssauvegardés doit correspondre à la date du snapshot de la base
de données. Ceciest garantie par le script livré avec la plateforme
GoFAST**

-  \*

\*\*Cas 1) La sauvegarde à distance d’Alfresco est faite dans
/var/backup \*\*

n Importde la base de données

n Copiede /var/backup/...alfresco dans /var/alfresco

n Chargementde la partie LDAP

**Cas 2) Lasauvegarde à distance d’Alfresco est faite directement dans
le répertoire/var/alfresco**

n Importde la base de données

n Chargementde la partie LDAP

 
-

`ANNEXE III : Duplication distante des fichiers <>`__
=====================================================

Il peut être souhaité de sauvegarder sur un autre serveurune simple
copie des fichiers de l'entrepôt. ****

**Nb : Dans ce cas seul la dernière versiondes fichiers est sauvegardée.
Les méta-données ou commentaires ne sont passauvegardés.**

**1) Méthode 1 : Lecteur Réseau**

La 1ère méthode est d'utiliser un logiciel de sauvegardesur le serveur
destiné à stocker les sauvegardes. Ce logiciel de sauvegardedoit pouvoir
sauvegarder un «lecteur réseau » ou directement un serveurWebdav. Afin
de limiter la bande passante utilisée et les ressources machinesil est
préférables de faire des sauvegardes incrémentales ou différentielles.

Le « lecteur réseau » possède l'adresse suivante:


`https://\ **url\_de\_la\_gofast**/alfresco/webdav <smb://url_de_la_gofast/alfresco/webdav>`__

 par exemple :
`https://gofast.ceo-vision.com/alfresco/webdav <../webdav>`__

Bien sûr l'identifiant doit être l'utilisateur **'adm'** qui est le seul
utilisateur ayant l'accès à tous les documents de la plate-forme.

**2) Méthode 2 : CMISSync**

La 2ème méthode consiste à utiliser l'utilitaire CMISSync.Cet utilitaire
permet une synchronisation régulière entre la GoFAST et unserveur (ou
PC) local.

CMISSync est gratuitement téléchargeable sur
`https://bitbucket.org/aegif/cmissync/downloads <smb://bitbucket.org/aegif/cmissync/downloads>`__.
Laversion actuelle est la v2.1.x

Cette application sauvegarde dans un répertoire local,l'ensemble de la
GoFAST. Si CMISSync détecte des changements avec le serveur,il rapatrie
les fichiers modifiés coté GoFAST.

Dans ce cas l'adresse à utiliser sera :


`https://url\_de\_la\_gofast/alfresco/cmisatom <smb://url_de_la_gofast/alfresco/cmisatom>`__

 par exemple :
`https://gofast.ceo-vision.com/alfresco/cmisatom <../cmisatom>`__

Bien sûr l'identifiant doit être l'utilisateur **'adm'** qui est le seul
utilisateur ayant l'accès à tous les documents de la plate-forme.

Le choix de l'espace racine se fait avec l'écranci-dessous. **Choisir «
\*\***\ Main Repository »\*\*pour être à la racine de l'ensemble de la
plateforme.

+----+------------+
+====+============+
|    | |image1|   |
+----+------------+

La fréquence de cette réplication est configurable. **Afinde ne pas trop
charger le serveur GoFAST choisir une fréquence supérieure à laminute.
**

Si l'on veut une sauvegarde par jour, il faut indiquer unefréquence de
24h et démarrer l'application à l'heure où l'on souhaite
lasynchronisation différentielle.

.. |image0| image:: img\exploit\clip_image012.jpg
.. |image1| image:: img\exploit\clip_image018.jpg

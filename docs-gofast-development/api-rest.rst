********************************************
GoFAST :  API REST 
********************************************

L'API REST de GoFAST permet aux développeurs d'intéragir avec l'application de manière applicative. Vous trouverez sur cette page toutes les informations nécessaires à l'exploitation de cette API.

Ressources
############################################

Ressource : node
**********************

Cette ressource permet d'intéragir avec les entités Drupal de type noeud. Ces derniers peuvent représenter des documents, articles, espaces, formulaires...

Action : node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir basiquement avec les entités Drupal de type noeud.

GET
__________

Cette méthode permet de récupérer des informations génériques d'une entité de type noeud

*GET: /api/node/node*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+--------------------------+
|  GET Parameter    |   Valeur                 |
+===================+==========================+
|    nid*           |N° du noeud               |
+-------------------+--------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+----------------------------------------------------+
|   Clé                 |   Valeur                                           |
+=======================+====================================================+
|nid                    | N° du noeud                                        |
+-----------------------+----------------------------------------------------+
|type                   | Type du noeud                                      |
+-----------------------+----------------------------------------------------+
|title                  | Titre du noeud                                     |
+-----------------------+----------------------------------------------------+
|status                 | 1: Publié, 0: Dépublié (Supprimé)                  |
+-----------------------+----------------------------------------------------+
|uid                    | N° du créateur du noeud                            |
+-----------------------+----------------------------------------------------+
|sticky                 | 1: Epinglé, 0: Pas épinglé                         |
+-----------------------+----------------------------------------------------+
|language               | Langue du noeud (und, fr, en, nl...)               |
+-----------------------+----------------------------------------------------+
|created                | Timestamp de création du noeud                     |
+-----------------------+----------------------------------------------------+
|updated                | Timestamp de dernière modification du noeud        |
+-----------------------+----------------------------------------------------+
|update_uid             | N° du dernier modificateur du noeud                |
+-----------------------+----------------------------------------------------+
|comment_count          | Nombre de commentaires attachés au noeud           |
+-----------------------+----------------------------------------------------+
|last_comment_uid       | N° du dernier commentateur du noeud                |
+-----------------------+----------------------------------------------------+
|last_comment_timestamp | Timestamp du dernier commentaire du noeud          |
+-----------------------+----------------------------------------------------+
|last_comment_cid       | N° du dernier commentaire du noeud                 |
+-----------------------+----------------------------------------------------+
|alfresco_reference     | Référence du contenu Alfresco associé au noeud     |
+-----------------------+----------------------------------------------------+

Action : metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec les métadonnées associés aux entités de type noeud

GET
__________

Cette méthode permet de récupérer des informations à propos des métadonnées associés aux entités de type noeud

Action : content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec le contenu Alfresco associés aux entités de type noeud

.. CAUTION:: Utiliser cette action sur un noeud sans contenu Alfresco associé aboutira à une erreur "404 Not Found". Les noeuds associés à un contenu Alfresco sont de type "alfresco_item".

GET
__________

Cette méthode permet de récupérer le contenu Alfresco associé à un noeud. 

*GET: /api/node/content*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/octet-stream |
+-------------------+--------------------------+
|Content-Disposition| attachment               |
+-------------------+--------------------------+

+-------------------+--------------------------+
|  GET Parameter    |   Valeur                 |
+===================+==========================+
|    nid*           |N° du noeud               |
+-------------------+--------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/octet-stream               |
+-------------------+----------------------------------------+
|Content-Disposition| attachment; filename="nom_du_fichier"  |
+-------------------+----------------------------------------+

Le contenu du retour de la requête est le contenu du document.


POST
__________

Cette méthode permet de remplacer le contenu Alfresco associé à un noeud en créant une nouvelle version. 

*POST: /api/node/content*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | multipart/form-data      |
+-------------------+--------------------------+

+-------------------+-----------------------------------------------------+
|  POST Parameter   |   Valeur                                            |
+===================+=====================================================+
|    file           | The file to upload                                  |
+-------------------+-----------------------------------------------------+

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+-----------------------------------------------------+
|  POST Parameter   |   Valeur                                            |
+===================+=====================================================+
|    nid*           | N° du noeud                                         |
+-------------------+-----------------------------------------------------+
|    comment        | Commentaire associé à la nouvelle version           |
+-------------------+-----------------------------------------------------+
|  major_version    | 0: Version mineure, 1: Version majeure (default : 0)|
+-------------------+-----------------------------------------------------+

Le contenu de la requête doit être le contenu du document.

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-------------------+----------------------------------------+
|   Clé             |   Valeur                               |
+===================+========================================+
|success            | 1: OK, 0: Erreur                       |
+-------------------+----------------------------------------+

Action : preview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec les prévisualisations PDF associés aux entités de type noeud

.. CAUTION:: Utiliser cette action sur un noeud sans contenu Alfresco associé aboutira à une erreur "404 Not Found". Les noeuds associés à un contenu Alfresco sont de type "alfresco_item".

GET
__________

Cette méthode permet de récupérer la prévisualisation PDF d'un contenu Alfresco associé à un noeud. 

*GET: /api/node/preview*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/pdf          |
+-------------------+--------------------------+
|Content-Disposition| attachment               |
+-------------------+--------------------------+

+-------------------+--------------------------+
|  GET Parameter    |   Valeur                 |
+===================+==========================+
|    nid*           |N° du noeud               |
+-------------------+--------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/pdf                        |
+-------------------+----------------------------------------+
|Content-Disposition| attachment; filename="nom_du_fichier"  |
+-------------------+----------------------------------------+

Le contenu du retour de la requête est le contenu de la prévisualisation PDF du document.

Action : preview_link
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec les prévisualisations PDF associés aux entités de type noeud

.. CAUTION:: Utiliser cette action sur un noeud sans contenu Alfresco associé aboutira à une erreur "404 Not Found". Les noeuds associés à un contenu Alfresco sont de type "alfresco_item".

GET
__________

Cette méthode permet de récupérer un lien vers une prévisualisations PDF associée à une entité de type noeud

*GET: /api/node/preview_link*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+--------------------------+
|  GET Parameter    |   Valeur                 |
+===================+==========================+
|    nid*           |N° du noeud               |
+-------------------+--------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+----------------------------------------------------+
|   Clé                 |   Valeur                                           |
+=======================+====================================================+
|link                    | Lien vers la prévisualisation                     |
+-----------------------+----------------------------------------------------+
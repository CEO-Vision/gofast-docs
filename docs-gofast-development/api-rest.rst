********************************************
GoFAST :  API REST 
********************************************

L'API REST de GoFAST permet aux développeurs d'intéragir avec l'application de manière programmative. Vous trouverez sur cette page toutes les informations nécessaires à l'exploitation de cette API.

Authentification
############################################

Basic
**********************

La méthode d'authentification Basic est la méthode d'authentification classique définit dans la RFC 7617 controlée par le protocole HTTP (aussi appelée HTTP authentication).

Elle nécessite de passer le header *Authorization* à une requête avec en valeur la chaine *Basic AUTHORIZATION_VALUE* ou *AUTHORIZATION_VALUE* est la chaine *username:password* encodée en base 64.

Exemple : Pour l'utilisateur user1:motdepasse1, il faudra passer la valeur :
*Basic dXNlcjE6bW90ZGVwYXNzZTE=*

Token
**********************

La méthode d'authentification par token est utilisée pour générer une session temporaire identifiée par un jeton (une chaine de caractères).

Elle utilise la ressource *login*, l'action *token* et la méthode *GET*.

.. CAUTION:: L'action *token* n'est pas disponible depuis l'API externe de GoFAST, elle est utilisée entre les composants internes de la plateforme.

Ressources
############################################

Ressource : login
**********************

Cette ressource permet d'intéragir avec le système d'authentification de GoFAST.

Action : token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec le système d'authentification par token.

.. CAUTION:: L'action *token* n'est pas disponible depuis l'API externe de GoFAST, elle est utilisée entre les composants internes de la plateforme.

GET
__________

Cette méthode permet de récupérer un token d'authentification. Ce dernier est valable pendant 3 minutes.

*GET: /api/login/token*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+--------------------------+
|  GET Parameter    |   Valeur                 |
+===================+==========================+
|    name*          |Username de l'utilisateur |
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
|token                  | Jeton d'authentification                           |
+-----------------------+----------------------------------------------------+

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

POST
__________

Cette méthode permet de créer une entité de type noeud. Si ce noeud est de type alfresco_item et qu'il n'est pas crée à partir d'un modèle, il est obligatoire d'y ajouter un fichier. 

*POST: /api/node/node*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | multipart/form-data      |
+-------------------+--------------------------+

+-------------------+-----------------------------------------------------------------------------------------------------------------+
|  Clé              |   Valeur                                                                                                        |
+===================+=================================================================================================================+
|    file**         | Le fichier à charger (si le type de noeud est 'alfresco_item' et qu'il n'est pas à créer à partir d'un template)|
+-------------------+-----------------------------------------------------------------------------------------------------------------+

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+--------------------------------------------------------------------------------------------------------------------------+
|  Clé              |   Valeur                                                                                                                 |
+===================+==========================================================================================================================+
|    type*          | Type de noeud                                                                                                            |
+-------------------+--------------------------------------------------------------------------------------------------------------------------+
|    title*         | Le titre du fichier, de l'article, du forum...                                                                           |
+-------------------+--------------------------------------------------------------------------------------------------------------------------+
|    locations**    | Les emplacements dans un tableau sous la forme "/Sites/_Organisations/Mon Organisation/XXX" (alfresco_item seulement)    |
+-------------------+--------------------------------------------------------------------------------------------------------------------------+
|    template_nid** | L'identifiant du noeud du template à partir duquel créer le fichier si nécessaire (alfresco_item seulement)              |
+-------------------+--------------------------------------------------------------------------------------------------------------------------+
|    gids**         | Les n° des espaces de destination dans un tableau (article, forum seulement)                                             |
+-------------------+--------------------------------------------------------------------------------------------------------------------------+
|    body**         | Le contenu au format HTML (article, forum seulement)                                                                     |
+-------------------+--------------------------------------------------------------------------------------------------------------------------+

Les types de noeud disponibles sont : 
 - alfresco_item (Document)
 - article (Page interne)
 - forum (Forum)

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-------------------+----------------------------------------+
|   Clé             |   Valeur                               |
+===================+========================================+
|nid                | N° du noeud                            |
+-------------------+----------------------------------------+

Action : metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec les métadonnées associés aux entités de type noeud

GET
__________

Cette méthode permet de récupérer les métadonnées associés aux entités de type noeud

*GET: /api/node/metadata*

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
|field_XXX              | Tableau contenant les valeurs du champ             |
+-----------------------+----------------------------------------------------+
|field_YYY              | Tableau contenant les valeurs du champ             |
+-----------------------+----------------------------------------------------+

POST
__________

Cette méthode permet de mettre à jour les métadonnées associés aux entités de type noeud

*POST: /api/node/metadata*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

.. NOTE:: Contrairement au retour de la méthode GET, les valeurs ne doivent pas êtres listés de cette manière
           field_XXX : *Array*
                      0: value: *Array*
                              VAL1
                      1: value: *Array*
                              VAL2
          Mais plutôt comme ceci
           field_XXX : *Array*
                      0: VAL1, 
                      1: VAL2 
          Ou comme cela selon le champ modifié
            field_XXX : VAL
          Les champs modifiables sont : field_category, field_state, field_target_link, field_external_page_url, field_date, field_criticity, field_document_author, field_tags

+-------------------+----------------------------------------+
|  Clé              |   Valeur                               |
+===================+========================================+
|    nid*           |N° du noeud                             |
+-------------------+----------------------------------------+
|    field_XXX      |Tableau contenant les valeurs du champ  |
+-------------------+----------------------------------------+
|    field_YYY      |Tableau contenant les valeurs du champ  |
+-------------------+----------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+----------------------------------------------------+
|   Clé                 |   Valeur                                           |
+=======================+====================================================+
|Field_XXX              | Tableau contenant le retour de la fonction         |
+-----------------------+----------------------------------------------------+
|Field_YYY              | Tableau contenant le retour de la fonction         |
+-----------------------+----------------------------------------------------+

PATCH
__________

Cette méthode permet d'ajouter une valeur à certaines métadonnées associés aux entités de type noeud

*PATCH: /api/node/metadata*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

.. NOTE:: Contrairement au retour de la méthode GET, les valeurs ne doivent pas êtres listés de cette manière
           field_XXX : *Array*
                      0: value: *Array*
                              VAL1
                      1: value: *Array*
                              VAL2
          Mais plutôt comme ceci
           field_XXX : *Array*
                      0: VAL1, 
                      1: VAL2 
          Ou comme cela selon le champ modifié
            field_XXX : VAL
          Les champs alterables sont : field_target_link, field_external_page_url, field_tags

+-------------------+----------------------------------------+
|  Clé              |   Valeur                               |
+===================+========================================+
|    nid*           |N° du noeud                             |
+-------------------+----------------------------------------+
|    field_XXX      |Tableau contenant les valeurs du champ  |
+-------------------+----------------------------------------+
|    field_YYY      |Tableau contenant les valeurs du champ  |
+-------------------+----------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+----------------------------------------------------+
|   Clé                 |   Valeur                                           |
+=======================+====================================================+
|Field_XXX              | Tableau contenant le retour de la fonction         |
+-----------------------+----------------------------------------------------+
|Field_YYY              | Tableau contenant le retour de la fonction         |
+-----------------------+----------------------------------------------------+

Action : locations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec les emplacements des contenus associés aux entités de type noeud

GET
__________

Cette méthode permet de récupérer les emplacements des contenus associés aux entités de type noeud

*GET: /api/node/locations*

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
|locations              | Tableau indexé contenant les emplacements.         |
+-----------------------+----------------------------------------------------+

PUT
__________

Cette méthode permet de modifier les emplacements des contenus associés aux entités de type noeud

*PUT: /api/node/locations*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+------------------------------------------+
|  POST Parameter    |   Valeur                                |
+===================+==========================================+
|    nid*           |N° du noeud                               |
+-------------------+------------------------------------------+
|    locations*     |Tableau indexé contenant les emplacements |
+-------------------+------------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+



+-----------------------+------------------------------------------------------------------+
|   Clé                 |   Valeur                                                         |
+=======================+==================================================================+
|locations              | Tableau indexé contenant les emplacements après vidage du cache. |
+-----------------------+------------------------------------------------------------------+

POST
__________

Cette méthode permet d'ajouter ou de supprimer des emplacements des contenus associés aux entités de type noeud

*POST: /api/node/locations*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+-------------------------------------------------------------+
|  POST Parameter    |   Valeur                                                   |
+===================+=============================================================+
|    nid*           |N° du noeud                                                  |
+-------------------+-------------------------------------------------------------+
|    locations*     |Tableau indexé contenant les nouveaux emplacements à ajouter |
+-------------------+-------------------------------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+



+-----------------------+------------------------------------------------------------------+
|   Clé                 |   Valeur                                                         |
+=======================+==================================================================+
|locations              | Tableau indexé contenant les emplacements après vidage du cache. |
+-----------------------+------------------------------------------------------------------+
|delete                 | Boolean 1 = suppression; 0 = ajout.                              |
+-----------------------+------------------------------------------------------------------+

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
|  Clé              |   Valeur                                            |
+===================+=====================================================+
|    nid*           | N° du noeud                                         |
+-------------------+-----------------------------------------------------+
|    comment        | Commentaire associé à la nouvelle version           |
+-------------------+-----------------------------------------------------+
|  major_version    | 0: Version mineure, 1: Version majeure (default : 0)|
+-------------------+-----------------------------------------------------+


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
|link                   |  Lien vers la prévisualisation                     |
+-----------------------+----------------------------------------------------+

Action : version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec les versions des contenus Alfresco associés aux entités de type noeud

GET
__________

Cette méthode permet de récupérer les versions d'un contenu Alfresco associé à une entité de type noeud

*GET: /api/node/version*

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
|creator                | Identifiant du créateur de la version              |
+-----------------------+----------------------------------------------------+
|type                   | MINOR : Version mineure, MAJOR : Version majeure   |
+-----------------------+----------------------------------------------------+
|created                | Timestamp de la création de la version             |
+-----------------------+----------------------------------------------------+
|version                | N° de version                                      |
+-----------------------+----------------------------------------------------+
|comment                | Commentaire associé à la version                   |
+-----------------------+----------------------------------------------------+

Action : versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec les versions des contenus Alfresco associés aux entités de type noeud

GET
__________

Cette méthode permet de récupérer les versions des contenus Alfresco associés à une entité de type noeud

*GET: /api/node/versions*

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
|creator                | Identifiant des créateur des versions              |
+-----------------------+----------------------------------------------------+
|type                   | MINOR : Version mineure, MAJOR : Version majeure   |
+-----------------------+----------------------------------------------------+
|created                | Timestamp de la création des versions              |
+-----------------------+----------------------------------------------------+
|version                | N° des versions                                    |
+-----------------------+----------------------------------------------------+
|comment                | Commentaire associé aux versions                   |
+-----------------------+----------------------------------------------------+

Action : archive
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec l'archivage des documents associées aux entités de type noeud.

POST
__________

Cette méthode permet d'archiver un document associé à une entité de type noeud.

*POST: /api/node/archive*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+--------------------------------------------------------------------+
|  Clé              |   Valeur                                                           |
+===================+====================================================================+
|      nid*         |N° du noeud                                                         |
+-------------------+--------------------------------------------------------------------+
|    unarchive*     |Si la valeur est "true", le document sera désarchivé                |
+-------------------+--------------------------------------------------------------------+

*Retour:*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+--------------------------------------------------------------------+
|  Clé              |   Valeur                                                           |
+===================+====================================================================+
|     nid           |N° du noeud                                                         |
+-------------------+--------------------------------------------------------------------+

Action : status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec le status des entités *node* de Drupal.

POST
__________

Cette méthode permet de publier ou dépublier un noeud et s'il s’agit d’un document, il sera restauré ou supprimé.

*POST: /api/node/status*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+--------------------------------------------------------------------+
|  Clé              |   Valeur                                                           |
+===================+====================================================================+
|  nid*             |   N° du noeud                                                      |
+-------------------+--------------------------------------------------------------------+
|  restore*         |   Si la valeur est "true", le document sera restauré               |
+-------------------+--------------------------------------------------------------------+

*Retour:*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+--------------------------------------------------------------------+
|  Clé              |   Valeur                                                           |
+===================+====================================================================+
|  nid              |N° du noeud                                                         |
+-------------------+--------------------------------------------------------------------+

Action : publication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec les publications de documents associées à des entités de type noeud.

GET
__________

Cette méthode permet de récupérer la publication d’un document si elle existe.

*GET: /api/node/publication*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|  Content-Type     | application/json         |
+-------------------+--------------------------+

+-------------------+--------------------------------------------------------------------+
|  Clé              |   Valeur                                                           |
+===================+====================================================================+
|  nid*             |N° du noeud                                                         |
+-------------------+--------------------------------------------------------------------+

*Retour:*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|  Content-Type     | application/json         |
+-------------------+--------------------------+

+-------------------+--------------------------------------------------------------------+
|  Clé              |   Valeur                                                           |
+===================+====================================================================+
|  nid              |N° du noeud                                                         |
+-------------------+--------------------------------------------------------------------+
|  status           |1: Publié, 0: Dépublié                                              |
+-------------------+--------------------------------------------------------------------+

POST
__________

Cette méthode permet de créer une publication à partir d’un document Alfresco associée à des entités de type noeud.

.. CAUTION:: La documentation de cette API n'est pas encore complète.

*POST: /api/node/publication*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|  Content-Type     | application/json         |
+-------------------+--------------------------+

+-------------------+----------------------------------------------------------------------+
|  Clé              |   Valeur                                                             |
+===================+======================================================================+
|nid*               |N° du noeud                                                           |
+-------------------+----------------------------------------------------------------------+
|locations*         |Tableau indexé contenant les emplacements sous la forme "/Sites/_xxx" |
+-------------------+----------------------------------------------------------------------+

*Retour:*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|  Content-Type     | application/json         |
+-------------------+--------------------------+

+-------------------+--------------------------------------------------------------------+
|  Clé              |   Valeur                                                           |
+===================+====================================================================+
|publication_nid    |N° du noeud de la publication                                       |
+-------------------+--------------------------------------------------------------------+


Action : autocomplete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec le système d'autocomplétion des entités *node* de Drupal.

GET
__________

Cette méthode permet de récupérer une liste de noeuds en fonction de la chaine passée en input et des bundles demandés.

*GET: /api/node/autocomplete*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+--------------------------------------------------------------------+
|  Clé              |   Valeur                                                           |
+===================+====================================================================+
|  str*             |Input                                                               |
+-------------------+--------------------------------------------------------------------+
|  bundles          |Liste de bundles séparés par une virgule (alfresco_item par default)|
+-------------------+--------------------------------------------------------------------+


*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+-----------------------------------------------------------+
|   Clé                 |   Valeur                                                  |
+=======================+===========================================================+
|uid                    | Quelques informations de base sur l'utilisateur           |
+-----------------------+-----------------------------------------------------------+

Ressource : comment
**********************

Cette ressource permet d'intéragir avec les entités Drupal de type comment. Ces derniers représent des commentaires associés à des entités de type noeud (node)

Action : comment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir basiquement avec les entités Drupal de type comment.

GET
__________

Cette méthode permet de récupérer un commentaire

*GET: /api/comment/comment*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+--------------------------+
|  GET Parameter    |   Valeur                 |
+===================+==========================+
|    cid*           |N° du commentaire         |
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
|cid                    | N° du commentaire                                  |
+-----------------------+----------------------------------------------------+
|uid                    | N° de l'utilisateur ayant commenté                 |
+-----------------------+----------------------------------------------------+
|subject                | Titre du commentaire                               |
+-----------------------+----------------------------------------------------+
|body                   | contenu du commentaire                             |
+-----------------------+----------------------------------------------------+
|is_private             | 0: Commentaire publique, 1: Commentaire privé      |
+-----------------------+----------------------------------------------------+

PUT
__________

Cette méthode permet d'attacher un commentaire à une entité de type noeud

*GET: /api/comment/comment*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+-----------------------------------------------------------+
|  Clé              |   Valeur                                                  |
+===================+===========================================================+
|    nid*           |N° du noeud                                                |
+-------------------+-----------------------------------------------------------+
|    subject*       |Titre du commentaire                                       |
+-------------------+-----------------------------------------------------------+
|    body*          |Contenu du commentaire (format HTML)                       |
+-------------------+-----------------------------------------------------------+
|    is_private     |0: Commentaire publique, 1: Commentaire privé (défaut : 0) |
+-------------------+-----------------------------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+----------------------------------------------------+
|   Clé                 |   Valeur                                           |
+=======================+====================================================+
|cid                    | N° du commentaire                                  |
+-----------------------+----------------------------------------------------+

Ressource : space
**********************

Cette ressource permet d'intéragir avec les *Organic Groups* de Drupal de type comment. Ces derniers représentent ce que l'on appelle des *espaces collaboratifs*

Action : space
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir basiquement avec les *Organic Groups* de Drupal.

PUT
__________

Cette méthode permet de créer un *espace collaboratif* en passant par le mécanisme Drupal

*PUT: /api/space/space*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+----------------------------------------------+
|  Clé              |   Valeur                                     |
+===================+==============================================+
|    gid*           |N° de noeud de l'espace parent                |
+-------------------+----------------------------------------------+
|    title*         |Titre du nouvel espace                        |
+-------------------+----------------------------------------------+
|    body           |Contenu de l'accueil de l'espace (format HTML)|
+-------------------+----------------------------------------------+


*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+----------------------------------------------------+
|   Clé                 |   Valeur                                           |
+=======================+====================================================+
|gid                    | N° de l'espace crée                                |
+-----------------------+----------------------------------------------------+

Action : member
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir basiquement avec les membres des *Organic Groups* de Drupal.

PUT
__________

Permet d’ajouter un membre (utilisateur ou une liste d’utilisateurs) dans un espace avec un rôle.

*PUT: /api/space/member*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+------------------------+-------------------------------------------------------------+
|  Clé                   |   Valeur                                                    |
+========================+=============================================================+
|    gid*                |N° de noeud de l'espace                                      |
+------------------------+-------------------------------------------------------------+
|    role*               |Rôle de l'utilisateur                                        |
+------------------------+-------------------------------------------------------------+
|    uid OU ul_node_id*  |Identifiant de l'utilisateur OU de la liste d'utilisateurs   |
+------------------------+-------------------------------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-------------------+----------------------------------------+
|   Clé             |   Valeur                               |
+===================+========================================+
|     uid           |N° de l’utilisateur                     |
+-------------------+----------------------------------------+

PATCH
__________

Permet de mettre à jour le rôle d’un membre (utilisateur ou liste d'utilisateurs) d’un espace.

*PATCH: /api/space/member*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+------------------------+-------------------------------------------------------------+
|  Clé                   |   Valeur                                                    |
+========================+=============================================================+
|      gid*              |N° de noeud de l'espace                                      |
+------------------------+-------------------------------------------------------------+
|      new_role*         |Nouveaux rôles des utilisateurs                              |
+------------------------+-------------------------------------------------------------+
|    uid OU ul_node_id*  |Identifiant de l'utilisateur OU de la liste d'utilisateurs   |
+------------------------+-------------------------------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-------------------+----------------------------------------+
|   Clé             |   Valeur                               |
+===================+========================================+
|        uid        |N° de l’utilisateur                     |
+-------------------+----------------------------------------+

DELETE
__________

Cette méthode permet de retirer un membre (un utilisateur ou une liste d'utilisateurs) d’un espace.

*DELETE: /api/space/member*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+------------------------+-------------------------------------------------------------+
|  Clé                   |   Valeur                                                    |
+========================+=============================================================+
|      gid*              |N° de noeud de l'espace                                      |
+------------------------+-------------------------------------------------------------+
|    uid OU ul_node_id*  |Identifiant de l'utilisateur OU de la liste d'utilisateurs   |
+------------------------+-------------------------------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-------------------+-------------------------------------------+
|   Clé             |   Valeur                                  |
+===================+===========================================+
|        uid        |N° de l’utilisateur                        |
+-------------------+-------------------------------------------+
|      status       |OK si tout s'est bien passé                |
+-------------------+-------------------------------------------+

Action : members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir basiquement avec les *Organic Groups* de Drupal.

GET
__________

Cette méthode permet de récupérer les membres d’un espace.

*GET: /api/space/members*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-------------------+----------------------------------------+
|  Clé              |   Valeur                               |
+===================+========================================+
|    nid*           |N° du noeud                             |
+-------------------+----------------------------------------+


*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-------------------+----------------------------------------------------+
|   Clé             |   Valeur                                           |
+===================+====================================================+
|     uid           |Identifiant de l'utilisateurs                       |
+-------------------+----------------------------------------------------+
|     name          |Username de l'utilisateur                           |
+-------------------+----------------------------------------------------+

Ressource : taxonomy
**********************

Cette ressource permet d'intéragir avec la taxonomy de Drupal. La taxonomy permets d'associer des *termes* à un contenu (exemple : catégorie, importance...) 

Action : terms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec les *termes* de la taxonomy de Drupal.

GET
__________

Cette méthode permet de récupérer les *termes* de taxonomy associés à un vocabulaire

.. NOTE:: Les valeurs de *vocabulary_name* disponibles peuvent être récupérés depuis l'action vocabularies. Exemple de valeurs exploitables : category, criticity, tags

*GET: /api/taxonomy/terms*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+----------------------------------------------+
|  Clé              |   Valeur                                     |
+===================+==============================================+
|  vocabulary_name* |Nom du vocabulaire                            |
+-------------------+----------------------------------------------+


*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+-----------------------------------------------------------+
|   Clé                 |   Valeur                                                  |
+=======================+===========================================================+
|term_name              | Tableau contenant l'ID du terme et certaines informations |
+-----------------------+-----------------------------------------------------------+

Action : vocabularies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec les *vocabularies* de la taxonomy de Drupal.

GET
__________

Cette méthode permet de récupérer les *vocabularies* de la taxonomy de Drupal

*GET: /api/taxonomy/vocabularies*

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+----------------------------------------------------------------+
|   Clé                 |   Valeur                                                       |
+=======================+================================================================+
|vocabulary_name        | Tableau contenant l'ID du vocabulary et certaines informations |
+-----------------------+----------------------------------------------------------------+

Ressource : user
**********************

Cette ressource permet d'intéragir avec les entités *user* de Drupal. Ces entités représentent les utilisateurs enregistrés sur la plateforme.

Action : autocomplete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec le système d'autocomplétion des entités *user* de Drupal.

GET
__________

Cette méthode permet de récupérer une liste d'utilisateurs en fonction de la chaine passée en saisie.

*GET: /api/user/autocomplete*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+----------------------------------------------+
|  Clé              |   Valeur                                     |
+===================+==============================================+
|  str*             |Input                                         |
+-------------------+----------------------------------------------+


*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+-----------------------------------------------------------+
|   Clé                 |   Valeur                                                  |
+=======================+===========================================================+
|uid                    | Quelques informations de base sur l'utilisateur           |
+-----------------------+-----------------------------------------------------------+

Ressource : locations
**********************

Cette ressource permet d'intéragir avec les emplacements disponibles sur Alfresco (l'ensemble des dossiers et espaces d'un point de vue GED uniquement)

Action : tree
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet de récupérer un *tree* d'emplacements au format JSON compatible avec le composant ZTree.

POST
__________

Cette méthode permet de récupérer un *tree* d'emplacements au format JSON compatible avec le composant ZTree.

*GET: /api/locations/tree*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+----------------------------------------------+
|  Clé              |   Valeur                                     |
+===================+==============================================+
|ename              | Chemin à partir duquel récupérer les enfants |
+-------------------+----------------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+----------------------------------------------------------------------+
|   Clé                 |   Valeur                                                             |
+=======================+======================================================================+
|tree                   | Chaine au format JSON directement exploitable par la librairie ZTree |
+-----------------------+----------------------------------------------------------------------+

Ressource : kanban
**********************

Cette ressource permet d'intéragir avec les tâches d'un utilisateur.

Action : user_task
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette ressource permet d'intéragir avec les tâches d'un utilisateur.

GET
__________

Cette méthode permet de récupérer les tâches de l'utilisateur.

*GET: /api/kanban/user_task*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+


*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+----------------------------------------------------------------------+
|   Clé                 |   Valeur                                                             |
+=======================+======================================================================+
|tasks                  |Tableau contenant la liste des tâches                                      |
+-----------------------+----------------------------------------------------------------------+

Ressource : search
**********************

Cette ressource permet d'intéragir avec les recherches documentaires.

Action : search
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'effectuer une recherche documentaire.

POST
__________

Cette méthode permet d'effectuer une recherche documentaire.

.. NOTE:: Les valeurs de *filters* disponibles sont les suivantes :
        ds_created (date de création) => [YYYY-MM-DDTHH:MM:SSZ TO YYYY-MM-DDTHH:MM:SSZ] date au format ISO 8601
        ds_changed (date de modification) => [YYYY-MM-DDTHH:MM:SSZ TO YYYY-MM-DDTHH:MM:SSZ] date au format ISO 8601
        sm_unr_document_reference (référence du document) => valeur
        im_field_format (format du document) => Identifiant du terme de la taxonomy *format* (cf. API taxonomy)
        im_field_tags (tags du document) => Identifiant du terme de la taxonomy *tags* (cf. API taxonomy)
        im_field_category (catégorie du document) => Identifiant du terme de la taxonomy *category* (cf. API taxonomy)
        sm_og_group_content_ref (Espace dans lequel rechercher) => node:xx Identifiant de l'espace dans lequel rechercher
        is_uid (utilisateur créateur) => Identifiant de l'utilisateur
        is_mod_uid (utilisateur modificateur) => Identifiant de l'utilisateur
        sm_unr_author (auteur du document) => valeur
        im_field_state (état du document) => Identifiant du terme de la taxonomy *state* (cf. API taxonomy)
        im_field_criticity (importance du document) => Identifiant du terme de la taxonomy *criticity* (cf. API taxonomy)
        ss_language (langue du document) => valeur (fr, en, ...)
        ds_field_date (échéance du document) => [YYYY-MM-DDTHH:MM:SSZ TO YYYY-MM-DDTHH:MM:SSZ] date au format ISO 8601

*POST: /api/search/search*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+-----------------------------------------------------------+
|  Clé              |   Valeur                                                  |
+===================+===========================================================+
|        query      |Texte à rechercher                                         |
+-------------------+-----------------------------------------------------------+
|      filters      |Tableau de filtres de recherche                            |
+-------------------+-----------------------------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+----------------------------------------------------------------------+
|   Clé                 |   Valeur                                                             |
+=======================+======================================================================+
|[Tableau de résultats] |Tableau contenant les 10 premiers résultats                           |
+-----------------------+----------------------------------------------------------------------+
|results                |Nombre total de résultats                                             |
+-----------------------+----------------------------------------------------------------------+

Ressource : userlist
**********************

Cette ressource permet d'intéragir avec les listes d'utilisateurs.

Action : userlist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet d'intéragir avec les listes d'utilisateurs.

GET
__________

Cette méthode permet de récupérer les informations d’une liste d'utilisateurs.

*GET: /api/userlist/userlist*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+----------------------------------------------+
|  Clé              |   Valeur                                     |
+===================+==============================================+
|nulid              |N° de noeud d'une liste d'utilisateurs        |
+-------------------+----------------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+----------------------------------------------------------------------+
|   Clé                 |   Valeur                                                             |
+=======================+======================================================================+
|title                  |Nom de l'userlist                                                     |
+-----------------------+----------------------------------------------------------------------+
|users                  |Liste des membres                                                     |
+-----------------------+----------------------------------------------------------------------+
|admin                  |Liste des administrateur                                              |
+-----------------------+----------------------------------------------------------------------+

PUT
__________

Cette méthode permet de créer une liste d'utilisateurs.

*PUT: /api/userlist/userlist*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+----------------------------------------------+
|  Clé              |   Valeur                                     |
+===================+==============================================+
|title              |Titre de la liste d'utilisateurs              |
+-------------------+----------------------------------------------+
|description        |Description de la liste d'utilisateurs        |
+-------------------+----------------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+----------------------------------------------------------------------+
|   Clé                 |   Valeur                                                             |
+=======================+======================================================================+
|title                  |Nom de la liste d'utilisateurs                                        |
+-----------------------+----------------------------------------------------------------------+
|nid                    |N° de noeud de la liste d'utilisateurs                                |
+-----------------------+----------------------------------------------------------------------+
|type                   |Type de la liste d'utilisateurs                                       |
+-----------------------+----------------------------------------------------------------------+
|created                |Date de création de la liste d'utilisateurs                           |
+-----------------------+----------------------------------------------------------------------+
|creator_id             |N° du créateur de la liste d'utilisateurs                             |
+-----------------------+----------------------------------------------------------------------+

PATCH
__________

Cette méthode permet de mettre à jour une liste d'utilisateurs.

*PATCH: /api/userlist/userlist*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+----------------------------------------------+
|  Clé              |   Valeur                                     |
+===================+==============================================+
|nulid              |N° de noeud de la liste d'utilisateurs        |
+-------------------+----------------------------------------------+
|title              |Nouveau titre de la liste d'utilisateurs      |
+-------------------+----------------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+----------------------------------------------------------------------+
|   Clé                 |   Valeur                                                             |
+=======================+======================================================================+
|new_title              |Nouveau titre de la liste d'utilisateurs                              |
+-----------------------+----------------------------------------------------------------------+
|status                 |Statut de la liste d'utilisateurs                                     |
+-----------------------+----------------------------------------------------------------------+

Action : admins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet aux administrateur de gérer la liste d'utilisateurs.

PUT
__________

Cette méthode permet d'ajouter un administrateur la liste d'utilisateurs.

*PUT: /api/userlist/admins*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+----------------------------------------------+
|  Clé              |   Valeur                                     |
+===================+==============================================+
|nulid              |N° de noeud de la liste d'utilisateurs        |
+-------------------+----------------------------------------------+
|uid                |Identifiant de l'utilisateur                  |
+-------------------+----------------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-------------------+----------------------------------------+
|   Clé             |   Valeur                               |
+===================+========================================+
|status             |Statut de l'ajout                       |
+-------------------+----------------------------------------+


Action : members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cette action permet aux membres d'accéder à la liste d'utilisateurs.

GET
__________

Cette méthode permet de récupérer la liste des membres de la liste d'utilisateurs.

*GET: /api/userlist/members*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+----------------------------------------------+
|  Clé              |   Valeur                                     |
+===================+==============================================+
|nulid              |N° de noeud d'une liste d'utilisateurs        |
+-------------------+----------------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+----------------------------------------------------------------------+
|   Clé                 |   Valeur                                                             |
+=======================+======================================================================+
|uid                    |N° de l'utilisateur                                                   |
+-----------------------+----------------------------------------------------------------------+
|username               |Nom d'utilisateur                                                     |
+-----------------------+----------------------------------------------------------------------+
|display_name           |Nom d'affichage de l'utilisateur                                      |
+-----------------------+----------------------------------------------------------------------+

PUT
__________

Cette méthode permet d'ajouter un membre à la liste d'utilisateurs.

*PUT: /api/userlist/members*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|Content-Type       | application/json         |
+-------------------+--------------------------+

+-------------------+----------------------------------------------+
|  Clé              |   Valeur                                     |
+===================+==============================================+
|nulid              |N° de noeud de la liste d'utilisateurs        |
+-------------------+----------------------------------------------+
|uid                |Identifiant de l'utilisateur                  |
+-------------------+----------------------------------------------+

*Retour:*

+-------------------+----------------------------------------+
|   Header          |   Valeur                               |
+===================+========================================+
|Content-Type       | application/json                       |
+-------------------+----------------------------------------+

+-----------------------+----------------------------------------------------------------------+
|   Clé                 |   Valeur                                                             |
+=======================+======================================================================+
|status                 |Statut de l'ajout                                                     |
+-----------------------+----------------------------------------------------------------------+

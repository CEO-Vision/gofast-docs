********************************************
GoFAST :  API REST 
********************************************

L'API REST de GoFAST permet aux développeurs d'intéragir avec l'application de manière applicative. Vous trouverez sur cette page toutes les informations nécessaires à l'exploitation de cette API.

Ressources
############################################

Ressource : node
**********************

Cette ressource permet d'intéragir avec les entités Drupal de type noeud. Ces derniers peuvent représenter des documents, articles, espaces, formulaires...

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

*GET: /api?ressource=node&action=content*

+-------------------+--------------------------+
|  Header           |   Valeur                 |
+===================+==========================+
|    nid*           |N° du noeud               |
+-------------------+--------------------------+
|Content-Type       | application/octet-stream |
+-------------------+--------------------------+
|Content-Disposition| attachment               |
+-------------------+--------------------------+
********************************************
GoFAST :  GOFAST WEBHOOK
********************************************

Le module GoFast Webhook permet l'intégration entre GoFast et des systèmes et applications tiers.
Dans cette page, vous trouverez toutes les informations sur la façon d'utiliser ce module pour alimenter des systèmes tiers en données à partir de la plateforme Gofast.

#################
Principes de base
#################
L'objectif du module Gofast Webhook est d'envoyer des informations spécifiques sur les nœuds à n'importe quel service qui s'y abonne
à travers sa simple configuration json qui se trouve dans une variable drupal sur l'instance de la plateforme Gofast.

Le module envoie une requête post à un service de la configuration pour lui notifier l'événement qui vient de se produire.
Les événements qui peuvent être notifiés sont les suivants :

- Création d'un nœud
- Mise à jour d'un nœud
- Suppression d'un nœud
- Publication d'un nœud
- Nœud de dépublication

###########################
 Configuration de services
###########################
Vous trouverez ci-dessous un exemple de configuration au format json :

.. code-block:: json
  
    [
      {
        "api_services": {
          "service_name": "GoFast creation webhook",
          "api_endpoint": "{service_url}",
          "events": [
            "CREATE"
          ],
          "method": "POST",
          "api_auth": {
            "type": "Bearer",
            "value": "{bearer_token_here}",
            "in_header": true,
          }
        }
      }
    ]

Comme vous pouvez le voir dans l'exemple ci-dessus, la configuration est un tableau de services. 
Chaque service possède les propriétés suivantes :

- ``api_services``: Il s'agit du nom du service. Il est utilisé pour identifier le service auquel l'événement sera envoyé.
- ``api_endpoint``: Il s'agit de l'adresse URL du service auquel l'événement sera envoyé.
- ``events``: Il s'agit d'un tableau d'événements qui seront envoyés au service. Les valeurs possibles sont les suivantes : ``CREATE``, ``UPDATE``, ``DELETE``.
- ``method``: Il s'agit de la méthode HTTP à utiliser pour envoyer l'événement au service. Il convient d'utiliser une méthode acceptée par le service tiers. Les valeurs possibles sont les suivantes : ``POST``, ``PUT``, ``PATCH``, ``DELETE``.
- ``api_auth``: Il s'agit de la configuration d'authentification à utiliser pour envoyer l'événement au service. Il s'agit d'un objet ayant les propriétés suivantes :

  - ``type``: Il s'agit du type d'authentification à utiliser. Les valeurs possibles sont les suivantes : ``Bearer``, ``Basic``.
  - ``value``: Il s'agit de la valeur de l'authentification à utiliser. Il s'agit du jeton qui dépend du type d'authentification.
  - ``in_header``: Il s'agit d'un booléen qui indique si l'authentification doit être envoyée dans l'en-tête ou dans le corps de la demande.
 
###########################
 Réglage de la configuration
###########################

Vous vous demandez peut-être comment définir la configuration. C'est très simple. Vous avez juste besoin de définir la configuration dans une variable Drupal.
Le nom de la variable est ``gofast_webhook_config``. Vous pouvez la configurer de différentes manières. L'une d'entre elles consiste à utiliser le module devel
et de la définir dans la page devel/php. Une autre façon est d'utiliser l'outil de ligne de commande drush. Vous pouvez utiliser la commande suivante pour définir la configuration :

Commandement Drush :
~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    drush @d7 vset gofast_webhook_config '{
      "api_services": {
        "service_name": "GoFast creation webhook",
        "api_endpoint": "{service_url}",
        "events": [
          "CREATE"
        ],
        "method": "POST",
        "api_auth": {
          "type": "Bearer",
          "value": "{bearer_token_here}",
          "in_header": true,
        }
      }
    }'

Sortie :
##########
.. code-block:: text

    La variable gofast_webhook_config a été réglée sur '[{"api_services": ...'
    
Configuration à l'aide du module Drupal Devel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour configurer la même commande en utilisant le module PHP Devel dans Drupal, suivez les étapes suivantes :

1. **Installation et activation du module Devel:**
   Si ce n'est pas déjà fait, installez et activez le module Devel sur votre site Drupal. Vous pouvez le faire via l'interface d'administration de Drupal ou en utilisant les commandes Drush.

2. **Accéder à la page Exécuter le code PHP:**
   Une fois Devel installé et activé, naviguez jusqu'au chemin suivant :
   ``Admin > Configuration > Développement > Exécuter le code PHP``.

3. **Entrez le code PHP:**
   Dans la page "Exécuter le code PHP", saisissez le code PHP ci-dessous dans la zone de texte prévue à cet effet :

   .. code-block:: php

      $config = [
        'api_services' => [
          'service_name' => 'GoFast creation webhook',
          'api_endpoint' => '{service_url}',
          'events' => ['CREATE'],
          'method' => 'POST',
          'api_auth' => [
            'type' => 'Bearer',
            'value' => '{bearer_token_here}',
            'in_header' => true,
          ]
        ]
      ];

      variable_set('gofast_webhook_config', json_encode($config));

4. **Exécuter le code PHP:**
   Cliquez sur le bouton "Exécuter" de la page pour exécuter le code PHP.
   
Une fois que le code a été exécuté avec succès, vous verrez une barre verte en haut de la page avec le message "Le code a été exécuté avec succès".

Une future version du module fournira une interface utilisateur graphique pour ajouter et supprimer des services. Pour l'instant, vous pouvez utiliser les méthodes ci-dessus pour ajouter et supprimer des services.

.. CAUTION:: Veuillez noter que la configuration sera validée par le module et que si elle n'est pas valide, le module n'enverra aucun événement aux services configurés.

###################################
Activation du module Gofast Webhook
###################################

Si le module n'est pas déjà installé et activé, vous pouvez le faire en suivant les étapes ci-dessous :

- **Activer le module:**
   Activez le module en exécutant la commande Drush suivante :

   .. code-block:: console

      drush @d7 en gofast_webhook -y

- **Vider le cache:**
    Effacez le cache en exécutant la commande Drush suivante :
  
    .. code-block:: console
  
        drush @d7 cc all

Vous pouvez également le faire via l'interface d'administration de Drupal en naviguant vers le chemin suivant :
``Admin > Modules``. 

Le module Gofast Webhook sera installé et activé sur votre instance Gofast et commencera à envoyer des événements aux services configurés ci-dessus.

###################################
Demandes envoyées aux services
###################################

Lorsque le module est activé avec succès, il est déclenché par l'un des événements spécifiés dans la configuration. Dans ce cas, le module envoie une requête aux services configurés. La requête envoyée à CHAQUE service est une requête POST avec le corps JSON suivant :

Le Content-Type est 'application/json'
Tous les champs ont des valeurs de type chaîne

.. code-block:: json

    {
      "operation": "CREATE",
      "gofast_nid": "1111",
      "title": "example.docx",
      "type": "alfresco_item",
      "created": "2023-06-28 15:27:39",
      "changed": "2023-06-28 15:27:39",
      "status": "1",
      "uid": "001",
      "alfresco_reference": "workspace://SpacesStore/{an_alfresco_reference}",
      "metadata": {
        "field_current_version": [
          {
            "value": "1.0"
          }
        ],
        "field_document_reference": [
          {
            "value": "odoo_service" 
          }
        ],
        "field_emplacement": [
          {
            "value": "/Sites/_Organisations/_ExampleSpace"
          }
        ],
        "field_filename": [
          {
            "value": "example.docx"
          }
        ],
        "field_main_emplacement": [
          {
            "value": "/Sites/_Organisations/_ExampleSpace"
          }
        ],
        "field_reference": [
          {
            "value": "workspace://SpacesStore/{an_alfresco_reference}"
          }
        ]
      }
    }

Champs de la demande Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    +--------------------+--------------------------------------------------------------+
    | Champ              | Description                                                  |
    +====================+==============================================================+
    | ``operation``      | Indique l'opération qui a déclenché l'événement.             |
    |                    | Valeurs possibles : ``CREATE``, ``UPDATE``, ``DELETE``.      |
    +--------------------+--------------------------------------------------------------+
    | ``gofast_nid``     | ID du nœud Gofast qui a déclenché l'événement.               |
    +--------------------+--------------------------------------------------------------+
    | ``title``          | Titre du nœud Gofast qui a déclenché l'événement.            |
    +--------------------+--------------------------------------------------------------+
    | ``type``           | Type de nœud Gofast qui a déclenché l'événement.             |
    +--------------------+--------------------------------------------------------------+
    | ``created``        | Date et heure du nœud Gofast qui a déclenché l'événement     |
    |                    | a été créé.                                                  |
    +--------------------+--------------------------------------------------------------+
    | ``changed``        | Date et heure du nœud Gofast qui a déclenché l'événement     |
    |                    | a été modifié pour la dernière fois.                         |   
    +--------------------+--------------------------------------------------------------+
    | ``status``         | État du nœud Gofast qui a déclenché l'événement.             |
    +--------------------+--------------------------------------------------------------+
    | ``uid``            | ID de l'utilisateur qui a créé le nœud Gofast qui            |
    |                    | a déclenché l'événement.                                     |
    +--------------------+--------------------------------------------------------------+
    | ``alfresco_        |                                                              |
    | reference``        | Référence Alfresco du nœud Gofast qui s'est déclenché        |
    |                    | l'événement.                                                 |
    +--------------------+--------------------------------------------------------------+
    | ``metadata``       | Contient les métadonnées du nœud Gofast qui s'est déclenché  |
    |                    | l'événement. Les métadonnées sont un tableau de champs et de |
    |                    | valeurs. Les noms des champs sont les mêmes que dans Gofast, |
    |                    | sont les valeurs des champs.                                 |
    +--------------------+--------------------------------------------------------------+

Le champ ``field_document_reference`` est un champ spécial qui est utilisé pour stocker la référence du document dans le système externe. Ce champ est utilisé pour déterminer si le document a déjà été envoyé au système externe. Si le champ est vide, le document n'a pas été envoyé au système externe. Si le champ est vide, le document a déjà été envoyé au système externe.

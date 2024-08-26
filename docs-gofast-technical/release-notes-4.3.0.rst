********************************************
GoFAST :  Version 4.3.0
********************************************

**[GoFAST Enterprise]** N’hésitez pas à solliciter notre support pour planifier la mise à jour.

Nouvelles fonctionnalités 
*****************************

.. csv-table::
   :header: "Ref.","Type", "Description"
   :widths: 1000, 2000, 60000

    "GOFAST-6807","Nouvelle fonctionnalité","Rajouter l'option de réunions récurrentes en web-conférence "
    "GOFAST-7248","Nouvelle fonctionnalité","Créer un écran de test des filtres AD pour faciliter la configuration de synchronisation "
    "GOFAST-11536","Nouvelle fonctionnalité","API Activation / Désactivation des Utilisateurs"
    "GOFAST-9870","Nouvelle fonctionnalité","Ajout de la la possibilité de changer les identifiants des utilisateurs "
   "GOFAST-12011","Nouvelle fonctionnalité","Publication d'un fichier DWG en PDF en plus de SVG "
    "GOFAST-3903","Nouvelle fonctionnalité","[OPTION] Possibilité de tamponer un PDF avec identifiant/date à l'étape de signature"
    "GOFAST-11208","Nouvelle fonctionnalité","[OPTION] Possibilité de tamponer un PDF avec identifiant/date à l'étape de validation"
    "GOFAST-4439","Nouvelle fonctionnalité","[TECHNIQUE] Conformité Profil sécurité ANSSI BP 28 Enhanced"
    "GOFAST-7469","Nouvelle fonctionnalité","[TECHNIQUE] Remplacement du système d'exploitation CentOS7 par Almalinux"

Note : Si indiqué [OPTION], il s'agit d'un module supplémentaire

Améliorations 
******************************

.. csv-table::
   :header: "Ref.","Type", "Description"
   :widths: 1000, 2000, 60000


    "GOFAST-7328","Amélioration","Ajout des polices Marianne, Arial Narrow, Montserrat, Century Gothic pour Onlyoffice et prévisualisation"
    "GOFAST-7892","Amélioration","Création des entités par liste administrable (remplacement du champ texte libre)"
    "GOFAST-8585","Amélioration","Annuaire Espaces : Possibilité de filtrer par nom les administrateurs des espaces"
    "GOFAST-9410","Amélioration","Possibilité d'ouverture des documents OnlyOffice de taille plus importante"
   "GOFAST-11797","Amélioration","Amélioration de l'UX pour la recherche avancée - multi-critères. "
   "GOFAST-11650","Amélioration","Mise à jour Onlyoffice 8.1.1. "
   "GOFAST-10069","Amélioration","Amélioration de la visibilité des formulaires "
    "GOFAST-10637","Amélioration","Pouvoir trier / filtrer par emplacement dans annuaire espace"
    "GOFAST-11002","Amélioration","Champ date 'personnalisé' : afficher la valeur dans les résultats de recherche"
    "GOFAST-11054","Amélioration","Pouvoir appliquer la règle de nommage sur tous les documents d'une même catégorie"
    "GOFAST-11430","Amélioration","Possibilité d'utiliser l'authentification à double facteur (2FA) pour les externes et SSO pour les internes"
    "GOFAST-11596","Amélioration","Passage de la date au format anglais Européen à selectionner dans la configuration"
    "GOFAST-11699","Amélioration","Ouverture du panneau latéral du chat lors d'un appel entrant"
    "GOFAST-11495","Amélioration","Exclusion des fichiers 7z de l'indexation"
    "GOFAST-11755","Amélioration","[TECHNIQUE] Mise en conformité d'Alfresco avec logrotate"
    "GOFAST-11842","Amélioration","[TECHNIQUE] Amélioration de performance "
    "GOFAST-9696","Amélioration","[TECHNIQUE] Optimisations lors création en masse de documents"
    "GOFAST-11092","Amélioration","[TECHNIQUE] Optimisation de la base de données en Alfresco 7"
    "GOFAST-11158","Amélioration","[TECHNIQUE] Optimisation du temps de traitement lors de la suppression d'utilisateurs"
    "GOFAST-11711","Amélioration","[TECHNIQUE] Maj Ckeditor 5 (éditeur riche)"
    "GOFAST-11987","Amélioration","[TECHNIQUE] Activation de la configuration SSRC rewriting de Jitsi "
    "GOFAST-11033","Amélioration","[TECHNIQUE] Item Zabbix pour identifier les processus tika ouverts depuis plus de X secondes / minutes"

Bugs 
******************************
.. csv-table::
   :header: "Ref.","Type", "Description"
   :widths: 1000, 2000, 60000


    "GOFAST-11429","Bug","[OUTLOOK] Réunion non ajoutée automatiquement dans l'agenda de l'organisateur"
    "GOFAST-11541","Bug","Réduction du temps d'attente lors de l'ajout d'un membre dans une liste importante"
    "GOFAST-11559","Bug","Rétablissement de l'icône 'Cloche' dans le chat pour les citations temps réelles"
   "GOFAST-11997","Bug","[ONLYOFFICE] Documents protégés par mot de passe : déverrouillage impossible avec une ancienne clé d'édition. "
   "GOFAST-11985","Bug","Règles de nommage : renommage en échec après retrait d'une règle "
   "GOFAST-11984","Bug","Le membre n'est pas visible dans la liste des membres d'un espace "
   "GOFAST-11982","Bug","Webform en lecture seule malgré un rôle de contributeur dans l'espace "   
   "GOFAST-11959","Bug","Date de modification affichée erronée dans certains cas "
   "GOFAST-11916","Bug","Notification de partage de documents : dans certains cas photo de profil erronée "
   "GOFAST-11911","Bug","Notifications de workflow : si un utilisateur n'a pas accès à un document, le lien vers le document doit être grisé "
   "GOFAST-11817","Bug","Commentaires : l'édition d'un ancien commentaire avec une personne mentionnée échoue lors de la sauvegarde "
   "GOFAST-11816","Bug","Si une étape personnalisée est assignée à une liste utilisateur, la bannette ne s'affiche plus "
   "GOFAST-11801","Bug","Compression/Décompression : correction de divers problèmes "
   "GOFAST-11783","Bug","Erreur de synchronisation avec l'annuaire LDAP "
   "GOFAST-11773","Bug","Le copié-collé d'une image reste bloqué sur 'Chargement d'une image' "
   "GOFAST-11771","Bug","Le 'lien vers cet emplacement' ne fonctionne pas dans un espace dont le titre contient un apostrophe (' ) "
   "GOFAST-11756","Bug","Gestion des erreurs liées à un mauvais nom de domaine pour une conférence démarrée via Element Web "
   "GOFAST-11657","Bug","Déconnexions en boucle sur Firefox "
   "GOFAST-11592","Bug","Dans l'audit, lors de l'utilisation d'un filtre sur un résultat, on ne revient pas à la page 1 "
   "GOFAST-11349","Bug","Il est possible d'éditer les listes d'utilisateurs même si elles sont synchronisées, ce qui entraîne la perte des modifications après sauvegarde "
   "GOFAST-11266","Bug","Redirection clic du lien de la fonction 'Partager par email' "
   "GOFAST-9984","Bug","Dépôt de fichiers .eml (Thunderbird macOS) impossible depuis un Mac "
   "GOFAST-11229","Bug","[ONLYOFFICE] Format des dates change lors de la publication en PDF d'un document Excel édité depuis Office365 "   
   "GOFAST-11095","Bug","Traduction des DUA non prises en compte dans les catégories du document "
    "GOFAST-10965","Bug","[TECHNIQUE] Mise en conformité de l'emplacement des logs d'Alfresco"
    "GOFAST-10982","Bug","[TECHNIQUE] Mise en conformité de l'emplacement des logs de Synapse (chat)"


Nouvelles fonctionnalités (R3)
*****************************

.. csv-table::
   :header: "Ref.","Type", "Description"
   :widths: 1000, 2000, 60000

   "GOFAST-11708","Nouvelle fonctionnalité","Formulaire : permettre le partage d'un formulaire avec des personnes sans compte, via email. "
   "GOFAST-5571","Nouvelle fonctionnalité","Refonte majeure des formulaires "
   

Améliorations (R3)
******************************

.. csv-table::
   :header: "Ref.","Type", "Description"
   :widths: 1000, 2000, 60000

   "GOFAST-11882","Amélioration","[TECHNIQUE] Pré implémentation et préparatifs pour le futur Framework technique VueJS "
   "GOFAST-10990","Amélioration","[TECHNIQUE] Pré implémentation et préparatifs pour le futur Framework technique Drupal 10 "


Bugs (R3)
******************************

.. csv-table::
   :header: "Ref.","Type", "Description"
   :widths: 1000, 2000, 60000

   "GOFAST-11629","Bug","[FIREFOX][LINUX] Edition en ligne ave LibreOffice impossible documents Office sans ITHit"

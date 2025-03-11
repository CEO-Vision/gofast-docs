********************************************
GoFAST :  Version 4.4.0
********************************************

**[GoFAST Enterprise]** N’hésitez pas à solliciter notre support pour planifier la mise à jour.

Nouvelles fonctionnalités 
*****************************

.. csv-table::
   :header: "Ref.", "Description"
   :widths: 1000, 60000

    "GOFAST-7126","Nouvelle fonctionnalité permettant la duplication des cartes Kanban"
    "GOFAST-5571","Nouveaux formulaires GoFAST (pouvoir créer des formulaires puissants mutli-lingues de sondage, quiz, ...)"
    "GOFAST-12582","Pouvoir ajouter des fichiers aux formulaires qui sont automatiquement versés dans GoFAST (dépôt de factures, CV, ...)"
    "GOFAST-12424","[YOUSIGN] Ajout d'un message de consentement à la création d'un workflow ""Diffusion de document"""
    "GOFAST-12356","Nouvelle fonctionnalité : pouvoir faire des quiz (calcul de bonnes réponses, chrono ...)"
    "GOFAST-12294","Utilitaire pour créer un plan de classement (espaces,sous-espaces) avec membres associés à partir d'un fichier excel"
    "GOFAST-12290","[IA] Ajout d'un plugin Onlyoffice d'IA souveraine basé sur Mistral (correction, traduction, ...) (module optionnel)"
    "GOFAST-12268","Ajout des liaisons de données externes dans Onlyoffice Tableur"
    "GOFAST-12165","Ajout de graphiques pour représenter les résultats des formulaires"
    "GOFAST-12161","Ajout de fonctions avancées pour les liens et les images dans l'éditeur enrichi"
    "GOFAST-12052","Mise en place des métadonnées pour les Espaces Collaboratifs"
    "GOFAST-12027","Ajout de la possibilité d’annoter directement les PDF en ligne via OnlyOffice"
    "GOFAST-11942","Passerelle Element/WhatsApp (OPTION)"
    "GOFAST-11940","Ajout du signataire et de la date sur le tampon Yousign"
    "GOFAST-11909","Compatibilité avec Element X"
    "GOFAST-11776","[IA] Nouvelle fonctionnalité d'anonymisation automatisée des documents par IA (module optionnel)"
    "GOFAST-11775","[IA] Possibilité d'hébergement Onpremise du modèle d'IA GoFAST"
    "GOFAST-11774","[IA] Nouvelle fonctionnalité de suggestion automatique des catégories de document par IA (module optionnel)"
    "GOFAST-11708","Ajout de la fonctionnalité de partage d’un formulaire avec des personnes sans compte GoFAST"
    "GOFAST-11098","Nouvelle fonctionnalité : module optionnel d'IA souveraine (Onpremise ou SaaS)"
    "GOFAST-6706","Tableau de bord Taches (Workflow et Kanban) - vue pilotage "
    "GOFAST-12274","[ONLYOFFICE][ENTERPRISE] Pouvoir modifier le contenu d'un PDF en ligne (nécessite OnlyOffice Enterprise)"    



Améliorations 
******************************

.. csv-table::

   :header: "Ref.","Description"
   :widths: 1000, 60000

    "GOFAST-8770","Personnalisation des couleurs des cartes Kanban"
    "GOFAST-6695","[YOUSIGN] Permettre de sélection l'emplacement de la ou des signatures lors du lancement du workflow"
    "GOFAST-12498","La prévisualisation des fichiers DWG est soumise à une limitation de taille"
    "GOFAST-12457","[TECHNIQUE] Supervision des iostats sur VM2 (Comm)"
    "GOFAST-12422","[TECHNIQUE] Mise à jour d'Element Web (GoFAST) : v1.11.90"
    "GOFAST-12390","Workflow : Changement de libellé ""Pour Signature"" devient ""Pour Signature (manuel)"""
    "GOFAST-12365","Workflow : dans les tâches ""Pour contribution""  seuls les utilisateurs ayant accès aux documents sont sélectionnables"
    "GOFAST-12341","[TECHNIQUE] Mise à jour AlmaLinux 9.5"
    "GOFAST-12298","Amélioration de l'éditeur riche des cartes Kanban (possibilité d'ajouter des images, ....)"
    "GOFAST-12171","Extension de la liste des catégories de documents avec l'ajout de 39 nouvelles catégories"
    "GOFAST-12169","Pouvoir modifier en masse les métadonnées spécifiques"
    "GOFAST-12168","Amélioration de la recherche avancée par la possibilité de mettre en masse dans le panier les fichiers sélectionnés"
    "GOFAST-12146","Amélioration du message de bannissement en cas de connexions échouées massives"
    "GOFAST-12103","[TECHNIQUE] Mise à jour de l'agent Zabbix en version 7"
    "GOFAST-12102","[TECHNIQUE] Indice qualité Apdex remonté sur Zabbix (alerte et valeur)"
    "GOFAST-12070","Amélioration du formulaire de login sur tablette si plusieurs méthodes d'authentification offertes"
    "GOFAST-12037","[R2][TECHNIQUE] MàJ Jitsi 2.0.9955"
    "GOFAST-12631","Passage de OnlyOffice v8.1.0 à v8.3.1 ( Possibilité de modifier le thème d’interface, possibilité de prévisualiser un fichier CSV dans un tableur ...)"
    "GOFAST-11924","[TECHNIQUE] Compatibilité API Yousign V3"
    "GOFAST-11908","[TECHNIQUE] Màj Matrix/Synapse 1.119+ compatible ElementX/ElementCall (2024-11-13) "
    "GOFAST-11824","Ajout de la possibilité de convertir les fichiers en d'autres formats (tous les formats convertibles par OnlyOffice)"
    "GOFAST-11767","Ajout de la possibilité d'ajouter des étiquettes et une couverture sur les cartes Kanban"
    "GOFAST-11151","Afficher l'expiration du mot de passe si activé dans la politique des mots de passe"
    "GOFAST-11097","Affichage d’un badge avec le nombre d’utilisateurs en coédition d'un document à côté du portrait de l’utilisateur ayant démarré la session"
    "GOFAST-10970","Rétablir le fonctionnement de JITSI et Element en environnement contraint (port 10000 fermé)"
    "GOFAST-10784","[YOUSIGN] Ajout de la fonctionnalité permettant d’ajouter des mentions sous les signatures"
    "GOFAST-12224","Installation de Element Call pour Element X"
    "GOFAST-7643","Refus explicite de la signature dans une notification de refus de signature Yousign"
    "GOFAST-12460","Depot des documents broadcasté dans un repertoire dedié"
    "GOFAST-12527","[DIGITALSIGN] : Améliorer la sélection de l'emplacement de signature lors de la création du WF"
    "GOFAST-12338","Pouvoir comparer les versions des documents html"
    "GOFAST-12441","Profil Qualification habilité ""Confidentiel"""
    "GOFAST-12447","Toujours afficher le formulaire de remplissage des métadonnées d'un document"
    "GOFAST-12449","Tableau de bord : avoir une vue globale des espaces dont on est Responsable (métadonnée sur Espace)"
    "GOFAST-12461","Duplication des métadonnées de l'espace parent à l'espace enfant"
    "GOFAST-12462","Pouvoir faire un export Excel de l’Audit d'un Espace en tant que support utilisateur"
    "GOFAST-12476","Créer un document word à partir des résultats des formulaires"



Bugs 
******************************

.. csv-table::
   :header: "Ref.","Description"
   :widths: 1000, 60000

    "GOFAST-12525","Correction d'un bug rendant impossible d'exporter tous les résultats d'audit si il y a un filtre actif"
    "GOFAST-12504","Correction d'un bug qui empêche l'affichage de la liste d'utilisateurs dans l'autocompletion d'ajout à un espace"
    "GOFAST-12496","Correction d'un bug qui empêchait la recherche par nom et prénom dans les filtres de la recherche avancée"
    "GOFAST-12491","Correction d'un bug empêchant la synchronisation des listes utilisateurs si dans la configuration synchro LDAP erronnée"
    "GOFAST-12458","[ELEMENT][RETEST] Le partage d'écran met fin à l'appel 1 to 1 (à reformuler si ca fonctionne)"
    "GOFAST-12420","Correction d'un bug aléatoire de téléversement sur le chat"
    "GOFAST-12418","Correction d'un bug ignorant le scoring de proximité lors d'une recherche non-stricte avec le filtre ""uniquement dans le titre"""
    "GOFAST-12394","Correction d'un bug visuel sur les filtres de l'annuaire des espaces"
    "GOFAST-12326","Correction d'un bug perdant la mise en forme d'un commentaire d'une nouvelle version de document"
    "GOFAST-12285","Correction d'un bug de duplication des colonnes dans l'onglet tâche des espaces"
    "GOFAST-12279","[ESSENTIAL] Correction d'un bug empêchant le changement d'onglet dans le bloc de métadonnées dans un document"
    "GOFAST-12201","Correction de bug intermittant Element sur les rôles et les membres dans les salons textuels d'espaces"
    "GOFAST-12198","Correction d'un bug qui rendait possible le partage (mirroring) du dossier FOLDERS TEMPLATES"
    "GOFAST-12197","Correction d'un bug : les utilisateurs connectés ne sont pas affichés dans les statistiques d'espaces"
    "GOFAST-12177","Correction d'un bug affichant un message parasite de changement de mot de passe si une politique de sécurité des mots de passe est appliquée"
    "GOFAST-12172","Correction d'un bug qui forçait la réouverture de fichiers venant d'être fermés dans l'arborescence"
    "GOFAST-12167","Correction d'un bug qui empechait la suppression de toute liste dans le champ ""Archiviste"" pour la DUA"
    "GOFAST-12154","Correction d'un bug enlevant quelques secondes le verrou en coédition OnlyOffice lors d'un CTRL-S"
    "GOFAST-12138","Correction d'un bug empechant la sauvegarde d'un document Onlyoffice dans le cas d'une erreur en base de données"
    "GOFAST-12128","Correction d'un bug qui empêchait la gestion des métadonnées en masse depuis le panier"
    "GOFAST-12113","Correction d'un bug qui bloque le mail de signature pour les adresses mails de contact déjà associées à un utilisateur"
    "GOFAST-12076","Correction d'un bug empêchant la comparaison des fichiers aux formats .pptx"
    "GOFAST-12071","Correction d'un bug empechant le chargement de fichiers sur iPad (zone basse de l'explorateur)"
    "GOFAST-12069","Correction d'un bug empêchant le filtrage dans la modale des membres autorisés sur un document"
    "GOFAST-12016","Correction d'un problème empechant le filtrage des catégorie dans l'écran de la DUA"
    "GOFAST-11984","Correction d'un bug empéchant l'affichage des membres dans un espace si un zoom navigateur est appliqué"
    "GOFAST-11913","Correction d'un bug qui permettait (sur certains actions) le multi-emplacement d'un document dans un répertoire mirroir"
    "GOFAST-11867","Correction d'un bug affichant dans certains cas la prévisualisation de la version précédente juste après une édition"
    "GOFAST-11832","Correction d'un bug OnlyOffice sur le publipostage à partir de fichier .xlsx"
    "GOFAST-11615","Correction d'un bug ouvrant 2 sessions OnlyOffice séparées (ex.ouverture quasi simultannée d'un même doc, ...)"
    "GOFAST-11433","Correction d'un bug qui dupliquait les catégories"
    "GOFAST-12503","Correction d'une possible fuite mémoire induite par Element"
    "GOFAST-10024","[MS-OFFICE] L'édition en ligne avec Office ne fonctionne plus (Désactivation de l'authentification de base par Microsoft)"
    "GOFAST-12569 ","Correction d'un bug empechant le scroll dans l'onglet ""Versions"""

Sécurité 
******************************
**[GoFAST Enterprise]** Contactez-nous pour obtenir la liste des correctifs sécurité  

********************************************
GoFAST :  Version 4.5.0
********************************************

**[GoFAST Enterprise]** N’hésitez pas à solliciter notre support pour planifier la mise à jour.

Nouvelles fonctionnalités 
*****************************

.. csv-table::
   :header: "Ref.", "Description"
   :widths: 1000, 60000

    "GOFAST-13032","Ajout d'un accès direct aux formulaires sur mobile"
    "GOFAST-12449","Dans le tableau de bord, ajout de la vue ""Espaces à ma charge"" basée sur la métadonnée ""Responsable"" associée à l’utilisateur"
    "GOFAST-12461","Duplication des métadonnées de l'espace parent à l'espace enfant"
    "GOFAST-13160","[IA] Intégration d’un Chat avec un Chatbot IA (Prompt Mistral dans Element)"
    "GOFAST-13158","[IA] Pouvoir limiter l'usage du module IA à certains espaces"
    "GOFAST-12523","Paramétrage pour désactiver l’accès au chat sur GoFAST"
    "GOFAST-12447","Pouvoir afficher systématiquement le formulaire de métadonnées lors de la création d’un document"
    "GOFAST-12462","Pouvoir exporter au format Excel ou CSV l’audit d’un espace depuis l’onglet dédié"
    "GOFAST-7774","Prévisualisation des fichiers Markdown"
    "GOFAST-12441","Profil “Qualification habilité Confidentiel” pour accès aux espaces confidentiels"
    "GOFAST-5316","Restauration d'espaces supprimés"
    "GOFAST-6706","Tableau de bord Taches (Workflow et Kanban) : vue pilotage "


Améliorations 
******************************

.. csv-table::
   :header: "Ref.","Description"
   :widths: 1000, 60000

    "GOFAST-11605","Règles Contenus Confidentiel/Interne appliquées sur Classification (en plus d'Importance) "
    "GOFAST-11710","Dans le calendrier d’un espace, pouvoir afficher les événements des calendriers des espaces enfants "
    "GOFAST-12037","[TECHNIQUE] MàJ Jitsi 2.0.10184 "
    "GOFAST-12274","[ONLY OFFICE] Pouvoir modifier le contenu d'un PDF en ligne "
    "GOFAST-12460","Depot des documents broadcasté dans un repertoire dedié "
    "GOFAST-12527","[DIGITALSIGN] Amélioration de la sélection des emplacements de signature lors de la création d'un workflow (Digitalsign) "
    "GOFAST-12591","Ajout de la métadonnée ""Responsable"" sur les espaces et documents "
    "GOFAST-12616","Ajout de l'option de partage par email pour les formulaires "
    "GOFAST-12790","Ajout de la classification de confidentialité dans les métadonnées d’espace "
    "GOFAST-12823","Ajout de la métadonnée ""Date d’échéance"" pour les espaces "
    "GOFAST-12829","Ajout de la métadonnée ""État"" pour les espaces "
    "GOFAST-12878","La valeur ""En cours"" peut être automatiquement attribuée à la métadonnée ""État"" lors de la création d’un espace. "
    "GOFAST-13146","[TECHNIQUE] MàJ Onlyoffice 9.x : Nouveaux thèmes d'interface, correction de différents bugs... "
    "GOFAST-7280","Ajout de restrictions supplémentaires sur les contenus confidentiels (édition et impression) "
    "GOFAST-7643","[YOUSIGN] Refus explicite de la signature dans une notification de refus de signature Yousign"


Bugs 
******************************

.. csv-table::
   :header: "Ref.","Description"
   :widths: 1000, 60000

    "GOFAST-10024","[MS-OFFICE] Correction d'un bug d'édition en ligne avec Office (Désactivation de l'authentification de base) "
    "GOFAST-12590","Correction d'un bug sur l’activation des comptes ""en attente"" après synchronisation des annuaires "
    "GOFAST-12662","Correction d'un bug de chargement infini sur les documents sans workflow actif "
    "GOFAST-12701","Correction d'un bug dans l'URL de réunion dans l'invitation, affichant des informations erronées sur les participants "
    "GOFAST-12802","Correction d'un bug dans l'éditeur riche dans le Kanban : la mise en forme ferme l'éditeur et enregistre les modifications "
    "GOFAST-12807","Correction de l’affichage des échéances Kanban dans le calendrier pour les lundis "
    "GOFAST-12809","Correction d’un bug lié au message d’erreur ""Impossible de restaurer la session"" dans Element "
    "GOFAST-12826","Correction d'un bug qui rendait non fonctionnelle la connexion LDAP en cas de liaison sans identifiant (Bind Anonymous) "
    "GOFAST-12827","Correction d'un bug affichant l’audit sur tous les commentaires lors de l’édition d’un seul "
    "GOFAST-12838","Correction d'un bug bloquant l’indexation des documents DOCX créés depuis la plateforme "
    "GOFAST-12906","[PASTELL] Correction d'un bug sur le connecteur Pastell "
    "GOFAST-12929","Correction d'un bug sur le mot de passe du compte ‘admin’ Alfresco qui expire si une politique d’expiration LDAP est activée "
    "GOFAST-12936","Correction d'un bug rendant impossible de créer un utilisateur avec SASL activé (depuis la synchronisation LDAP ou l'interface) "
    "GOFAST-12940","Correction d'un bug rendant les filtres non fonctionnels dans la recherche avancée (espaces, catégories...) "
    "GOFAST-12949","Correction d'un bug remontant ""admin"" dans l'audit quand synchronisation LDAP "
    "GOFAST-12977","Correction d'un bug entrainant l'échec de l’ajout LDAP lors de la création d’un utilisateur avec l’option SASL activée "
    "GOFAST-12983","Blocage temporaire d’Element X côté serveur pour éviter les conflits avec Element Legacy "
    "GOFAST-12987","Correction d'un bug empêchant d'intégrer Element dans une iframe depuis un autre nom de domaine "
    "GOFAST-13008","Correction d’un bug de visibilité incohérente des utilisateurs dans l'annuaire "
    "GOFAST-13050","[ESSENTIAL] Correction d'un bug sur la recherche "
    "GOFAST-13167","Correction d’un bug empêchant l’ouverture directe d’un dossier partagé par email, même si l’utilisateur dispose des droits d’accès "
    "GOFAST-13180","[YOUSIGN] Correction d'une erreur de libellé pour les signatures YouSign"

Sécurité 
******************************
**[GoFAST Enterprise]** Contactez-nous pour obtenir la liste des correctifs sécurité  

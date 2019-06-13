********************************************
GoFAST :  Version 3.6.0
********************************************


Nouvelles fonctionnalités
*************************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
      "[4848]","Mise à jour majeure du moteur de Workflows BonitaSoft 7.7.4 : 
      - nouvelle ergonomie
      - nouvelles fonctionnalités
      - nouvelles notifications
      - meilleures performances
      Voir : https://bit.ly/2UZP5Lp","[Enterprise]"
      "[4711]","Nouvelle vue historique pour les workflows archivés, accessible depuis la page d’un document
   
   Voir : https://bit.ly/2Xk8ZxV","[Enterprise]"
      "[4262]","Historique détaillé des actions et commentaires faits dans un workflow en cours
   
   Voir : https://bit.ly/2Zgf5RL","[Enterprise]"
      "[4713]","Historique détaillé des actions et commentaires faits dans un workflow archivé
   
   Voir : https://bit.ly/2Xk8ZxV","[Enterprise]"
      "[4822]","Nouveau formulaire pour le workflow standard avec possibilité de rechercher et ajouter plusieurs documents
   
   Voir : https://bit.ly/2UjWqRn","[Enterprise]"
      "[4783]","Création de widgets GoFAST sur BonitaSoft","[Enterprise]"
      "[4784]","Nouveaux connecteurs BonitaSoft/GoFAST (+ amélioration des existants)","[Enterprise]"
      "[4820]","Nouvelles API supplémentaires pour BonitaSoft","[Enterprise]"
      "[1640]","Listes d’Utilisateurs : gestion en masse et automatique des accès aux Espaces Collaboratifs et autres fonctionnalités
   
   Voir : https://bit.ly/2UoTfYC","[Community en v3.6.1][Enterprise]"
      "[3782]","Nouvelle API REST GoFAST pour simplifier les couplages avec d’autres outils métiers","[Community en v3.6.1][Enterprise]"
      "[4141]","Gestion en masse des documents depuis le panier documentaire
   
   Voir : https://bit.ly/2vaO4Bq","[Community en v3.6.1][Enterprise]"
      "[4201]","Création en masse des Publications depuis une séléction de documents de travail
   
   Voir : https://bit.ly/2UGLORU","[Community en v3.6.1][Enterprise]"
      "[4202]","Comparatif de versions : écarts entre 2 versions d'un document en les affichant côte-à-côte [BETA]
   
   Voir : https://bit.ly/2GrV03u","[Community en v3.6.1][Enterprise]"
      "[4273]","Extension des fonctionnalités sur GoFAST mobile : 
      
      - Pouvoir consulter sur la page d’un document sa catégorie, son état et son échéance, 
      - Pouvoir renommer un document
      - Pouvoir accéder et modifier son profil utilisateur
      - Amélioration de l’affichage du menu déroulant (menu principale)
      - Amélioration du bouton qui permet d’affichage/masquer le bloc de droite","[Community][Enterprise]"
      "[4404]","Création d'une zone Membres Bloqués sur la page d’un Espace Collaboratif, dans l’onglet 'Membres'","[Community][Enterprise]"
      "[4561]","Synchronisation des informations d'un Espace Collaboratif avec la navigation dans GoFAST File Browser","[Community][Enterprise]"
      "[4694]","Persistance des filtres sur le fil d'activité et affichage des filtres appliqués en haut du bloc","[Community][Enterprise]"
      "[4798]","Ajout de filtres dans l’annuaire des utilisateurs bloqués","[Community][Enterprise]"
      
   
Améliorations fonctionnelles
****************************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10

      "[4198]","Réduction du nombre de clics lors de l’ajout d’une échéance à un document (l’heure et les minutes sont auto-attribuées par défaut)","[Community][Enterprise]"
      "[4234]","Sélection en masse dans GoFAST File Browser : cocher plusieurs fichiers/dossiers grâce à des cases (et non seulement via les raccourcis clavier)","[Community][Enterprise]"
      "[4282]","Amélioration des notifications liées aux réunions et Webconférences","[Enterprise]"
      "[4715]","Amélioration du mécanisme d’autocomplétions des champs de destinataires de messages : lors de la saisie d’un texte il n’y a plus besoin de cliquer sur la suggestion pour valider le destinataire","[Community][Enterprise]"
      "[4773]","Dans le panier documentaire, ajout de la possibilité de supprimer tous les éléments du panier en un clic","[Community][Enterprise]"
      "[4791]","Exclusion des utilisateurs bloqués de l'autocomplétions dans les champs","[Community][Enterprise]"
      "[4835]","Enlever l'envoi de l’e-mail de notification lorsqu'un utilisateur est débloqué","[Community][Enterprise]"
      "[4903]","Amélioration de l’affichage (taille) de certaines popups (commentaires, message privé, partage par e-mail, etc.)","[Community][Enterprise]"
      "[4914]","Amélioration de l’affichage des Espaces Collaboratifs dont est membre un utilisateur, sur sa page de profil","[Community][Enterprise]"
      "[4935]","Amélioration du message explicatif lors de l’affichage de la popup d'installation ITHitEditDocumentOpener","[Community][Enterprise]"
      "[4952]","Ajout des rôles finaux des espaces dans le profil de l'utilisateur","[Community][Enterprise]"
      "[5002]","Ajout d’un bouton d'accès à la page d'accueil (fil d’activité/tableau de bord) dans le menu principal (à côté du logo)","[Community][Enterprise]"


Améliorations techniques
************************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10

      "[3742]","Mise à jour de Bonita 7.7.4","[Enterprise]"
      "[4774]","Mise à jour de la Suite OnlyOffice 5.2.8","[Enterprise]"
      "[4831]","Implémentation de hooks et altérateurs dans l'activity feed","[Community][Enterprise]"
      "[4866]","Ajout de l’anti-virus CLAMAV","[Community][Enterprise]"
      "[4876]","Mise à jour de LibreOffice 6.2.0.3 (améliorations des prévisualisations des fichiers Office)","[Community][Enterprise]"
      "[4888]","Modification de la gestion des traductions des vues associées aux Workflows (Tableau de bord des processus, formulaires, notifications...)","[Enterprise]"
      "[4922]","Mise à jour de de Jitsi-Meet r3548+","[Enterprise]"
      "[4991]","Supervision Zabbix php-fpm","[Enterprise]"
      "[4957]","Augmentation du max_open_file (ulimit) du système","[Community][Enterprise]"


Sécurité
********
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
      "[4828]","Mise à jour du thème Bootstrap 7.x-3.23 (Security update Boostrap 3.4.0)","[Community][Enterprise]"
      "[4866]","Ajout de l’anti-virus CLAMAV avec notification de supervision","[Community][Enterprise]"
      "[4960]","Mise à jour de sécurité de Views 7.x-3.21","[Community][Enterprise]"


Bugs
****
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10

      "[2913]","Correction de la recherche de chaîne exacte entre guillemets (“ ”)","[Community][Enterprise]"
      "[3962]","Correction du retour sur le fil d'activité (via les boutons du navigateur) pour être ramené sur la bonne page du fil (non la 1ère page par défaut)","[Community][Enterprise]"
      "[4770]","Permettre l’affichage d’un dossier ayant comme titre 'Sites' dans GoFAST File Browser","[Community][Enterprise]"
      "[4803]","Correction de l’affichage des dossiers d'un Espace non archivé qui sont affichés comme archivés (dans le formulaire de gestion des emplacements)","[Community][Enterprise]"
      "[4829]","Permettre le mécanisme d'exclusion de mot clé dans la recherche (via l’utilisation de l’opérateur '-' )","[Community][Enterprise]"
      "[4837]","Correction de l'option 'Conserver les filtres actuels' dans la recherche","[Community][Enterprise]"
      "[4850]","Contenus filtrés dans les autosuggestions des divers champs (ex : recherche, contenus liés…) selon les droits d’accès (pour éviter de suggérer des documents qui sont non accessibles à l’utilisateur)","[Community][Enterprise]"
      "[4915]","Correction du problème d’installation de GoFAST Community via image OVA","[Community]"
      "[4943]","Permettre au créateur d'un document de rechercher et filtrer les documents supprimés et les restaurer (dans la limite de conservation dans la corbeille)","[Community][Enterprise]"
      "[5000]","Récupération de l'extension de fichier lors de la création d’un document vierge","[Community][Enterprise]"


Bugs mineurs
************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10

      "[4769]","Afficher tous les emplacements existants (fil d’Ariane) sur la page d’un forum","[Community][Enterprise]"
      "[4787]","Correction de l’affichage des éléments du bloc 'lien vers d'autres contenus' lorsqu’il y a beaucoup de contenus liés","[Community][Enterprise]"
      "[4800]","Divers problèmes liés au 'sélecteur d’emplacements' dans les formulaires de gestion des emplacements des documents","[Community][Enterprise]"
      "[4862]","Correction de l'affichage des filtres appliqués sur le résultat de recherche lorsque qu’il y a beaucoup de critères","[Community][Enterprise]"
      "[4870]","Correction du pré-remplissage du champs 'Titre' d’un document lors de sa création depuis un modèle (formulaire de création d’un document)","[Community][Enterprise]"
      "[4921]","“InvalidAccessError : Failed to execute” lors webconference","[Enterprise][JITSI][CHROME]"
      "[4939]","Permettre à l’utilisateur de charger une image supérieure à 1Mb pour sa photo de profil","[Community][Enterprise]"
      "[4945]","Site inaccessible si lancement avec options par defaut (à priori security)","[Community][AWS]"
      "[4946]","Champs obligatoires non indiqués comme obligatoires","[Community]"
      "[4947]","Après soumission config 'This site cannot be reached' si pas d'entrée DNS","[Community][AWS]"
      "[4948]","Correction du positionnement de la popup du multi-emplacement sur la page du document","[Community][Enterprise]"
      "[4974]","Afficher des icones manquantes dans l’éditeur de texte de l'accueil d'un Espace Collaboratif","[Community][Enterprise]"
      "[4977]","Afficher l’éditeur de texte du microblogging (sur le fil d’activité)","[Community][Enterprise]"
      "[4995]","Dans GoFAST File Browser, activer les boutons d'actions quand les éléments sont sélectionnés par via les cases à cocher","[Community][Enterprise]"
      
      
**Note: Mettre à jour GoFAST Community** 
   Pour pouvoir mettre à jour votre GoFAST Community, le serveur de mise à jour doit être accessible. Les nouvelles fonctionnalités et les autres améliorations seront disponibles sur www.ceo-vision.com en libre téléchargement en 3.6.1 (actuellement v3.5.2).  



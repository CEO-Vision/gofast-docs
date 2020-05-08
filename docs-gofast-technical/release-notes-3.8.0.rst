********************************************
GoFAST :  Version 3.8.0
********************************************

**[GoFAST Enterprise]** N’hésitez pas à solliciter notre support pour planifier la mise à jour (https://srv01.ceo-vision.com/osticket/index.php).

**[GoFAST Community]** Pour que vous puissiez mettre à jour votre GoFAST Community, le serveur de mise à jour doit être accessible. Posez-vos questions sur nos forums : https://community.ceo-vision.com/


Nouvelles fonctionnalités
***************************
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40
   
   "[GOFAST-5724]", "Nouveau Chat / Plateforme collaborative de discussion instantannée basée sur Riot.im (de type Slack/MS-Teams)"
   "[GOFAST-6126]", "Création automatique des Salons de discussion (nouveau Chat intégré) pour les 2 premiers niveaux des Espaces type Organisation"
   "[GOFAST-6044]", "Intégration du sytstème des membres d'un Espace au Salon de discussion du Chat (Riot.im) associé à cet Espace"
   "[GOFAST-6041]", "Intégration du Chat Riot.im avec la webconférence de GoFAST (côté Jitsi Meet)"
   "[GOFAST-5547]", "Nouvelle version de la webconférence Jitsi-Meet (r3936+)"
   "[GOFAST-5001]", "Nouvelle version GoFAST Mobile (évolutions ergonomiques et fonctionnelles, en vue de la future version GoFAST 'Light/Simplifiée')"
   "[GOFAST-4602]", "[BETA] Edition en ligne avec la Suite Collaborative OnlyOffice sur mobile/tablette dans le navigateur web"
   "[GOFAST-5897]", "Mise à jour OnlyOffice 5.5.1 : listes déroulantes en lecture"
   "[GOFAST-6010]", "Mise en place d'aides contextuelles au démarrage de GoFAST 'Mobile'"
   "[GOFAST-5990]", "Nouvel annuaire utilisateurs sous forme de tableau sur GoFAST 'Mobile'"
   "[GOFAST-5808]", "Nouveau bloc 'Tâches' disponible pour le Tableau de Bord d'Accueil"
   "[GOFAST-5778]", "DUA : Nouveau statut 'Pré-archiver' pour les documents (passage en lécture seule et démarrage de la DUA)"
   "[GOFAST-5452]", "Nouvel indicateur de supervision (sous Zabbix) : le nombre de documents"



Améliorations fonctionnelles
******************************
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40
   
   "[GOFAST-6064]", "Chaines de traductions GoFAST (traduction de l'anglais vers le français)"
   "[GOFAST-5913]", "Amélioration des libellés dans la gestion de la taxonomie en masse"
   "[GOFAST-5849]", "Optimisation du formulaire de création d'un utilisateur (changement des champs pré-cochés par défaut)"
   "[GOFAST-5837]", "Audit : ajout des actions sur les listes d'utilisateurs"
   "[GOFAST-5845]", "Audit : afficher le rôle utilisateur quand il est ajouté à un espace de type Organisation"
   "[GOFAST-5811]", "Dans les blocs Espaces et Dossiers favoris du Tableau de Bord d'accueil : séléction via arborescences au lieu de champs d'autocomplétion"
   "[GOFAST-5816]", "Amélioration de l'administration des catégories (visibilité par Espaces)"
   "[GOFAST-5798]", "Ajouter le nom du document ouvert dans l'onglet OnlyOffice (lors de l'édition avec la Suite Collaborative)"
   "[GOFAST-5794]", "Pouvoir associer des repertoires classiques à des réunions (génération d'un lien d'accès à l'emplacement sur GoFAST Explorer, y compris dans la notification email)"
   "[GOFAST-5783]", "Affichage d'une bulle d'aide expliquant les rôles utilisateurs sur la page d'un Espace, onglet 'Membres'"
   "[GOFAST-5773]", "Page d'un document : griser les liens vers les Espaces dont l'utilisateur n'est pas membre (éviter une page 'accès refusé')"
   "[GOFAST-5731]", "Kanban : pouvoir aller directement sur une carte depuis un lien (et non uniquement la tableau Kanban)"
   "[GOFAST-5641]", "Liste utilisateur : notifier l'utilisateur lors de son ajout/suppression d'une liste"
   "[GOFAST-5636]", "Lors de la création d'un compte utilisateur pouvoir l'ajouter à une liste d'utilisateurs"
   "[GOFAST-5605]", "Extension des droits de création des sous-Groupes et sous-Extarnet pour les utilisateurs non administrateurs de l’Espace parent"
   "[GOFAST-5564]", "Uniformisation des icônes dans les menus des actions contexctuels (menu 'burger')"
   "[GOFAST-5556]", "Kanban : permettre du texte 'riche' (mise en page) dans le champs 'Description' d'une carte"
   "[GOFAST-5539]", "Pouvoir changer les emplacements des documents archivés"
   "[GOFAST-5479]", "Masquer le bouton télécharger dans la prévisualisation PDF" 
   "[GOFAST-5371]", "Ne pas afficher le menu contextuel GoFAST au clic droit sur le nom d'un document en mode édition, dans GoFAST Explorer"
   "[GOFAST-5328]", "Reprise automatique de certaines métadonnées (étiquettes, catégorie...) lors de la création des publications"
   "[GOFAST-5279]", "Possibilité de suppression d'une liste d'utilisateurs"
   "[GOFAST-5245]", "Intégration des info-bulles explicatives aux menus contextuels"
   "[GOFAST-5151]", "Pouvoir mettre à jour le contenu d'une page web externe en changeant le champs 'external URL'"
   "[GOFAST-5126]", "Amélioration du libellé du menu de l'ajout d'un utilisateur / liste d'utilisateur à un Espace"
   "[GOFAST-4953]", "DUA : losqu'une DUA est activée laisser certains champs de métadonnées modifiables"
   "[GOFAST-4658]", "Partage de document(s) par email (lien URL) : l'expéditeur indiqué dans l'email est l'utilisateur et non 'postmaster'"
   "[GOFAST-4632]", "Pouvoir entrer en mode renommage d'un contenu par silmple-clic dans GoFAST Explorer (si document séléctioné, un clic pour modifier le nom)"
   "[GOFAST-4017]", "Eviter la popup d'authentification MS-Office 2010 et 2013 lors de l'ouverture d'un document en 'Edition depuis PC' "
   "[GOFAST-4001]", "DUA : possibilité d'associer une DUA sur une 'Catégories Standard'"
   "[GOFAST-3910]", "Permettre aux administrateurs d'Espaces Collaboratifs, la suppression des commentaires/annotations laissés par les membres de l'Espace"
   "[GOFAST-3608]", "Changement automatique de l'extension(de .dotx vers .docx) des nouveaux documents créés à partir d'un modèle"
   "[GOFAST-2626]", "Nouvelles notifications dédiées aux commentaires"
    
   

Améliorations techniques
**************************
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40

  
   "[GOFAST-6050]", "Fiabilisation de la supervision des erreurs de processus Solr"
   "[GOFAST-6028]", "Mise à jour de la librairie ITHITDocumentopener v5.12.5290 pour l'édition en ligne"
   "[GOFAST-6019]", "Pouvoir utiliser le champ 'memberof' dans les filtres de synchronisation LDAP"
   "[GOFAST-5868]", "Enrichissement de la fonctionnalité de création des objets LDAP"
   "[GOFAST-5777]", "DUA : Changer le mode de déclenchement (association des critères 'Etat' et 'Catégorie')"
   "[GOFAST-5703]", "Mise à jour de la Suite Collaborative OnlyOffice en v5.5.0 (dont mise à l'échelle .xlsx)"
   "[GOFAST-5644]", "Amélioration du workflow standard"
   "[GOFAST-5455]", "Ne pas générer les requêtes webdav dans les cas où GoFAST Explorer est masqué (volet latéral)"
   "[GOFAST-5410]", "Mise à jour du plugin Onlyoffice/Alfresco en v4.0.2"
   "[GOFAST-5284]", "Amélioration des performances : asynchroniser tous les envois de mails"
   "[GOFAST-4237]", "Optimisation des performances lors de la création d'un Espace" 
   
  

Sécurité
**********
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40
  
   "[GOFAST-5951]", "Divers correctifs de sécurité"
  


Bugs
**********
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40

   "[GOFAST-6123]", "Correction des prblèmes de synchronisation de l'organisation principale à l'annuaire lors de la mise à jour"
   "[GOFAST-6063]", "Amélioration des performances à l'ouverture du formulaire d'édition d'un profile utilisateur (ne plus charger tous les rôles de l'utilisateur dans ses Espaces)"
   "[GOFAST-6047]", "Correction des problèmes de cache suite au déplacement d'un espace"
   "[GOFAST-6039]", "Ne pas notifier lors de l'ajout ou suppression d'un membre s'il est également membre d'une liste d'utisateurs dans l'Espace"
   "[GOFAST-6024]", "Correction du blocage aléatoire à la création d'une page web externe"
   "[GOFAST-6013]", "Empêcher la suppresson de dossiers par les contributeurs dans le cas où il y a des fichiers créés par d'autres utilisateurs (côté Alfresco)"
   "[GOFAST-6007]", "Précocher l'emplancement (Espace) d'un article s'il est au-delà du 2é niveau de l'arborescence"
   "[GOFAST-5977]", "Après la suppression d'un répertoire favoris supprimer celui-ci de la liste des favoris (sans avoir à réactualiser la page)"
   "[GOFAST-5969]", "Renommer en 'Tâche' et corriger l'icône des contenus du 'kanban' dans les filtres de recherche par type de contenus"
   "[GOFAST-5925]", "Correction du lien vers un document dans l'email de confirmation de téléchargement après un partage par email"
   "[GOFAST-5919]", "Kanban : éviter la nécessité de cliquer 2 fois pour réaliser une action (Windows + Chrome)"
   "[GOFAST-5889]", "Correction de l'affichage des Emplacements (Espaces) dans l'arborescence lors d'une modification (dans certains cas particuliers)"
   "[GOFAST-5875]", "Correction de la gestion en masse pour la mise à jour des membres d'Espace(s)"
   "[GOFAST-5846]", "Correction du bug lié à la présence d'une virgule dans les noms des fichiers lors de la création/edition d'une réunion"
   "[GOFAST-5860]", "Kanban : correction du problème de renommage d'une colonne après avoir apuyé sur la touche 'Entrée' "
   "[GOFAST-5843]", "Correction de l'affichage des dates"
   "[GOFAST-5838]", "Correction des performances lors de l'ouverture de certains fichiers avec OnlyOffice à cause du téléchargement des polices de caractères"
   "[GOFAST-5815]", "Gestion des Catégories :  Correction du filtrage des catégories par Espace Collaboratif "
   "[GOFAST-5442]", "Récupération de la supervision IOSTAT/MYSQL dans zabbix"
   "[GOFAST-4391]", "Afficher l'avatar de l'utilisateur sur la version mobile "
   "[GOFAST-4176]", "Corresction des des instabilités de la Webconference  Jitsi meet"



Bugs mineurs
***************
.. csv-table:: 
   :header: "Ref.", "Description"
   :widths: 10, 40

   
   "[GOFAST-6121]", "Correction du problème d'affichage de l'arborescence des modèles de répertoires"
   "[GOFAST-5999]", "Correction du problème des doublons de sessions OnlyOffice"
   "[GOFAST-5997]", "Correction de l'affichage de certains titres des documents dans le resultat de recherche"
   "[GOFAST-5992]", "GoFAST Explorer : correction du nommage d'un Espace s'il y a un espace au début ou à la fin du nom"
   "[GOFAST-5985]", "Correction de l'affichage de la liste des 'Favoris'"
   "[GOFAST-5950]", "Remplacer/traduire le mot 'Term' dans la popup de gestion des abonnements par 'Étiquette'"
   "[GOFAST-5941]", "Dans le Fil d'Activité : masquer les commentaires qui ont été supprimés"
   "[GOFAST-5926]", "Correction des traductions des libelés dans la gestion de masse de taxonomie et la carte Kanban"
   "[GOFAST-5775]", "Empêcher de sauvegarder une recherche si le champs 'nom' est vide"
   "[GOFAST-5701]", "Notifications d'administration : pouvoir identifer rapidement l'utilisateur qui souhaite rejoindre un Espace"
   "[GOFAST-5635]", "Lors de la création d'un document, affecter l'utilisateur créateur comme étant l’auteur"
   "[GOFAST-5274]", "Empêcher l'apparition de la fenêtre d'authentification du moteur de workflows dans GoFAST"
   


**Bonne utilisation de GoFAST !**

********************************************
GoFAST :  Version 3.9.0
********************************************

**[GoFAST Enterprise]** N’hésitez pas à solliciter notre support pour planifier la mise à jour (https://srv01.ceo-vision.com/osticket/index.php).



Nouvelles fonctionnalités 
******************************
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40   

   "[GOFAST-6725]", "[ONLYOFFICE] Notes de bas de page et Références croisées "
   "[GOFAST-6618]", "Module Connecteur Pastell (Libriciel)"
   "[GOFAST-6602]", "Onglet pour les métadonnées spécifiques"
   "[GOFAST-6582]", "Création de salon non attaché à des espaces collaboratifs (salon 'libre')"
   "[GOFAST-6405]", "Notification par email tache workflow à échéance"
   "[GOFAST-6364]", "Pouvoir télécharger l'ensemble des documents du panier"
   "[GOFAST-6317]", "Implémentation des APIs de gestion des membres (Espaces & Listes d'Utilisateurs)"
   "[GOFAST-6105]", "Enregistrer une webconference sur GoFAST / Webdav"
   "[GOFAST-5629]", "Gestion des contacts externes"




Améliorations fonctionnelles
******************************
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40
   
   "[GOFAST-6763]", "Element/Chat Masquer 'Partager un utilisateur'"
   "[GOFAST-6747]", "[MOBILE] Ajout d'un menu 'A propos'"
   "[GOFAST-6692]", "MàJ Ajax library v5.18.x"
   "[GOFAST-6662]", "Permettre de pouvoir ajouter un formulaire à une invitation webconference-réunion"
   "[GOFAST-6640]", "Avoir une configuration du cloisonnement pour que le rôle 'admin de plateforme' ne soit pas concerné par celui-ci"
   "[GOFAST-6619]", "Entrée Télécharger au 1er niveau de menu"
   "[GOFAST-6609]", "Amélioration des suggestions d'autocomplétion"
   "[GOFAST-6606]", "Mise à jour Onlyoffice 6.1.0"
   "[GOFAST-6590]", "Lors de la création à partir d'un modèle, ne prendre en compte que les repertoires enfants"
   "[GOFAST-6540]", "Recherche améliorée des nombres et symboles"
   "[GOFAST-6528]", "Dans version mobile, faire pointer le menu 'conversation' ( qui normalement est masqué ) vers une page avec liens de DL des clients lourds"
   "[GOFAST-6436]", "Pouvoir voir les membres et admin d'une liste lorsqu'on partage un espace avec celle-ci"
   "[GOFAST-6302]", "Indexation en fonction de la langue"
   "[GOFAST-6274]", "[SAFARI][JITSI] MàJ Jitsi compatible Safari"
   "[GOFAST-6247]", "Pouvoir supprimer un compte utilisateur jamais utilisé"
   "[GOFAST-6242]", "Pouvoir créer un utilisateur ayant le même email qu'un ancien utilisateur (éviter les demandes de suppression)"
   "[GOFAST-6238]", "Restreindre la possibilité de modifier les modèles de documents que par l'administrateur de l'espace"
   "[GOFAST-6224]", "[CRITICAL] Lors de la suppression d'un répertoire afficher les fichiers partagés qui vont être supprimés"
   "[GOFAST-6014]", "Pouvoir modifier le titre d'un document via l'API de gestion des métadonnées"
   "[GOFAST-5494]", "Pouvoir rechercher les utilisateurs par identifiant/adresse mail"
   "[GOFAST-5096]", "Rajouter le numéro de la version dans le téléchargement de document"
   "[GOFAST-4817]", "Mise à jour Solr 8.x"
   "[GOFAST-3181]", "Synchronisation Etat d'un document avec ceux du Workflow standard"
   "[GOFAST-6653]", "Pouvoir ajouter un webform dans les fichiers attachés à une réunion"
   "[GOFAST-6617]", "Augmentation de la taille maximum de fichier maximale autorisé sur Matrix"
   "[GOFAST-6166]", "Lors d'une connexion par SSO, l'url de la page d'arrivée sur GoFast n'est pas conservée"
   "[GOFAST-5294]", "SELINUX : industrialisation du paramétrage"


   

   

Améliorations techniques
**************************
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40

   "[GOFAST-5269]", "Amélioration performances indexation"
   "[GOFAST-6666]", "Mise à jour Tika 1.18 -> 1.24.1"
   "[GOFAST-6360]", "Mise à jour de PHP 7.2.X vers PHP 7.4.X"
   "[GOFAST-5735]", "Mise à jour pdf-diff v0.9.1"

   
  

Sécurité
**********
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40

   "[GOFAST-6778]", "[iOS] GoFAST : Arret du support iOS12"
   "[GOFAST-6505]", "Supprimer la possibilité de créer un utilisateur avec le rôle administrateur d'espace par défaut"
   "[GOFAST-6797]", "Arrêt support Internet Explorer"
   "[GOFAST-6546]", "Mise à jour Drupal Core 7.73"

 


Bugs
**********
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40

   "[GOFAST-6846]", "[3.9.0_HOTFIX_1.0] Parfois, problème de synchronisation des membres des espaces public lors de la création"
   "[GOFAST-6833]", "[3.9.0_HOTFIX_1.0] Notification carte Kanban avec saut de ligne doublée"
   "[GOFAST-6789]", "Saut de lignes supplémentaires à l'affichage d'une description de tâche (Kanban)"
   "[GOFAST-6782]", "Le changement du role d'une userlist n'est pas pris en compte dans Element"
   "[GOFAST-6766]", "Quand une liste d'utilisateur est rajouté à un espace. Une notification ne doit pas être envoyé si un membre de UL est déjà membre de l'espace"
   "[GOFAST-6765]", "Incohérence entre les historiques d'un document de la version normale et de la version mobile"
   "[GOFAST-6758]", "[SAFARI] Impossible de fermer une card Kanban"
   "[GOFAST-6757]", "Impossible de drag&drop dans GoFAST File Browser après être entré en renommage"
   "[GOFAST-6756]", "Quand une liste d'utilisateurs est retirée d'un espace, aucune notification n'est envoyée"
   "[GOFAST-6733]", "Impossible de faire 'Partager par email' si copie/colle un email puis entrée"
   "[GOFAST-6730]", "[3.8.1_HOTFIX_2.0] Bug de synchronisation des avatars Gofast vers Element"
   "[GOFAST-6712]", "[HOTFIX 3.8.1_HOTFIX_2.0]Mauvaise gestion du scroll dans le ztree des modèles de document"
   "[GOFAST-6701]", "Impossible d'aller à la page d'un mot recherché dans previsualisation"
   "[GOFAST-6700]", "[3.8.1_HOTFIX_2.0] La modification des utilisateurs d'une userlist ne s'enregistrent pas dans LDAP si la liste est vide"
   "[GOFAST-6665]", "[3.8.1_HOTFIX_2.0] Il est possible de modifier le nom du dossier d'un espace depuis l'explorateur GoFAST"
   "[GOFAST-6659]", "Si définir version majeure pas de rechargement automatique de la version sur la page"
   "[GOFAST-6657]", "Message intempestif 'Mise à jour GoFAST' dans le chat"
   "[GOFAST-6655]", "Les utilisateurs ont accès à l'écran de gestion en masse (vide) alors qu'ils ne devraient pas"
   "[GOFAST-6652]", "[MOBILE] Correctifs de bugs (menu contextuel, ....)"
   "[GOFAST-6651]", "Mauvais ordre des salons Element"
   "[GOFAST-6645]", "Pas d'autocomplétion dans certains cas pour les liens entre fichiers"
   "[GOFAST-6628]", "[3.8.1_HOTFIX_1.0] Parfois le plugin Onlyoffice n'enregistre pas le bon modificateur du document (Mise à jour v4.1.0)"
   "[GOFAST-6626]", "[3.9.0_HOTFIX_1.0] Chat: Reconnexion automatique en échec"
   "[GOFAST-6624]", "Enlever la limite du nombre de workflows dans la bulle de navigation"
   "[GOFAST-6614]", "Perte du formatage d'un commentaire créé lors d'une annotation"
   "[GOFAST-6605]", "Enlever le bouton 'rejoindre' sur les espaces public dans l'annuaire"
   "[GOFAST-6572]", "Problèmes de recherche dans les forums (suggestion et highlight)"
   "[GOFAST-6568]", "Bug dans les statistiques des Espaces"
   "[GOFAST-6532]", "Historique des messages desynchronisé en cas de multi-onglet après une ré-authentification"
   "[GOFAST-6523]", "Impossible de déplacer une colonne Kanban juste après son renommage"
   "[GOFAST-6509]", "[BLOCKER] Auto-restart Alfresco non basé sur le timezone"
   "[GOFAST-6398]", "Audit : l'ajout et la suppression d'un membre à une liste doit impacter l'audit des membres et espaces"
   "[GOFAST-6199]", "Après suppression d'un espace dans GFB on revient à la page principale du site"
   "[GOFAST-5851]", "Empecher de renommer un espace par GFB ou renommage pas proposé"
   "[GOFAST-5463]", "Pouvoir archiver un espace de type Extranet"
   "[GOFAST-3959]", "Liste des workflows qui n'apparait pas (roue d'attente)"
   "[GOFAST-2309]", "Problème d'impression de l'aperçu PDF"
   "[GOFAST-6193]", "Latences sur saisies dans le moteur de recherche [autocomplete]"
   "[GOFAST-6801]", "Désactivation temporaire du renommage au clic dans l'explorateur de fichiers"



Bugs mineurs
***************
.. csv-table:: 
   :header: "Ref.", "Description"
   :widths: 10, 40


   "[xxxxxxxxxxx]", "xxxxxxxxxxxxxxxxxxxxxxxxx"





**Bonne utilisation de GoFAST !**

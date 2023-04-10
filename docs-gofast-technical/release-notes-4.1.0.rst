********************************************
GoFAST :  Version 4.1.0
********************************************

**[GoFAST Enterprise]** N’hésitez pas à solliciter notre support pour planifier la mise à jour.


Nouvelles fonctionnalités 
*****************************

.. csv-table::
   :header: "Ref.", "Description"
   :widths: 1000, 60000
   
   "GOFAST-8362","[ESSENTIAL] Nouvelle interface 'Essential' pour utilisateurs occassionnels"
   "GOFAST-7494","[ESSENTIAL] Nouvelle fonctionnalité d'aide contextuelle"
   "GOFAST-9250","[ESSENTIAL] Explorateur de fichiers affiche les 5 derniers emplacements"
   "GOFAST-9500","[ESSENTIAL] Sur IPAD bénéficie maintenant de l'interface 'Essential' en remplacement de l'interface 'Mobile'"
   "GOFAST-5912","Modèles dans Public accessible à toute l'Organisation"
   "GOFAST-7140","Pouvoir compresser / extraire un zip directement sur 'GOFAST'"
   "GOFAST-7957","Permalien d'une carte kanban"
   "GOFAST-8381","Amélioration permettant de simplifier la page d'authentification (choix de l'offre sur écran séparé)"
   "GOFAST-8933","Téléchargement de plusieurs fichiers (explorateur ou panier) sont maintenant dans une archive (zip)"
   "GOFAST-9054","Option création de compte utilisateur après validation du profil support utilisateur"
   "GOFAST-6310","Pouvoir interdire l'ajout d'utilisateur 'Externe' en dehors des espaces 'Extranet'"
   "GOFAST-8344","API de création de workflow"
   "GOFAST-8356","Amélioration permettant d'afficher les échéances des taches dans le calendrier des espaces"
   "GOFAST-8439","Nouvelle fonctionnalité permettant de transformer les anciens formats Office (.doc...) lors de la co-édition"
   "GOFAST-7345","Partage par email d'un répertoire automatiquement compressé en zip"
   "GOFAST-9812","Nouvelle fonctionnalité permettant d'enregistrer une webconference en local"
   "GOFAST-2374","Refonte de la gestion des catégories et des DUA (profil support utilisateurs)"
  
Améliorations 
******************************

**Améliorations Fonctionnelles & Techniques**

.. csv-table::
   :header: "Ref.", "Description"
   :widths: 1000, 60000
  
   "GOFAST-9404","Amélioration permettant d’avoir le texte des colonnes aligné dans l’explorateur de fichiers"
   "GOFAST-9119","Amélioration permettant d'avoir une suggestion des étiquettes existantes sur l'écran de gestion en masse des métadonnées"
   "GOFAST-9395","Améliore l'affichage du fil d'ariane quand le chemin est très long"
   "GOFAST-7941","Amélioration visant à éviter la suppression par erreur d'un espace en demandant une double validation"
   "GOFAST-9425","Ajout de nouvelles actions à l'administration des catégories"
   "GOFAST-6454","Amélioration significative performances export audit"
   "GOFAST-7400","Vérification de l'email saisie par rapport à l'Annuaire lors de la création utilisaeur "
   "GOFAST-7958","Amélioration de notification de tache arrivant à échéance (dont ajout personne responsable)"
   "GOFAST-8780","Amélioration permettant de débloquer un compte par mail de rénitialisation mot de passe "
   "GOFAST-9108","Wikis sous forme d'arboresence (de répertoire et de livres)"
   "GOFAST-9333","Amélioration permettant d'ajouter 2 nouvelles positions pour les signatures Yousign"
   "GOFAST-2341","Message d'alerte de suppression d'un contenu partagé dans plusieurs espaces"
   "GOFAST-6235","Amélioration permettant de voir les taches (kanban) assignées aux autres"
   "GOFAST-6340","Amélioration permettant d'ajouter une liste d'utilisateur à une webconference"
   "GOFAST-6341","Amélioration permettant de protéger une webconference par mot de passe à sa création"
   "GOFAST-6970","Améioration affichant une confirmation si on téléverse un fichier avec le même nom"
   "GOFAST-7584","Amélioration permettant sur Essential de ne plus avoir un sous domaine -mobile"
   "GOFAST-9092","Amélioration par affichage d'une explication lorsque l'on ne peut pas retirer un emplacement"
   "GOFAST-9335","Ajout d'une animation d'attente pour les prévisualisations longues à afficher"
   "GOFAST-9350","Nouvelle amélioration des performances du fil d'activité"
   "GOFAST-7649","Mise à jour MySQL 5.x vers MySQL 8.x (montée version majeure) "
   "GOFAST-7652","Mise à jour Alfresco V6.x vers Alfresco v7.3 (montée version majeure) "
   "GOFAST-9084","Mise à jour PHP v7.x vers PHP 8 (montée version majeure)"
   "GOFAST-8776","Mise à jour plugin Alfresco-Onlyoffice de v4.x à v6.x"  
  

Sécurité 
******************************
.. csv-table::
   :header: "Ref.", "Description"
   :widths: 1000, 60000
  
   "GOFAST-9110","Renforcement sécurité du composant Fail2Ban" 

Bugs 
******************************
.. csv-table::
   :header: "Ref.", "Description"
   :widths: 1000, 60000
      
   "GOFAST-9413","Réintroduction des popups au survol des images de profil dans plusieurs contextes"
   "GOFAST-9516","Correction d'un bug générant une erreur lors de la création d'un espace avec un '+'"
   "GOFAST-8398","Correction d'un bug empechant de citer quelqu'un dans un commentaire avec des majuscules"
   "GOFAST-9149","Correction d’un bug empêchant de rejoindre une webconference sur Iphone"
   "GOFAST-9451","Correction d’un bug indiquant qu’on ne fait plus parti d’un espace alors qu’on est toujours dans une autre liste de cet espace"
   "GOFAST-8808","[ELEMENT][ANDROID] Amélioration permettant d'éviter un message de sessions non vérifiées"
   "GOFAST-9096","Correction d'un bug aléatoire qui empeche d'afficher le titre au dessus d'un document"
   "GOFAST-9555","Modèles de dossier modifiables par le profil support utilisateurs et non super administrateur"
   "GOFAST-8805","Correction d'un bug causant un téléchargement de la prévisualisation dans le format d'origine au lieu de PDF"
   "GOFAST-9205","Correction d'un message d'erreur 'Cet élément ne peut pas être supprimé' alors que le répertoire a bien été supprimé"
   "GOFAST-9387","Correction d'un bug causant l'affichage incorrect de la liste des membres d'un espace"
   "GOFAST-9369","Correction d'un bug causant que l'éditeur de texte riche de la fenêtre de commentaire avait une largeure incorrecte"



  
  
     

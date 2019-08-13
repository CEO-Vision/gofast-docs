********************************************
GoFAST :  Version 3.6.2
********************************************

**[GoFAST Enterprise]** Avis aux équipes techniques : N’hésitez pas à solliciter notre support pour planifier la mise à jour (https://srv01.ceo-vision.com/osticket/index.php).

**[GoFAST Community]** Pour que vous puissiez mettre à jour votre GoFAST Community, le serveur de mise à jour doit être accessible. Posez-vos questions sur nos forums : https://community.ceo-vision.com/

Nouvelles fonctionnalités
*************************
N/A
   
Améliorations fonctionnelles
****************************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[5167]","Améliorer les exports des statistiques sur les espaces/documents/utilisateurs" 
   "[5169]","Améliorer message lors du retrait de membres d'un espace et les conséquences sur les espaces enfants de cette action"
   "[5189]","Visualiser les miniatures des images ou photos dans GFB (GoFAST File Browser ou explorateur de fichiers)"
   "[5235]","Pouvoir annuler un workflow  en cours par l'administrateur d'espace"
   "[5242]","Permettre au créateur d'un document de restaurer son document supprimé si l’auteur ne fait plus partie de l’espace"

Améliorations techniques
************************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[5234]","Amélioration/Correctifs API de publication (changement de format de transformation pendant publication, ...)"
   "[5223]","Pouvoir stocker les images séparément (serveur) dans le micro-blogging"
   "[3093]","Mécanisme de vérification d'intégrité en arrière plan"
   "[5213]","Ne pas rafraîchir l'explorateur lors d'un renommage de fichier"
   "[5281]","Augmenter le délai de déclenchement des requêtes d'auto-complétions de recherche"
   "[5203]","Ajout polices Wingding pour la prévisualisation"
      
Sécurité
********
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[5142]","Correctif faille Intel MDS (Fallout, RIDL, Zombieload)"
   "[5193]","Mise à jour module UUID security update (SA-CONTRIB-2019-052)"
   "[5227]","Mise à jour module Advanced Forum (SA-CONTRIB-2019-054)"
   "[5303]","[MOBILE] Possibilité d’éditer une annotation co-éditable sans avoir les droits"

Bugs
****
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[5197]","Corriger le filtre 'Tous' dans la rubrique “Filtrer les espaces” dans l’Annuaires"
   "[5219]","Impossible de copier-coller une image dans l'éditeur de texte riche (ckeditor)"
   "[5275]","Empêcher l'analyse antivirus Clamd pendant la journée"
   "[5277]","SElinux : corriger les alertes remontées dans les logs (php-fpm, etc.)"
   "[5280]","Pouvoir modifier le rôle d'une liste d’utilisateur qui n'a pas de rôle"
   "[5283]","Glisser-déposer une arborescence dans un répertoire sur GoFAST ne fonctionne pas quand un des   dossiers importés depuis le serveur de fichiers est vide"
   "[5287]","Ne pas propager la suppression d'un membre de l’espace parent aux membres d’espaces enfants si ce membre fait toujours parti de l'espace via une liste d’utilisateurs" 
   "[5291]","Tous les éléments de l'historique des process Bonita affichent le même historique"
   "[5310]","Empêcher le renommage d'un dossier d'un espace dans GFB"
   "[5338]","Supprimer fonctionnalité mutlifiling/publication/par mail en masse sur espace/répertoire" 

Bugs mineurs
************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
      
   "[5200]","Mauvais texte s’affiche quand il n'y a pas de page d'accueil sur un espace"
   "[5221]","Rubrique “Derniers contenus vus" dans le menu dépasse si le nom de documents est trop long"
   "[5222]","Champ d'autocomplétion coupé trop tôt ce qui empêche de voir les titres en entier"
   "[5253]","Icône espace archivé apparaît sur un espace qui n'est pas archivé lors de la création de contenu/ multifiling"
   "[5254]","[IE] GFB: Navigation automatique vers la page d'un espace ne fonctionne pas"
   "[5257]","Bouton d'ajout au panier manquant dans les actions contextuelles quand on sélectionne plusieurs documents dans GFB"
   "[5261]","Impossible de sélectionner certains emplacements comme filtres sur le fil d'activité"
   "[5262]","[IE] Formatage et Navigation cassés dans une page externe"
   "[5263]","Erreur du changement de la métadonnée "Importance" sur un contenu de type forum"
   "[5266]","Impossible de gérer la taxonomie en masse depuis le panier documentaire"
   "[5270]","La liste des filtres d'activité ne doit s'afficher que sur le fil d'activité"
   "[5273]","[IE] Profil d'un utilisateur mal formaté"
   "[5184]","Corriger l’erreur non bloquante "You have to set a comment" quand on republie un document sans laisser de commentaires"
   "[5285]","Bug graphique au niveau de la quand navigation ajax suite à la après création d'un nouveau forum"
   "[5286]","Lors d'un partage en masse par mail, l'action doit se voir sur le fil  d'activité"
   "[5292]","Dernier contenus vus dans le menu ne sont pas à jour"
   "[5296]","[MOBILE] Le fil d'activité n'est pas centré sur l'écran"
   "[5297]","[MOBILE] Redirection absente après la création d’une page interne depuis calendrier" 
   "[5298]","[MOBILE] GoFAST File Browser : Les cases ne se cochent pas suite au choix de plusieurs emplacements (multi sélection)"
   "[5301]","Mauvais affichage des images larges dans le micro-blogging"
   "[5304]","[MOBILE] "Menu d’actions contextuelles" homogène à la version desktop (à gauche de la recherche)"
   "[5333]","Erreur " Le site Web a rencontré une erreur inattendue." après l'authentification"   
   "[5302]","[MOBILE] Correctif du microblogging/nouvelle sur le Tableau de bord"


**Bonne utilisation de GoFAST !**

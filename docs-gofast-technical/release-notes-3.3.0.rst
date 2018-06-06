
********************************************
GoFAST :  Version 3.3.0
********************************************

Améliorations
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[4158]", "Pouvoir choisir le nom de l'expediteur des notifications", "Notification"
   "[4054]", "Nouvel explorateur de fichiers Web (remplacement ITHit Browser)", "Explorateur de fichiers"
   "[4082]", "Amélioration des Réunions et Visio-conférence", "Visio-conférence"
   "[4143]", "Visuel de notification : Pour la création d'un compte utilisateur", "Notification"
   "[4144]", "Visuel de notification : Pour l'acceptation d'un utilisateur à un espace après une demande", "Notification"
   "[4145]", "Visuel de notification : Pour l'ajout d'un utilisateur dans un nouvel espace par un administrateur", "Notification"
   "[4146]", "Visuel de notification : Pour l'ajout d'un utilisateur dans un nouvel espace", "Notification"
   "[4147]", "Visuel de notification : Pour informer du partage de lien d'un document à un autre utilisateur", "Notification"
   "[4148]", "Visuel de notification : Pour la suppression d'un lien de *relation* entre deux utilisateurs", "Notification"
   "[4150]", "Visuel de notification : Pour la récupération du mot de passe", "Notification"
   "[4151]", "Visuel de notification : Pour la date d'échéance sur un document", "Notification"
   "[2964]", "Séparer les termes *Catégories* standards et non standards", "Catégorie"
   "[4108]", "Amélioration du comportement bouton *Retour / Suivant* du navigateur", "Performance"
   "[3562]", "Notification de mise en relation", "Notification"
   "[4199]", "Mieux discerner les espaces dans l'explorateur de fichiers", "Affichage" 
 




Sécurité
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10

   "[4153]", "Utilisation d'une requête POST au lieu de GET dans l'API de récupération de ticket Alfresco", "Requête"


Bugs mineurs
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 60, 10
   
   "[4098]", "Impossibilité d'aller sur la gestion en masse des membres", "Gestion en masse"
   "[4122]", "Impossibilité de supprimer un espace (Ancien espace créé sous GF2)", "Suppression"
   "[4124]", "Visio-conférence non fonctionnelle sur la plateforme Cloud : impossible de démarrer une session", "Visio-conférence"
   "[4134]", "Devoir vider l'intégralité du cache de Drupal à chaque création de document par un formulaire", "Création de document"
   "[4152]", "Affichage de l'arborescence lors de la gestion des membres", "Affichage"
   "[4162]", "Formulaire d'export des utilisateurs affiche le retour de l'ajaxification lors de l'accès en Ajax", "Formulaire"
   "[4163]", "Temps de latence à mettre entre la fermeture de la fenêtre apparente de workflow et le rechargement de la page", "Chargement"
   "[3016]", "Fichier comprennant de nombreuses révisions non expliquées", "Versionning"
   "[3083]", "Visio-conférence invisible dans le fil d'actuailité de la version mobile", "Mobile"
   "[3845]", "Page *non trouvée* (non GF) suite à l'édition en ligne d'un fichier PDF", "Edition en ligne"
   "[3922]", "Perte de l'onglet lors de la navigation sur les mois du Calendrier l'Espace privé", "Calendrier"
   "[4037]", "Depuis le tableau de bord/fil d'Ariane, impossible d'arriver sur l'onglet document", "Navigation"
   "[4038]", "Impossible d'ouvrier un fichier .ODT avec MS Office : Message d'erreur de MS", "Edition en ligne" 
   "[4067]", "Correction des chaines de traduction", "Traduction"
   "[4072]", "Arrivé sur l'onglet documents lors d'un clic sur un emplacement ou depuis un espace du tableau de bord", "Tableau de bord"
   "[4126]", "Erreur 404 lors de l'abonnement à des mots-clés", "Etiquette"
   "[4165]", "Envoi de notifications considérablement ralenti", "Notification"
   "[2667]", "Un document supprimé reste dans l'explorateur de fichiers tant qu'on a pas volontairement rafraichit la page manuellement", "Suppression"
   "[3445]", "Fenêtre apparente du commentaire sur la version mobile n'est pas optimisée", "Mobile"
   "[3749]", "Affichage des dates sur la version mobile : Jour et Mois sont inversés", "Mobile"
   "[4091]", "Lors de la réponse à un commentaire à travers une notification : le commentaire ne se positionne pas", "Commentaire"
   "[3749]", "Affichage des dates sur la version mobile : Jour et Mois sont inversés", "Mobile"
   "[4190]", "Affichage multiple d'une fenêtre apparente avec un message *en cours d'ouverture* + Manque du verrouillage du document", "Edition en ligne"
   
Bugs majeurs
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[4174]", "Changement de langue non fonctionnel", "Traduction"
   "[3069]", "Aucun résultat ne s'affiche lors d'une recherche (or éléments existants)", "Moteur de recherche"
   "[4106]", "Temps de session de Drupal jugé incorrect", "Chargement"
   "[4138]", "Ajouter *Favoris* (public ou privé) : Une page blanche apparait", "Affichage"
   "[4169]", "Rendre le bouton d'actions asynchrone sur la page de recherche", "Performance"
   "[4188]", "Impossible de supprimer une conférence", "Suppression"
   "[3634]", "Lenteur pour aller sur un profil", "Performance"
   "[4172]", "Workflow - Impossible de récupérer un Modèle", "Workflow"
    
Hotfix
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[4115]", "Mise à jour de Drupal Correctif Faille PSA-2018-003", "Sécurité"
   "[4132]", "Impossible de créer un répertoire dans l'explorateur de fichier", "Explorateur de fichiers"
   "[4156]", "Champs *Date d'échéance* sur le bloc de métadonnées d'un noeuf n'enregistre pas la bonne date", "Métadonnée"
   "[4166]", "Le multi-emplacement n'est pas fonctionnel : Le document partagé mais n'est pas vu par l'utilisateur", "Multi-emplacement" 
   "[4111]", "Le lien du menu parent *Annuaire* n'est pas bon", "Annuaire"
   "[4114]", "Les formats de date dans les notifications standards ne sont pas adaptées à la langue du destinataire", "Notification" 



Améliorations* de l'Explorateur de fichiers GoFAST (File Browser)
**********************
Fonctionnelles
---------------
.. csv-table::  
   :header: "Description", "Action"
   :widths: 40, 10
   
   "Gérer les emplacements en masse", "Nouveau"
   "Filtrer les contenus d'un espace ou d'un dossier par titre", "Nouveau"
   "Menu disponible par *clique-droit* qui affiche toutes les actions possibles sur un document et un ensemble de documents", "Nouveau"
   "Indique le temps de chargement", "Nouveau"
   "Créer un document depuis l'explorateur de fichiers File Browser", "Nouveau"
   "Glisser/Déposer des fichiers à partir d'un PC utilisateur", "Existant"
   "Trier par type, date, taille", "Existant"
   "Ajouter des documents depuis/vers son PC", "Existant"
   "Créer des dossiers entre les espaces et les dossiers dans l'explorateur GoFAST", "Existant"
   "Déplacer des contenus depuis un PC utilisateur", "Existant"
   "Gérer la taxonomie", "Existant"
   "Différentes possibilités d'affichage des contenus", "Existant"

Visuelles et ergonomiques 
----------
.. csv-table::  
   :header: "Description", "Action"
   :widths: 40, 10

   "Bouton *Affichage* proposant la possibilité d'afficher les fichiers : détails/icônes", "Amélioration"
   "Mise à jour visuelle de l'explorateur de fichiers", "Amélioration"
   "Visibilité des éléments listés dans l'explorateur de fichiers", "Amélioration"
   "Icônes distincts dans l'arborescence permettant d'identifier un dossier classique et le type d'espace", "Amélioration"











********************************************
GoFAST :  Version 3.5.0
********************************************


Nouvelles fonctionnalités
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[2067]", "Cloisonnements des utilisateurs + visibilité des espaces (hors Chat)"
   "[3772]", "Offre GoFAST Community"
   "[4529]", "Plugin OnlyOffice pour enregistrer le document dans GoFAST sans fermer l’onglet"
   "[4598]", "Annotations et commentaires partagés ou privés"
   "[4608]", "Nouvelle supervision (serveurs / process) sous Zabbix"
   
   
   
Améliorations fonctionnelles
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[3795]", "Formulaire 'Création Document' permettant de détecter la langue du contenu" 
   "[4239]", "Ajout d’un menu 'Navigation Générale' (si tableau de bord présent)"
   "[4273]", "[MOBILE] Améliorations diverses (ajout catégorie, action renommer, nouveau menu...)"
   "[4500]", "[MOBILE] : Améliorations de l’ergonomie des filtres de recherche"
   "[4533]", "Amélioration de l'affichage des emplacements dans le fil d'activité"
   "[4563]", "Pré-cocher l'emplacement du document de travail lors de la création de sa publication"
   "[4564]", "Afficher un message d'erreur cohérent quand le document est supprimé"
   "[4592]", "Besoin de différencier les espaces archivés des autres espaces (GoFAST File Browser et autre)"
   "[4625]", "Résumé Accusé réception de partage par email"
   "[4646]", "Dans les résultats de recherche : Ne pas afficher les contenus obsolètes par défaut"
   "[4648]", "Homogénéisation entre les filtres de recherche et les filtres fil d'activité"
   "[4654]", "Classer les libellés dans 'Importance'"
   "[4681]", "Ouverture dans un nouvel onglet à la suite d’un clic sur un lien externe dans un PDF"
   
   
   
Améliorations techniques
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
 
   "[3379]", "Mise à Jour Jquery 3.1 (jquery 1.10 EOF)"
   "[3882]", "Amélioration de la rapidité lors du renommage d’espaces"
   "[3927]", "[JITSI MEET] Permettre le fonctionnement sur le port sur le 80"
   "[4048]", "Utilisateurs bloqués : Raccourci et filtre vue ajoutés"
   "[4484]", "Mise à Jour de Jitsi-Meet 1.0.3081"
   "[4607]", "Mise à jour OnlyOffice 5.2.3"
   "[4635]", "Augmenter la limitation de caractères dans le nom de la plateforme"


   
Sécurité
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[4636]", "MAJ Drupal 7.60 (sa-core-2018-006)"



Bugs majeurs
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[3722]", "[OnlyOffice] Les paramètres d'un document Classeur Onlyoffice ne sont pas sauvegardés (orientation, marges...)"
   "[4035]", "Nombreux correctifs formulaires/webform"
   "[4304]", "[ONLYOFFICE] Affichage d’un message d’avertissement indiquant la perte de réseau"
   "[4313]", "Problèmes de création d'espace quand caractère ‘+' dans le nom"
   "[4323]", "La pop-up multi-emplacement ne se ferme pas"
   "[4340]", "La hauteur de la zone 'commentaire' n’est pas optimale et editeur riche mal positionné
   "[4477]", "Des templates de documents vierges manquant lors de l'installation + image par defaut"
   "[4492]", "[BLOCKER] La popularité (scoring) ne change pas lorsqu’un document est sauvegardé"
   "[4509]", "GFBrowser mobile passe au dessus du contenu dans certaines résolutions"
   "[4521]", "Supprimer une publication depuis GFBrowser redirige vers la page d'accueil"
   "[4538]", "Mauvaise action listée dans le fil d'activité suite à la modification de l’importance"
   "[4552]", "Le formulaire de configuration de la DUA est vide"
   "[4571]", "Erreur lors d'archivage d'un type autre que 'Groupes'"
   "[4576]", "La page d'arrivée suite au clic sur "Lien vers cet emplacement" affiche le bloc de chargement de document"
   "[4601]", "Amélioration des performances du fil d'activité"
   "[4627]", "Recherche : la chaîne exacte ('xxxx')  n'est pas prise en compte"
   "[4629]", "Impossible de créer un 'article' à la racine de son espace privé"
   "[4633]", "GFB : Télécharger la version Windows d'ITHitDocument pour MacOS ou Linux"
   "[4652]", "Scrollbar invisible dans l'arborescence (ztree) de GFB et auto scroll vers la droite"
   "[4657]", "Erreur de navigation depuis le fil d'ariane quand '&' dans chemin"
   "[4660]", "[BLOCKER][MOBILE] : Annotations affichées de façon aléatoire"
   "[4661]", "[BLOCKER][MOBILE] Le bouton 'Annoter' est mal positionné et le bouton et pop-up sont traduits"
   "[4664]", "[BLOCKER][MOBILE] Impossible de séléctionner correctement le texte souhaité pour annoter"
   "[4673]", "[BLOCKER] Les participants GoFAST d'une réunion ne recoivent pas l'annulation lors de sa suppression"
   "[4683]", "Problème de sauvegarde de la position ouvert/fermé de l'explorateur de gauche"
 


Bugs mineurs
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[2968]", "Erreur sous Office quand on renomme puis édite un fichier en ligne"
   "[4352]", "Plusieurs correctifs fonction 'Relation'"
   "[4566]", "[iPpad] Le détail des événements agenda est manquant sur la version mobile + besoin d’agrandir la police des liens"
   "[4644]", "Envoi d'un message généraliste à la création d'un user par le client"
   "[4656]", "La loupe de la recherche se décale"
   "[4692]", "Apparition de multiples étiquettes lors de l'ajout d'une seule"
   "[4693]", "Problème lors de l'auto-complétion"

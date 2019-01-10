********************************************
GoFAST :  Version 3.5.0
********************************************


Nouvelles fonctionnalités
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[2067]", "Cloisonnements des utilisateurs + visibilité des espaces (hors Chat)
   (Voir : https://gofast-docs.readthedocs.io/fr/latest/docs-gofast-users/doc-gofast-guide-utilisateurs.html#annotations-partagees-ou-privees)"
   "[3772]", "Offre GoFAST Community"
   "[4529]", "Plugin OnlyOffice pour enregistrer le document dans GoFAST sans fermer l’onglet"
   "[4598]", "Annotations et commentaires partagés ou privés
   (Annotations, voir : https://gofast-docs.readthedocs.io/fr/latest/docs-gofast-users/doc-gofast-guide-utilisateurs.html#annotations-partagees-ou-privees
   Commentaires, voir : https://gofast-docs.readthedocs.io/fr/latest/docs-gofast-users/doc-gofast-guide-utilisateurs.html#commentaires-partages-ou-prives)"
   "[4608]", "Nouvelle supervision (serveurs / process) sous Zabbix"
   
   
   
Améliorations fonctionnelles
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[3795]", "Formulaire 'Création Document' permettant de détecter la langue du contenu" 
   "[4239]", "Ajout d’un menu 'Navigation Générale' (si tableau de bord présent)"
   "[4273]", "[VERSION MOBILE] Améliorations diverses (ajout catégorie, action renommer, nouveau menu...)"
   "[4500]", "[VERSION MOBILE] : Améliorations de l’ergonomie des filtres de recherche"
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
   


HOTFIX (Version Enterprise)
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[3192]", "Certaines notifications workflow ne sont pas envoyées"
   "[4587]", "[VERSION MOBILE] Faire une annotation n'affiche pas le commentaire sans avoir à rafraichir la page"
   "[4620]", "Il y a une erreur de transaction Alfresco quand erreur d'envoi de mail dans script de réplication"
   "[4643]", "La hauteur de de la fenêtre de prévisualisation doit être fixe"
   "[4702]", "[3.5.0_1] Regression sur le fonctionnement du broadcast dans un espace privé"
   "[4703]", "[3.5.0_1] Problème de performance base de donnnées lors d'une indexation en masse de documents"
   "[4705]", "[3.5.0_2][IPAD] Imprécision de la sélection pour l'annotation"
   "[4708]", "[3.5.0_2] Depuis page d'un espace, si on décoche tous les rôles d'un user, la membership ne disparait pas"
   "[4714]", "[3.5.0_3][SECURITE] MAJ Drupal 7.61"
   "[4704]", "[3.5.0_4] Pas possible d'annoter une seconde fois"
   "[4716]", "[3.5.0_4] Erreur de droit lors d'une publication"
   "[4718]", "[3.5.0_4] Supprimer des espaces à droite lors de la publication d'un document ne les suppriment pas réellement"
   "[4719]", "[3.5.0_4] Partage par email : envoi en anglais au lieu de francais"
   "[4722]", "[3.5.0_4] Mauvaise configuration de la popularité pour certains types de contenus"
   "[4723]", "[3.5.0_5] La vérification d'orthographe ne s'active plus sous OnlyOffice"
   "[4730]", "[3.5.0_5] Erreur si on partage un dossier qui est profond dans l'arborescence"
   "[4731]", "[3.5.0_5] GFB passe par dessus le fil d'activité"
   "[4732]", "[3.5.0_5] Dans certains cas des docs visibles en Webdav ne sont pas dans GoFAST"
   "[4746]", "[3.5.0_6] Double envoi de mail lors de l'annulation de réunion"
   "[4729]", "[3.5.0_7.0/8.0] Destinataires extranets n'apparaissent pas dans zone destinataires dans la notification de partage par mail"
   "[4749]", "[3.5.0_9] Zone de glissé-déposé plus visible sur page d'accueil"
   "[4750]", "[3.5.0_9] Impossible d'éditer en ligne un document depuis l'explorateur"
   "[4756]", "[3.5.0_10] Page de filtres malformées lors d'une réactualisation de la page de recherche"
   "[4757]", "[3.5.0_10] GFB mobile se met en erreur quand on va sur certaines pages d'espace"

Bugs majeurs
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[3722]", "[ONLYOFFICE] Les paramètres d'un document Classeur OnlyOffice ne sont pas sauvegardés (orientation, marges...)"
   "[4035]", "Nombreux correctifs formulaires/webform"
   "[4304]", "[ONLYOFFICE] Affichage d’un message d’avertissement indiquant la perte de réseau"
   "[4313]", "Problèmes de création d'espace quand caractère ‘+' dans le nom"
   "[4323]", "La pop-up multi-emplacement ne se ferme pas"
   "[4340]", "La hauteur de la zone 'commentaire' n’est pas optimale et editeur riche mal positionné"
   "[4477]", "Des templates de documents vierges manquant lors de l'installation + image par defaut"
   "[4492]", "[BLOCKER] La popularité (scoring) ne change pas lorsqu’un document est sauvegardé"
   "[4509]", "GFB de gauche passe au dessus du contenu dans certaines résolutions"
   "[4521]", "Supprimer une publication depuis GFBrowser redirige vers la page d'accueil"
   "[4538]", "Mauvaise action listée dans le fil d'activité suite à la modification de l’importance"
   "[4552]", "Le formulaire de configuration de la DUA est vide"
   "[4571]", "Erreur lors d'archivage d'un type autre que 'Groupes'"
   "[4576]", "La page d'arrivée suite au clic sur 'Lien vers cet emplacement' affiche le bloc de chargement de document"
   "[4601]", "Amélioration des performances du fil d'activité"
   "[4627]", "Recherche : la chaîne exacte ('xxxx')  n'est pas prise en compte"
   "[4629]", "Impossible de créer un 'article' à la racine de son espace privé"
   "[4633]", "GFB : Télécharger la version Windows d'ITHitDocument pour MacOS ou Linux"
   "[4652]", "Scrollbar invisible dans l'arborescence (ztree) de GFB et auto scroll vers la droite"
   "[4657]", "Erreur de navigation depuis le fil d'ariane quand '&' dans chemin"
   "[4660]", "[BLOCKER][VERSION MOBILE] Annotations affichées de façon aléatoire"
   "[4661]", "[BLOCKER][VERSION MOBILE] Le bouton 'Annoter' est mal positionné et le bouton et pop-up sont traduits"
   "[4664]", "[BLOCKER][VERSION MOBILE] Impossible de séléctionner correctement le texte souhaité pour annoter"
   "[4673]", "[BLOCKER] Les participants GoFAST d'une réunion ne recoivent pas l'annulation lors de sa suppression"
   "[4683]", "Problème de sauvegarde de la position ouvert/fermé de l'explorateur de gauche"
 


Bugs mineurs
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[2968]", "Erreur sous Office quand on renomme puis édite un fichier en ligne"
   "[4352]", "Plusieurs correctifs fonction 'Relation'"
   "[4566]", "[IPAD] Le détail des événements agenda est manquant sur la version mobile + besoin d’agrandir la police des liens"
   "[4644]", "Envoi d'un message généraliste à la création d'un user par le client"
   "[4656]", "La loupe de la recherche se décale"
   "[4692]", "Apparition de multiples étiquettes lors de l'ajout d'une seule"
   "[4693]", "Problème lors de l'auto-complétion"

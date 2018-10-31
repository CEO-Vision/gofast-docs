********************************************
GoFAST :  Version 3.4.1
********************************************


Améliorations fonctionnelles
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[4347]", "L'arrivée sur le tableau de bord n'est pas ergonomique"
   "[4393]", "Les rappels de réunions survenant juste avant la réunion sont à supprimer"
   "[4394]", "Création réunion : Possibilité de décocher des users non invités même s'ils font partie de l'espace à inviter"
   "[4418]", "Nombre de lignes augmenté pour les Favoris"
   "[4436]", "Adaptation de PDF.js à la charte graphique GoFAST"
   "[4443]", "Différencier les dossier TEMPLATES (rouge) dans GFBrowser"
   "[4456]", "Amélioration de la création de la traduction d'un document"
   "[4473]", "Message indiquant une 'Prévisualisation en cours'"
   "[4474]", "Menu déroulant pour : Documentation - Forum - A propos de - Swap version mobile"
   "[4481]", "Renommer la fonction 'Conférence' en 'Réunion'"
   "[4498]", "Amélioration de l'ergonomie 'Calendrier mobile'"
   "[4501]", "Améliorer la gestion des actions dans l'explorateur de fichiers sur tablette"
   "[4502]", "Fil d'ariane sur les documents (version mobile)"
   "[4531]", "Affichage des réunions sous format texte simple pour les appareils ne pouvant pas décoder le HTML"
   "[4577]", "Thème spécifique pour les notifications"
   "[4585]", "L'action 'Supprimer' a été ajoutée (version mobile)"



Améliorations techniques
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[4370]", "Le format 'rtf' n'est pas identifié comme format 'text'"
   "[4420]", "Mise à jour WebDAV Ajax Library 5.7.3252.0"
   "[4468]", "Optimiser le temps de réponse du fil d'activité"

   
   
Sécurité
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[4452]", "L1TF - L1 Terminal Fault Attack - CVE-2018-3620 & CVE-2018-3646"



HOTFIX (Enterprise)
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[3644]", "Si le champ 'Téléphone' est rempli avec un caractère espace, l'utilisateur n'est pas créé"
   "[4494]", "Terme 'Activité' changé par 'Accueil' dans le menu mobile"
   "[4495]", "Rôle 'Lecture seule' : l'action 'Partager par email' manque dans le menu des actions rapides"
   "[4497]", "Création de réunion : Problème d'affichage liste des documents"
   "[4503]", "Après la suppression d'un document sur la version mobile, on reste sur la page"
   "[4515]", "Ajouter un espace en participant réinitialise la date de la conférence"
   "[4520]", "Export des documents depuis les stats : Erreur pour téléchanger l'export"
   "[4523]", "Bouton 'Partager par email' dans les actions sur la version mobile est manquant"
   "[4524]", "Le titre sur la page d'une réunion est manquant sur la version mobile"
   "[4525]", "Les actions rapides sur la recherche mobile sont manquantes"
   "[4545]", "Fil d'activité sur mobile et tablette : affichage cassé dans certain cas"
   "[4557]", "Le bouton 'Accéder à mon calendrier' sur le tableau de bord redirige vers l'explorateur de fichiers"
   "[4559]", "Le fil d'ariane dans les espaces sur la version mobile est manquant"
   "[4560]", "Le bouton 'Ajouter documents dans le GFBrowser' ne marche pas sur iPad"
   "[4562]", "La page d'espace sur version mobile n'est pas thémée (pour les non membre)"
   "[4572]", "Après l'ajout de document par 'Glisser/déposer' sur l'accueil : fichier de 0k"
   "[4573]", "Ajout de participants à une conférence : Problème quand ajout avec une virgule"
   "[4580]", "Action dans le fil d'activité : mauvais utilisateur"
   "[4582]", "Copier/coller un document et l'ouvrir dans GFBrowser redirige vers document d'origine si on n'actualise pas"
   "[4589]", "Scroll intempestif quand on arrive sur la page d'un espace depuis le fil d'ariane (version mobile)"
   "[4591]", "Impossible d'annoter sous iOS (iPAD)"
   "[4617]", "La gestion de taxonomie (classification) en masse ne fonctionne pas correctement"

   
   
Bugs majeurs
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[3750]", "Mobile : workflow manquant dans les informations sur les documents quand le document est dans un workflow" 
   "[3796]", "Affichage des dates pour les visioconférences : La date de fin apparaît en version anglo-saxonne"
   "[4058]", "Gestion des membres en masse : liste des membres non visible l'explorateur d'espaces pour certains espace"
   "[4327]", "Le fil d'activité pose problème d'affichage quand il est vide"
   "[4348]", "Certaines vues sur mobile ne sont pas centrées (lecture sur Ipad)"
   "[4351]", "Perte de l'affichage du calendrier mobile sur la version optimisée"
   "[4373]", "Commentaires sur la version mobile : un seul s'affiche lors du chargement de la page"
   "[4376]", "Problème d'affichage des réunions dans les calendriers suite à une création/modification"
   "[4388]", "Problèmes divers dans les notifications et manque le 'suivi' des réunions dans Outlook (dont 2010)"
   "[4390]", "Les réunions sont indiquées à la mauvaise heure dans le calendrier"
   "[4396]", "Le logo est surdimensionné dans les notifications de réunion (Outlook 2010)"
   "[4397]", "L'emplacement de la réunion n'est pas repris dans le calendrier Outlook (2010)"
   "[4399]", "Problème d'affichage dans certains blocs sur le tableau de bord"
   "[4401]", "Affichage des filtres de recherche à améliorer sur version mobile"
   "[4403]", "Les actions non autorisées sont affichées dans le menu des actions sur mobile"
   "[4417]", "Edition d'un livre dans un article : Message d'erreur"
   "[4422]", "Un point (.) dans le nom d'un espace coupe son nom dans le fil d'ariane"
   "[4434]", "Le microblogging ne fonctionne pas sur la version mobile"
   "[4454]", "Impossible de créer un nouveau contenu après avoir fait un 'glisser-déposer' sur la page 'Activité'"
   "[4458]", "Les permaliens vers les commentaires ne fonctionnent plus"
   "[4461]", "Modifier un événement (article) après l'avoir créé génère une erreur"
   "[4466]", "L'action 'Créer Document' est très lente"
   "[4470]", "Chargement de la liste des dossiers/documents par le GFB : colonne de droite revient à la ligne par dessus colonne de gauche, ce qui créer un bug graphique"
   "[4480]", "Envoi d'email à un groupe : dysfonctionnement"
   "[4483]", "L'affichage du résumé d'un document n'apparaît pas pour les utilisateurs en lecture seule"
   
   
   
Bugs mineurs
**********************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
   "[4285]", "Onglet 'Catégorie de la configuration' : Les langues autre que FR, NL et EN sont à enlever"
   "[4335]", "Le menu déroulant est masqué lors du résultat de recherche"
   "[4344]", "Impossible de supprimer en masse sur l'explorateur de fichiers (menu de gauche)"
   "[4407]", "Favoris : Après avoir ajouté un fichier dans les favoris, 'Ajouter aux favoris publics' restent afficher à la place de 'Retirer des favoris publics'"
   "[4432]", "Suppression d'une publication : Le bouton 'Cancel' ne ferme pas la page et n'a pas de style"
   "[4448]", "Après récupération du mot de passe, l'explorateur de gauche est déployé et ne veut plus se masquer"
   "[4476]", "Partage par email : Notification de téléchargement incorrecte"
   "[4479]", "Modifier le résumé : Le bouton 'Modifier le résumé' apparaît"
   "[4486]", "Le fil d'activité n'affiche plus la personne qui ajoute ou modifie un commentaire"
   "[4487]", "Perte des émoticônes dans le chat"
   "[4504]", "La zone 'Glisser-Déposer' est affichée sur le tableau de bord"

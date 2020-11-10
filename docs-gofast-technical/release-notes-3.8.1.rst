********************************************
GoFAST :  Version 3.8.1
********************************************

**[GoFAST Enterprise]** N’hésitez pas à solliciter notre support pour planifier la mise à jour (https://srv01.ceo-vision.com/osticket/index.php).



Améliorations fonctionnelles
******************************
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40
   
   "[GOFAST-5996]", "Amélioration graphique de la page 'Accès refusé' et 'Page non trouvée'"
   "[GOFAST-6482]", "Indicateur de présence des utilisateurs dans le Chat [Element]"
   "[GOFAST-5625]", "Liste utilisateurs 'Public' : remplacement du créateur 'admin' par un message (car liste créée automatiquement)"
   "[GOFAST-6087]", "Interdiction de refuser de rejoindre ou de quitter un salon de Chat associé à un Espace dont on est membre [Element]"
   "[GOFAST-6245]", "Dans le Chat : afficher en premier les salons avec des messages non lus (ou récents) [Element]"
   "[GOFAST-6384]", "Profil utilisateur : ajout de la mention Extranet pour les utlisateurs ayant ce rôle"
   "[GOFAST-6191]", "Améliorer l'aperçu des documents affiché à partir des actions contextuelles (menu burger, ex : depuis résultat de recherche)"
   "[GOFAST-6427]", "Affichage du message 'vous êtes en lecture seule' sur un document si l'état est 'Pré-Archivé'"
   "[GOFAST-6527]", "Masquer le menu 'conversation' sur le client Mobile [Element]"
   "[GOFAST-6305]", "Enlever la fonctionnalité de partage de message [Element]"
   "[GOFAST-6323]", "Améliorer l'affichage du bloc des options de recherche (largeur fixe trop petite)"
   "[GOFAST-6353]", "Arriver sur le bon salon de discutions après un clic sur une notification navigateur du Chat [Element]"
   "[GOFAST-6402]", "Permettre de partager des images dans le Chat (avec un copier-coller)"
   "[GOFAST-6170]", "Masquer les listes non accessibles plutôt qu'afficher 'vous n'avez pas le droit de voir la liste' ou 'liste cachée'"
   "[GOFAST-6211]", "Correction d'un problème de paramétrage par défaut lors de la création d'un salon de discussion"
   "[GOFAST-5522]", "Vérifier et corriger la configuration du serveur de date/temps en prenant en compte les fuseaux horaires"
   "[GOFAST-6205]", "Mise à jour d'OnlyOffice 5.6.4 (5.5.5 en ancienne numérotation)"
   "[GOFAST-6097]", "Afficher l'espace de stockage dans les status en GB plutôt qu'en Octets"
   "[GOFAST-6450]", "Amélioration de l'affichage de la popup de gestion des emplacements d'un document"
   "[GOFAST-6290]", "Pouvoir utiliser l'opérateur 'OU' dans la requête de synchronisation LDAP/AD"
   "[GOFAST-4682]", "Afficher 'Supprimer' dans la notification email de 'Synthèse d'activité'"
   "[GOFAST-6561]", "Conserver le style du texte dans le commentaire lors de la création d'un version majeure"
   "[GOFAST-5753]", "Publication en masse : ne pas transformer les images en PDF"
   "[GOFAST-6174]", "Permettre l'ajout d'un lien dans le descriptif d'une tâche 'card kanban'"
   "[GOFAST-6175]", "Afficher l'emplacement dans le paramétrage des notifications et l'email"
   "[GOFAST-6293]", "Permettre la création d'Etiquette commencant par un chiffre"
   "[GOFAST-6418]", "Masquer les utilisateurs qu'on n'a pas le droit de voir, plutôt que d'afficher 'vous n'avez pas les droits pour voir ce profile'"
   "[GOFAST-6297]", "Modifier les messages d'information et d'erreur de conexion et de récupération de mot de passe"
   "[GOFAST-6501]", "Voir les étiquettes des salons et messages privés quand le chat est replié"
   "[GOFAST-6426]", "Enlever le message 'Mise a jour Element' dans le volet du Chat [Element]"
   "[GOFAST-6573]", "Masquer certains messages 'toasters' lors de la modification de la page d'un Espace"

   

Améliorations techniques
**************************
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40

   "[GOFAST-6451]", "Ajout du résultat du contrôle d'intégrité dans les logs remontés par Graylog"
   "[GOFAST-6481]", "Extension du contrôle d'intégrité LDAP effectué lors du login aux listes d'utilisateurs"
   "[GOFAST-3453]", "Centralisation des logs (outil utilisé 'Graylog')"
   "[GOFAST-5532]", "Mise à jour PDF.js 2.6.347"
   "[GOFAST-5987]", "La touche 'Suppr' du clavier peut désormais supprimer d'autres types de contenus sélectionnés dans l'explorateur de fichiers (dossiers, espaces)"
   "[GOFAST-6343]", "Mise à jour du Chat 1.7.5 [Element]"
   "[GOFAST-6442]", "Rendre altérable par des modules clients le système de permissions du tableau de bord des processus"
   "[GOFAST-6549]", "Reprendre automatiquement la configuration d'Atatus lors des mise-à-jours"
   "[GOFAST-4176]", "Amélioration de la stabilité de la Webconference Jitsi.meet"
   "[GOFAST-6015]", "Amélioration des performances lors de l'ajout d'un membre dans un Espace pour les cas où la 'table gofast_mail_queue' est trop pleine"
   "[GOFAST-6063]", "Amélioration des performances à l'ouverture de l'édition d'un profile utilisateur (ne pas charger tous les rôles dans les Espaces)"
   "[GOFAST-6214]", "Récupérer la session du Chat après rechargement 'Fn+F5' d'une page GoFAST [Element]"
   "[GOFAST-5882]", "Afficher dans Zabbix les cas où les machines de backups internes ne tournent pas"
   "[GOFAST-6187]", "Amélioration du temps de réponse du nouvel 'Annuaire utilisateurs' pour atteindre les critères qualité (lorsque le cloisonnement est actif)"
   "[GOFAST-6562]", "Annotator' PDF.js version 2.6.347"
   "[GOFAST-6050]", "Amélioration de la supervision du moteur de recherche Solr"
   "[GOFAST-6486]", "Se déconnecter de GoFAST doit détruire la session SSO"
   
  

Sécurité
**********
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40
  

   "[GOFAST-6283]", "Mise à jour tomcat-7.0.76-12.el7_8"
   "[GOFAST-6287]", "[HOTFIX] Masquer certaines informations techniques"
   "[GOFAST-6280]", "Mise à jour I18N en V 7.x-1.27"
   "[GOFAST-6107]", "Mise à jour sécurité java-1.8.0-openjdk-1.8.0.252.b09-2.el7_8"
   "[GOFAST-6108]", "Mise à jour git-1.8.3.1-23.el7_8"
   "[GOFAST-6109]", "Mise à jour ckeditor-7.x-1.19"
   "[GOFAST-6362]", "Mise à jour kernel-3.10.0-1127.18.2"
   "[GOFAST-6363]", "Mise à jour ntp-4.2.6p5-29"
   "[GOFAST-6208]", "Mise à jour Drupal Core 7.72"
   "[GOFAST-6464]", "Mise à jour Grub 2-2.02-0.86"
   "[GOFAST-6465]", "Mise à jour PHP 7.2.33-1"
   "[GOFAST-6393]", "Mise à jour dbus-1.10.24-14.el7_8"

 


Bugs
**********
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40


   "[GOFAST-6289]", "Correction de la récupération des flux RSS qui était non fontionnelle dans certains cas"
   "[GOFAST-6485]", "[HOTFIX] Afficher le champs de configuration de 'timezone' dans l'edition du profil d'un utilisateur"
   "[GOFAST-6604]", "Mettre un document à l'état archivé génère des versions mineures"
   "[GOFAST-6169]", "Mise à jour d'Ajax library v5.16.5450.0 (correctif problème sur Mac et Linux/Firefox)"
   "[GOFAST-6539]", "Correction d'un problème d'affichage des articles sur la version Mobile"
   "[GOFAST-5958]", "Intérdir le '_' (Underscore) lors du renommage des dossiers dans le bloc latéral gauche de l'Explorer"
   "[GOFAST-6096]", "A la connexion, masquer les salons dont ont n'est pas membre (expulsé) de la zone dédiée aux salons acceptés"
   "[GOFAST-6210]", "Correction de la création d'un document de traduction depuis un document existant"
   "[GOFAST-6263]", "Correction des actions en masses depuis GoFAST Explorer sur la version Mobile"
   "[GOFAST-6326]", "Au renommage d'un Espace ne pas faire remonter à l'Espace parent"
   "[GOFAST-6346]", "[HOTFIX] Permettre le bon fontionnement des web-conférences dans des environnements avec du NAT depuis JVB2"
   "[GOFAST-6370]", "HOTFIX] Permettre de se connecter au Chat si il y a un @ dans le login de l'utilisateur [Element]"
   "[GOFAST-6506]", "[HOTFIX] Ne pas perdre la version en cours lors de la suppression de versions mineures dans certains cas"
   "[GOFAST-6520]", "Actualiser automatiquement certaines informations après le renommage d'un document (bloc droite, menu contextuel)e"
   "[GOFAST-6521]", "Correction de l'ajout de mots-clés en masse"
   "[GOFAST-6524]", "Récupération de certaines actions dans les pistes d'audit"
   "[GOFAST-6530]", "Enlever les suggestions du moteur de recherche 'Solr' dans l'autocmplétion de la recherche"
   "[GOFAST-6536]", "Ajouter la suppression d'un membre d'un espace dans les pistes d'audit"
   "[GOFAST-6551]", "Les étiquettes de l'éditeur riche dans la description d'une tâche Kanban ne sont pas conservés"
   "[GOFAST-6555]", "Correction d'un bug lors de l'édition en ligne lorsqu'on fait parti d'une liste d'utilisateurs"
   "[GOFAST-6557]", "Pouvoir mettre un salon de Chat en salon favori [Element]"
   "[GOFAST-6558]", "Correction d'une erreur à la connexion vers la brique de workflows"
   "[GOFAST-6563]", "Correction d'une erreur JS sur version Mobile"
   "[GOFAST-6574]", "Lorsqu'un message est affiché dans le Chat (ex : mise à jour), impossible d'avoir le focus dans les champs de formulaire du reste de la page"
   "[GOFAST-6575]", "Correction de l'affichage des signatures dans PDF.js v2"
   "[GOFAST-6592]", "Entrer du texte dans la recherche GoFAST fait disparaître le Chat"
   "[GOFAST-4548]", "Masquer les Espace à la suite de leur suppression dans GoFAST Explorer (volet latéral de gauche) [GF Explorer]"
   "[GOFAST-4662]", "Correction de l'affichage de l'icone du format du document pour les extension avec majuscule [GF Explorer]"
   "[GOFAST-5362]", "[HOTFIX] Correction du fonctionnement de l'application Jitsi.meet client lour sur iOS, Android [Jitsi]"
   "[GOFAST-5736]", "Empêcher la création d'un doublon dans le cas d'un 'timeout' à la création d'une 'Liste d'utilisateurs'"
   "[GOFAST-5944]", "Correction de l'autosuggestion dans le champs 'mots-clefs' dans la fenêtre de 'Gestion en masse de la taxonomie'"
   "[GOFAST-6025]", "Correction de l'affichage des contenus épinglés sur le fil d'activité pour les comptes ayant accès a énormément de contenus"
   "[GOFAST-6162]", "Gestion et correction globale d'erreurs Javascript de GoFAST"
   "[GOFAST-6192]", "Correction de la navigation dans les onglets d'un Espace après le renommage de celui-ci (correction 'page non trouvée')"
   "[GOFAST-6252]", "Correction de l'arborescence des dossiers affichée lors de la modification d'une réunion quand un dossier est déjà sélectionné"
   "[GOFAST-6255]", "Correction de l'affichage du titre d'une réunion dans le fil d'ariane (de cette réunion)"
   "[GOFAST-6344]", "Lors d'un copier-coller dans l'auto complétion, impossible de valider la saisie"
   "[GOFAST-6351]", "Correction de la redirection vers la page d'une tâche 'card kanban'"
   "[GOFAST-6372]", "Correction de l'action de déplacer un sous-Espace"
   "[GOFAST-6493]", "Correction de la récupération de la session du Chat en multi-onglets après une nouvelle authentication [Element]"
   "[GOFAST-6507]", "Correction du faux message d'erreur : 'Désolé, Riot n'est pas supporté par votre navigateur'"
   "[GOFAST-6586]", "La bande du Chat casse la mise en page sur certaines pages sur la version Mobile [Element]"
   "[GOFAST-5237]", "Correction de l'édition en ligne des fichiers non Office malgré le module ITHIT installé sous Chome [ITHIT]"
   "[GOFAST-5299]", "Correction des actions en masses ne fonctionnent pas sur le GoFAST File Browser en version mobile"
   "[GOFAST-5597]", "Correction du bouton 'Répondre' dans les notifications des messages privés"
   "[GOFAST-5825]", "Correction d'un defauts d'affichage du tableau 'Kanban' sous Safari"
   "[GOFAST-6004]", "Correction de la redirection après la création d'un document vierge (vers a page du nouveau document créé)"
   "[GOFAST-6132]", "Correction des filtres dans les annuaires"
   "[GOFAST-6354]", "Problème d'actualisation d'icone et de nom lors du renommage des dossiers dans le bloc latéral gauche de l'explorer"
   "[GOFAST-6355]", "Correction d'un bug lors d'un clique droit dans le vide dans le bloc latéral gauche de l'explorateur GoFAST"
   "[GOFAST-6382]", "Correction d'un bug visuel du chat lorsqu'on reçoit une notification"
   "[GOFAST-6483]", "Correction de l'édition d'un document sous Linux-Fierfox via le module d'édition avec client lourd [ITHIT]"
   "[GOFAST-6538]", "Amélioration de la gestion de la déconnexion du chat en multi onglet"
   "[GOFAST-6542]", "Amélioration de l'affichage de la fonctionnalité 'répondre' et de l'autocomplétion du chat"
   "[GOFAST-6576]", "Correction du dfilement des pages en 'mode présentation PDF.js v2'"
   "[GOFAST-6584]", "Correction de la recherche contextuelle dans l'aperçu PDF (après clic sur un mot-clef depuis un résultat de recherche)"
   "[GOFAST-6186]", "[HOTFIX] Correction de l'affichage des citations dans Chat [Element]"
   "[GOFAST-6529]", "Correction de 'affichage de doublons du nom de l'Espace dans le GoFAST Explorer (dans certains cas)"
   "[GOFAST-6535]", "Correction du lien vers la web-conférence dans l'invitation agenda dans certains cas (.ics)"
   "[GOFAST-6537]", "Permettre la création d'un fichier zip pour le téléchargement de plusieurs documents"



Bugs mineurs
***************
.. csv-table:: 
   :header: "Ref.", "Description"
   :widths: 10, 40


   "[GOFAST-6397]", "Armoniser la photo de profil de l'utilisateur dans la vue du nouveau Chat GoFAST [Element]"
   "[GOFAST-6201]", "Réparer et améliorer le retour des versions de la GoFAST Comm dans la modal des version des composants"
   "[GOFAST-6593]", "Masquer le message d'erreur après le faire de vider le champ de la recherche"
   "[GOFAST-6069]", "Masquer le bloc 'mes relations' sur la page de login"
   "[GOFAST-5850]", "Correction du drapeau pour la langue arabe"




**Bonne utilisation de GoFAST !**

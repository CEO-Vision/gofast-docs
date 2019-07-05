********************************************
GoFAST :  Version 3.6.1
********************************************

**[GoFAST Enterprise]** Avis aux équipes techniques : N’hésitez pas à solliciter notre support pour planifier la mise à jour (https://srv01.ceo-vision.com/osticket/index.php).

**[GoFAST Communiy]** Pour que vous puissiez mettre à jour votre GoFAST Community, le serveur de mise à jour doit être accessible. Posez-vos questions sur nos forums : https://community.ceo-vision.com/

Si vous souhaitez instaler GoFAST v3.6.1, rendez-vous sur : https://www.ceo-vision.com/fr/content/gofast-community-ged-plateforme-collaborative-opensource

Nouvelles fonctionnalités
*************************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
      "[2747]","Pouvoir télécharger une image depuis son PC vers l’éditeur riche (dans forums, commentaires, accueil d’un Espace, etc.)","[Community][Enterprise]"
      "[4896]","Partager plusieurs fichiers via des URL de téléchargement par email en une fois","[Community][Enterprise]"      
      "[5086]","Ajout d’un Tableau de Bord Dynamique standard comme page d’accueil alternative","[Community][Enterprise]"
      "[5137]","Création d'un espace de chaque type (Extranet, Public, Groupe, Organisation) à l'installation de GoFAST","[Community]"
      "[5175]","Pouvoir démarrer un workflow directement depuis le panier documentaire","[Enterprise]"
      "[4743]","Pouvoir faire des exports des données soumis dans les formulaires GoFAST","[Community][Enterprise]"
   
Améliorations fonctionnelles
****************************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10

      "[4916]","Pouvoir redimensionner le volet de gauche, le volet du bas et la hauteur de GoFAST File Browser","[Community][Enterprise]"
      "[4918]","Supprimer le mot 'Commentaire' au survol d'une version de fichier quand il n'y en a aucun","[Community][Enterprise]"
      "[4919]","Possibilité de visualiser depuis les versions d'un document de travail, les versions des publications associées","[Community][Enterprise]"
      "[4984]","Ajout du Portugais dans les langues possibles pour un document","[Community][Enterprise]"
      "[5015]","Ajout d’un accès aux derniers contenus vus dans le menu principal","[Community][Enterprise]"
      "[5017]","Amélioration des notifications pour l'ajout ou le refus d'un nouveau membre dans un Espace","[Community][Enterprise]"
      "[5024]","Reprise automatique du titre du commentaire initial dans le titre du commentaire de réponse (ex. 'Re: titre du commentaire)' ","[Community][Enterprise]"
      "[5026]","Agrandissement du GoFAST File Browser (pleine page) sur la page Explorateur","[Community][Enterprise]"
      "[5064]","Amélioration du message indiquant l’interdiction de déposer des contenus à la racine (Organisation, Groupe, Extranet, Public)","[Community][Enterprise]"
      "[5081]","Toujours ouvrir l'onglet 'Documents' quand on arrive sur la page d'un Espace","[Community][Enterprise]"
      "[5119]","Ajout de certains évènements dans les filtres d'audit et correctifs","[Community][Enterprise]"
      "[5124]","Ajout de l’Arabe dans les langues possibles pour un document","[Community][Enterprise]"
      "[5129]","Prise en charge du format vidéo MPEG pour la lecture en streaming","[Community][Enterprise]"
      "[5180]","Partage d’un document par e-mail : Pouvoir saisir en une seule fois plusieurs adresses e-mails séparées par des virgules, point virgules ou des espaces dans le champs 'Destinataires' ","[Community][Enterprise]"
      "[5085]","Amélioration de l'ergonomie de la popup de gestion des Emplacements/Visibilité","[Community][Enterprise]"
      "[5095]","Traduction de certaines chaines de l’anglais vers le français","[Community][Enterprise]"
      "[5097]","Augmentation du nombre d'éléments affichés dans certains filtres de recherche","[Community][Enterprise]"
      "[5127]","Remplir le champs URL d’une invitation agenda (fichier ICS) de messagerie (ex: Outlook) avec l'URL d’accès à la webconférence GoFAST","[Community][Enterprise]"
      "[5138]","Déplacement d’éléments du menu 'profil utilisateur' vers le menu burger 'bouton magique' : Configuration, Import utilisateurs, Audit, Statistiques","[Community][Enterprise]"
      "[5190]","Amélioration du fonctionnement lorsque le fil d'activité est vide","[Community][Enterprise]"

Améliorations techniques
************************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10

      "[3347]","Mise en place de la rotation des logs VM GOFAST","[Community][Enterprise]"
      "[4624]","Mise à jour WebDAV Ajax Library 5.8.X","[Community][Enterprise]"
      "[4849]","Corriger l’alerte MYSQL : 'innodb_index_stats has length mismatch' ","[Community][Enterprise]"
      "[5132]","Griser le bouton de mise-à-jour 'Majeur' tant que les HOTFIX n'ont pas été passés","[Community]"
      "[5131]","Empêcher Alfresco de ralentir les autres services au démarrage du serveur GoFAST","[Community][Enterprise]"
      "[5130]","Détection de la langue du clavier lors de l’instanciation de la GoFAST dans l’outil de virtualisation","[Community]"
      "[5212]","Amélioration des performances lors de la création d’une liste d’utilisateurs sur certains environnements","[HOTFIX][Community][Enterprise]"

Sécurité
********
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
      "[4118]","Remplir le champs 'Mot de passe' dans la configuration du serveur de messagerie SMTP","[Community][Enterprise]"
      "[4815]","Etude et ajout d'un Système de Détection d'Intrusion","[Community][Enterprise]"
      "[4976]","Correction du système de perte de session utilisateur automatique après 10 heures","[Community][Enterprise]"
      "[5069]","Mise à jour sécurité Python","[Community][Enterprise]"
      "[5071]","Mise à jour sécurité Drupal 7.67","[Community][Enterprise]"
      "[5134]","Changement du mot de passe temporaire MYSQL pour l'utilisateur root à l’installation","[Community]"
      "[5136]","Suppression des mots-de-passe dans le récapitulatif affiché en fin de configuration de GoFAST, après installation","[Community]"
      
Bugs
****
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
   
      "[3188]","Afficher les icônes de style dans l’éditeur riche des forums et des résumés","[Community][Enterprise]"
      "[3965]","Depuis la vue 'plein écran' sur un document, revenir à l’affichage normal après un clic sur 'retour' (bouton du navigateur)","[Community][Enterprise]"
      "[4380]","Correction de la prévisualisation d'un fichier au format EML","[Community][Enterprise]"
      "[4535]","Correction d’un bug lors de l’ajout d'une page Wiki dans un livre","[Community][Enterprise]"
      "[4819]","Empêcher la suppression d’un Espace archivé","[Community][Enterprise]"
      "[4869]","Correction de la sauvegarde manuelle des documents depuis OnlyOffice (bouton 'enregistrer sur GoFAST' pour créer une version du fichier sans fermer OnlyOffice)","[Enterprise]"
      "[4883]","Empêcher la roue d'attente de tourner dans le vide après une demande pour rejoindre un Espace","[Community][Enterprise]"
      "[4884]","Actualiser le fil d'Ariane après changement du/des emplacement(s) d’un document (sur la page du document)","[Community][Enterprise]"
      "[5012]","Permettre à l’administrateur d’un Espace de modifier sa page d'accueil même s’il n'est pas administrateur de l’Espace parent","[Community][Enterprise]"
      "[5044]","Correction d’un bug aléatoire dans la construction du lien de l'emplacement du document dans le bloc d’information (page du document)","[Community][Enterprise]"
      "[5045]","Correction d'une erreur ajax sur GoFAST Mobile lors d’un clic sur le bouton de recherche pendant le chargement des autosuggestions","[Community][Enterprise]"
      "[5060]","DUA (durée d’utilité administrative) : correction de l’envoi des e-mails de notification","[Community][Enterprise]"
      "[5065]","Multi-emplacement : permettre de décocher des emplacements présélectionnés (problème lié aux listes d’utilisateurs)","[Community][Enterprise]"
      "[5074]","Partage d’un document par e-mail : pouvoir soumettre le formulaire quand le destinataire est une liste d’utilisateurs","[HOTFIX][Community][Enterprise]"
      "[5077]","Correction de l’édition en ligne de documents avec LibreOffice sous UBUNTU","[Community][Enterprise]"
      "[5078]","Correction du comparateur des versions d’un document","[Community][Enterprise]"
      "[5083]","Correction de l'apparition de la popup 'Wrapper auth' (sans session authentifiée)","[HOTFIX][Community][Enterprise]"
      "[5092]","Empêcher le redémarrage d'Alfresco via le cron, si celui est déjà en cours de redémarrage","[Community][Enterprise]"
      "[5105]","Correction du lien accepter/refuser un membre en attente depuis un espace","[HOTFIX][Community][Enterprise]"
      "[5106]","Permettre les requêtes vers Bonitasoft quand le serveur GoFAST est derrière un proxy","[Enterprise]"
      "[5111]","Correction d’un bug aléatoire dans l'affectation du rôle lors de l'ajout d'un nouveau membre à un espace","[Community][Enterprise]"
      "[5115]","Liste d'utilisateurs : exclure les Groupes des autosuggestions du formulaire","[HOTFIX][Community][Enterprise]"
      "[5117]","Redéploiement des filtres dans l'annuaire des utilisateurs bloqués","[Community][Enterprise]"
      "[5125]","Permettre la restauration d’un formulaire supprimé","[Community][Enterprise]"
      "[5133]","Masquer le bouton d’accès à la version Mobile de GoFAST tant que le nom de domaine n’est pas configuré","[Community]"
      "[5177]","Gestion en masse des emplacements depuis le panier : les emplacements présélectionnés dans le formulaire ne sont pas les bons","[Community][Enterprise]"
      "[5188]","Correction du 'glisser-déposer' d’un document dans GoFAST File Browser quand il est en pleine page","[Community][Enterprise]"
      "[5201]","Interface de gestion en masse des membres : empêcher le bouton 'sélectionner tout' de sélectionner les valeurs cachées","[Community][Enterprise]"
      "[5204]","Correction d’une erreur JS bloquante sous IE","[HOTFIX][Community][Enterprise]"
      "[5210]","Création d’utilisateur depuis un espace : redonner accès à un administrateur d’espace au formulaire de création d'un compte utilisateur, même s'il n'a pas le rôle d'administrateur de plateforme","[HOTFIX][Community][Enterprise]"
      

Bugs mineurs
************
.. csv-table::  
   :header: "Ref.", "Description", "Catégorie"
   :widths: 10, 40, 10
      
      "[4678]","PB : le bloc de gauche se déplie trop souvent","[Community][Enterprise]"
      "[4909]","Empêcher la gestion de certains espaces depuis GoFAST File Browser","[Community][Enterprise]"
      "[4911]","Gestions des membres : icones des espaces dans le ztree non cohérentes","[Community][Enterprise]"
      "[4926]","Emplacement plus lisible sur une ligne dans le fil d'activité","[Community][Enterprise]"
      "[4972]","Partage de document par email : empêcher la soumission si adresse e-mail non renseignée","[Community][Enterprise]"
      "[5107]","Correction de l’apparence du bouton 'Rejoindre la conférence' sur certains clients de messageries","[Community][Enterprise]"
      "[5035]","Supprimer le message 'Access denied' en bas de page sur l'écran de connexion sur la version mobile","[Community][Enterprise]"
      "[5072]","Le polling de l'icône workflow d'un document ne fonctionne plus","[Community][Enterprise]"
      "[5113]","Harmonisation du formulaire de création d’utilisateur accessible depuis la page d’un Espace avec le celui accessible depuis le menu principal","[Community][Enterprise]"
      "[5176]","Fixer la hauteur de la prévisualisation d'une image (sur la page du document)","[Community][Enterprise]"      
      


**Bonne utilisation de GoFAST !**

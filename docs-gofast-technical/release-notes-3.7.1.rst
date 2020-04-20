********************************************
GoFAST :  Version 3.7.1
********************************************

**[GoFAST Enterprise]** N’hésitez pas à solliciter notre support pour planifier la mise à jour (https://srv01.ceo-vision.com/osticket/index.php).

**[GoFAST Community]** Pour que vous puissiez mettre à jour votre GoFAST Community, le serveur de mise à jour doit être accessible. Posez-vos questions sur nos forums : https://community.ceo-vision.com/


Nouvelles fonctionnalités
***************************
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40
   
   "[GOFAST-3535]", "Guide de démarrage avec GoFAST (Carousel explicatif)"
   "[GOFAST-2582]", "Chat-Messagerie Instantanée avec des groupe de discussions (Salon)"
   "[GOFAST-3296]", "Modèle d’arborescence de répertoires"
   "[GOFAST-4885]", "Gestion collaborative des tâches sous forme Kanban (= type Trello)"
   "[GOFAST-4981]", "Option de recherche 'stricte' (en plus de la recherche actuelle considérée comme étendue)"
   "[GOFAST-5014]", "Accéder à la piste d’audit depuis la page d'un document (uniquement pour les ‘super-administrateur’)"
   "[GOFAST-5029]", "Sauvegarde des critères de recherche"
   "[GOFAST-5031]", "Pouvoir passer le document d’origine/de travail en version majeure lors d'une publication"
   "[GOFAST-5032]", "Afficher le formulaire de connexion sur la page de téléchargement d’un document transmis par e-mail sous forme de lien de téléchargement"
   "[GOFAST-5120]", "Nouveau Tableau de Bord des Workflows"
   "[GOFAST-5123]", "Système d’authentification SingleSignOn (SSO SAML)"
   "[GOFAST-5336]", "Notion d'utilisateur 'supprimé' (ayant quitté l'organisation)"
   "[GOFAST-5391]", "Pouvoir afficher la liste des emplacements d’un document et les droits de l’utilisateur sur les divers contenus (Documents, Espaces…) dans GoFAST File Browser"
   "[GOFAST-4846]", "Pouvoir archiver en masse les documents depuis le panier documentaire et GoFAST File Browser"
   "[GOFAST-5358]", "Notification de suppression d'un membre d'Espace envoyée aux administrateurs de l’Espace et à l’utilisateur concerné"
   "[GOFAST-5598]", "Création d'un champ 'Référence Documentaire' avec un libellé paramétrable"

  
Améliorations fonctionnelles
******************************
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40
   
   "[GOFAST-5426]", "Export complet des informations relatives aux Espaces depuis la vue des statistiques"
   "[GOFAST-3588]", "Avoir des administrateurs 'métiers' de l'Espace Public pouvant ajouter du contenus"
   "[GOFAST-4000]", "DUA : Application rétroactive de la DUA (Durée d’Utilité Administrative)"
   "[GOFAST-4892]", "Pouvoir arrêter le chargement d'un fichier unitairement dans la file d’attente de GoFAST File Browser"
   "[GOFAST-4917]", "Regrouper les notifications d'ajout/suppression de membres, pour les administrateurs d'Espaces"
   "[GOFAST-5051]", "Ajout d’un lien vers le profil de l'utilisateur dans la notification d'utilisateur bloqué"
   "[GOFAST-5004]", "Liste Utilisateurs : possibilité de donner le rôle d’administrateur d’une liste à d’autres utilisateurs en plus du créateur de la liste"
   "[GOFAST-5139]", "Blog : pouvoir épingler, éditer et supprimer les messages à tout moment (pour le créateur du message)"
   "[GOFAST-5171]", "Avoir l’autosuggestion des contenus lors de la saisie des numéros de référence des contenus (numéro du ‘node’ dans l’URL)"
   "[GOFAST-5187]", "Mise à jour de la Suite OnlyOffice 5.4.1 : nouvelles fonctionnalités, améliorations et ergonomie plus proche de la Suite de MS Office365 (release note OnlyOffice : https://helpcenter.onlyoffice.com/fr/server/document/changelog.aspx)"
   "[GOFAST-5192]", "Amélioration de la gestion en masse des emplacements/visibilité des documents"
   "[GOFAST-5195]", "Empêcher le changement de l'extension des fichiers dans GoFAST File Browser, lors du renommage d’un fichier"
   "[GOFAST-5202]", "Evolution du système de prévisualisation (basé OnlyOffice en plus de LibreOffice)"
   "[GOFAST-5352]", "Interface mobile : amélioration de l’affichage des Espaces sur le profil utilisateur"
   "[GOFAST-5385]", "Regroupement des actions d'administration de la plateforme du menu contextuel dans un sous-menu (uniquement pour les administrateurs système)"
   "[GOFAST-5400]", "Identification des fichiers ayant l’extension .mov en tant que format vidéo (permet la lecture en streaming)"
   "[GOFAST-5409]", "Réorganisation des actions du menu contextuel d'un document (le ‘Burger menu’)"
   "[GOFAST-5140]", "Amélioration de l’affichage des contenus liés dans la popup de modification des contenus liés, si beaucoup de contenus"
   "[GOFAST-5146]", "Déplier les dossiers ‘TEMPLATES’ par défaut dans l’arborescence, permettant de sélectionner le modèle plus rapidement, lors de la création d’un document"
   "[GOFAST-5323]", "Indexation des comptes bloqués plus cohérente : exclus par défaut et recherchables via un filtre"
   "[GOFAST-5309]", "Amélioration de diverses traductions (anglais, français, néerlandais)"
   "[GOFAST-5411]", "Amélioration et uniformisation de la taxonomie de certaines actions en masses"
   "[GOFAST-5548]", "Gris plus foncé pour la police"
   "[GOFAST-5603]", "Amélioration d'affichage 'Supprimer des favoris'"
   "[GOFAST-5679]", "Améliorer la compréhension de la modification des recherches sauvegardées"
   "[GOFAST-5730]", "Ne plus générer de mot de passe envoyé par mail lors de la création des comptes"
   "[GOFAST-5738]", "Empêcher de pouvoir naviguer sur la plateforme pendant la session temporaire de récupération de mot de passe"
   "[GOFAST-5818]","Améliorer l'affichage des erreurs"
   

Améliorations techniques
**************************
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40
   
   "[GOFAST-4982]", "Supervision : avoir le nombre d’utilisateurs connectés dans l'heure et le nombre de documents non indexés dans Zabbix"
   "[GOFAST-5256]", "Asynchroniser l'archivage d'espace (éxecution en arrière plan)"
   "[GOFAST-5320]", "Réinitialisation de la date des VM au lancement de celles-ci"
   "[GOFAST-5337]", "Permettre de filtrer les utilisateurs pendant la synchronisation LDAP"
   "[GOFAST-5355]", "Extension des actions auditées : téléchargement et publication"
   "[GOFAST-5364]", "Eviter le rechargement de GoFAST File Browser après le dépôt d'un fichier"
   "[GOFAST-5366]", "Améliorations diverses des API GoFAST (pour étendre les possibilités dans les workflows)"
   "[GOFAST-5369]", "Activation du module HTTP Upload d'Ejabberd : Transfert de fichiers/images dans le Chat"
   "[GOFAST-5415]", "Amélioration des performance à cause du hook node_access sur environnements avec beaucoup d'espaces"
   "[GOFAST-5422]", "Ajout d’un champs 'summary' (décrit l'état en cours d'un workflow) dans l'objet BDM processHistory"
   "[GOFAST-5432]", "Amélioration des performances du formulaire de création de document lorsqu’il y a de nombreux modèles de documents"
   "[GOFAST-5437]", "Amélioration des performance du bloc des métadonnées (dans le cas où il y a un grand nombre d’Espaces)"
   "[GOFAST-5441]", "Optimiser le temps de chargement de la page d'un espace"
   "[GOFAST-5444]", "Supervision : ajout du nombre de connexion maximum MySQL dans Zabbix"
   "[GOFAST-5446]", "Optimisation des performances de l'audit pendant la création d'un contenu"
   "[GOFAST-5453]", "Optimisation des performances du fil d'activité"
   "[GOFAST-5457]", "Optimiser le temps de chargement d'un profil"
   "[GOFAST-5459]", "Amélioration des performances de création d'un compte-utilisateur"
   "[GOFAST-5460]", "Mise à jour librairie ITHit WebDAV AJAX Library v5.10.4919.0"
   "[GOFAST-2342]", "Sauvegarde des historiques des échanges dans le Chat côté serveur JSXC (Chat Ejabberd)"
   "[GOFAST-2568]", "Réduire le nombre de sessions Tomcat non nécessaires"
   "[GOFAST-2625]", "Optimisations JVM : Garbage Collector G1, paramètres optimisation mémoire et compatibilitée JDK 1.8"
   "[GOFAST-2710]", "OpenLDAP : amélioration des performances au démarrage et des logs transactionnels"
   "[GOFAST-5368]", "Amélioration de l'auto-restart des services"
   "[GOFAST-5442]", "Supervision : récupération des données IOSTAT/MYSQL dans Zabbix"
   "[GOFAST-5255]", "Amélioration de l’expérience utilisateur lors d’un déplacement d'un Espace qui est désormais fait de manière asynchrone"
   "[GOFAST-5321]", "Interdiction du choix de l'état 'archivé' pour les contenus dans la gestion en masse de la taxonomie (l’archivage est fait via la fonction 'Archiver' sous condition d’en avoir les droits)"
   "[GOFAST-5443]", "Réduction de la place disque utilisé par le mécanisme de contrôle d'intégrité de l'annuaire LDAP"
   "[GOFAST-2886]", "Mise à jour EJABBERD version 19.05"
   "[GOFAST-4437]", "Mise à jour Alfresco 5.2g - General Release : 201707"
   "[GOFAST-4621]", "Mise à jour JSXC 4.0 (serveur de Chat Ejabberd)"
   "[GOFAST-5392]", "Retirer la possibilité de désactiver les notifications depuis la gestion en masse"
   "[GOFAST-5447]", "Retirer la sauvegarde interne des erreurs JS"
   "[GOFAST-4994]", "Supervision Zabbix httpd"
   "[GOFAST-5538]", "Mise en place d'un mécanisme de vérification de l'intégrité des droits des documents et des espaces, lié à la réplication"
   "[GOFAST-5807]", "Amélioration de performance du mécanisme de vérification de la fiabilité de connexion avec OnlyOffice"


Sécurité
**********
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40
   
   "[GOFAST-5471]", "[Multiple CVE] Mise à jour kernel CentOS kernel-3.10.0-1062.7.1.el7"
   "[GOFAST-5528]", "Mise-à-jour du module Localization"
   "[GOFAST-5545]", "RHSA-2019:2964 : Mise à jour du paquet patch-2.7.1-12.el7"
   "[GOFAST-5546]", "RHSA-2019:3128 Mise à jour du paquet java-1.8.0-openjdk-1.8.0.232.b09-0.el7"
   "[GOFAST-5653]", "Vérification de la désactivation de TLSv1 TLSv1.1 et certains Cyphers sur GoFAST COMM"
   "[GOFAST-5723]", "[CVE] Mise à jour nss-3.44.0-7.el7_7.x86_64"


Bugs
**********
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40

   "[GOFAST-4697]", "Scalabilité : Annuaire des utilisateurs actifs / inactifs"
   "[GOFAST-4920]", "Le bouton ‘Annoter’ ne doit pas être visible dans le preview PDF sur la version PC"
   "[GOFAST-5228]", "Message privé : correction ‘page non trouvée’ après un clic sur ‘répondre’ dans la notification e-mail"
   "[GOFAST-5388]", "Correction de la mise à jour d’un PDF par glisser-déposer quand l’extension est en majuscule"
   "[GOFAST-5420]", "Résolution des problèmes de performance liés à de grosses volumétries"
   "[GOFAST-5421]", "L’autocomplétion de recherche est trop lente si beaucoup documents et d’espaces"
   "[GOFAST-5468]", "La sélection d’une catégorie non-standard créé parfois un doublon de celle-ci"
   "[GOFAST-5557]", "Correction de l’affichage de la vue des favoris personnels"
   "[GOFAST-5609]", "Clarifier le message sur la complexité du mot de passe (Contraintes obligatoires)"
   "[GOFAST-5620]", "Le mécanisme de mise à jour passe plusieurs fois les mises à jour GoFAST COMM"
   "[GOFAST-5654]", "Correction problème d’import de users depuis LDAP après la navigation sur une autre page"
   "[GOFAST-5656]", "Lors d’un lock Microsoft Office, le menu contextuel ne grise pas certaines actions après un rechargement de page"
   "[GOFAST-5661]", "Corriger les doublons de dossiers épinglés sur le tableau de bord causant des bugs dans l’explorateur et des doublons dans les favoris"
   "[GOFAST-5663]", "Le comparateur de version se trompe de version au dessus de la version X.9"
   "[GOFAST-5666]", "La mémoire allouée à Solr n’est pas adaptée à tous les environnements"
   "[GOFAST-5693]", "Gérer les renommages des dossiers pour éviter les favoris morts"
   "[GOFAST-5696]", "Profil : champs 'Demande d’accès à' toujours vide"
   "[GOFAST-5712]", "COMMUNITY : Avoir une apostrophe dans le mot de passe MySQL fait planter la configuration"
   "[GOFAST-5716]", "Lors du téléchargement d’un document partagé par mail, si le titre contient un espace, le nom du document est coupé"
   "[GOFAST-5732]", "Mettre un message d’erreur compréhensible lorsqu’on accède à un lien de partage expiré"
   "[GOFAST-5733]", "Correction problème pour retirer un emplacement quand un document est multifilé plusieurs fois dans le même espace"
   "[GOFAST-5744]", "Mettre un lien vers le fil d’activité dans le menu de la version mobile"
   "[GOFAST-5745]", "DUA : L’adresse mail de notification n’est pas enregistrée"
   "[GOFAST-5763]", "En version mobile, la zone principale de contenu ne prend pas toute la largeur"
   "[GOFAST-5767]", "Un article multifilé apparaît plusieurs fois dans le bloc article d’un espace"
   "[GOFAST-5769]", "Rajouter le champ Broadcast dans la fenêtre de publication"
   "[GOFAST-5772]", "Dans la page de recherche, on affiche 2 fois l’étiquette correspondante à l’état sur les résultats de recherche"
   "[GOFAST-5785]", "Le bloc des livres n’apparait plus sur les articles dans les livres"
   "[GOFAST-5805]", "Limiter l’appel à l’API de génération du ticket de session Ejabberd"
   "[GOFAST-5822]", "Permission : impossible de renommer un espace pour un admin d’un seul espace"

   
Bugs mineurs
***************
.. csv-table:: 
   :header: "Ref.", "Description"
   :widths: 10, 40

   "[GOFAST-5047]", "Correction de l’affichage de la liste des tâches d’un processus (workflow) sur l’interface mobile"
   "[GOFAST-5144]", "Correction de l'affichage de la hauteur du champ de renommage d'un fichier dans GoFAST File Browser"
   "[GOFAST-5157]", "Correction du bug d’affichage des contenus en double dans le GoFAST File Browser"
   "[GOFAST-5168]", "Empêcher que des emplacements non désirés se déplient dans l'arborescence de GoFAST File Browser"
   "[GOFAST-5205]", "Griser le bouton 'Nouveau' dans le menu du GoFAST File Browser quand on est dans un Espace archivé"
   "[GOFAST-5334]", "Supervision : rermettre le démarrage automatique de Zabbix pour les nouvelles installations de GoFAST"
   "[GOFAST-5367]", "Permettre de faire du multi-lignes dans le mail de Bienvenue"
   "[GOFAST-5381]", "Correction d'un bug qui empêche de modifier les participants d'une réunion"
   "[GOFAST-5382]", "Empêcher l’affichage du bouton renommer dans le menu contextuel d'un Espace (le ‘burger menu’) si l’action n’est pas permise à l’utilisateur" 
   "[GOFAST-5405]", "Vider le contenu du champ message après soumission dans les mails internes"
   "[GOFAST-5419]", "Correction message d'erreur lors de la création d'un document depuis un fichier vide sans sélectionner de type"
   "[GOFAST-5438]", "Message d'erreur lors de l'export de l'audit"
   "[GOFAST-5495]", "Message d'erreur quand partage d’un document par e-mail via lien URL de téléchargement"
   "[GOFAST-5643]", "Correction perte du nom de l'organisation principale de l'utilisateur dans le snippet de la recherche"
   "[GOFAST-5743]", "Correction des actions contextuelles dans la version mobile sur l'explorateur de fichier"
   "[GOFAST-5758]", "Pouvoir créer un document depuis un modèle depuis le résultat de recherche"


**Bonne utilisation de GoFAST !**

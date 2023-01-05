********************************************
GoFAST :  Version 4.0.1
********************************************

**[GoFAST Enterprise]** N’hésitez pas à solliciter notre support pour planifier la mise à jour (https://srv01.ceo-vision.com/osticket/index.php).


Nouvelles fonctionnalités 
*****************************

.. csv-table::
   :header: "Ref.", "Description"
   :widths: 1000, 60000
   
   "[GOFAST-4833]","Nouvelle fonctionnalité : Outil de gestion des étiquettes (fusion, correction, ...)"
   "[GOFAST-8999]","Nouvelle fonctionnalité permettant de disposer d'une API d'auto-complétion par liste d'utilisateur"
   "[GOFAST-8757]","Permettre de charger un document sur mobile"
   "[GOFAST-7216]","Amélioration grace à l'affichage de la description d'un espace lors de son survol"
   "[GOFAST-8010]","Ajout d'alerte de supervision en cas de sealert dans les logs"
   
 
   


Améliorations 
******************************

**Améliorations Fonctionnelles & Techniques**


.. csv-table::
   :header: "Ref.", "Description"
   :widths: 1000, 60000
  

  

   "[GOFAST-8872]","Amélioration : pouvoir filtrer par utilisateur dans certaines colonnes de l'annuaire des espaces	"
   "[GOFAST-8620]","Amélioration de l'affichage du Titre avec le fil d'ariane en dessous permettant de voir les titres longs et une meilleure lisbilité	"
   "[GOFAST-9103]","Amélioration de la page d'accueil d'espace évitant de repousser les blocs (favoris,...) vers le bas si la page wiki de l'espace est longue	"
   "[GOFAST-8538]","Amélioration de la page de téléchargement lors d'un partage par email	"
   "[GOFAST-7413]","Amélioration de la sécurisation de certains cookies	"
   "[GOFAST-8818]","Amélioration du temps de réponse d'affichage des modèles si très nombreux	"
   "[GOFAST-8739]","Amélioration performance du fil d'activité si beaucoup d'espaces	"
   "[GOFAST-7810]","Amélioration permettant aux autres utilisateurs que le créateur de supprimer les modèles de dossier	"
   "[GOFAST-9055]","Adapter les statistiques de processus pour le workflow standard	"
   "[GOFAST-8814]","Message d'alerte lors qu'on retire un membre d'un espace alors qu'il en reste membre car aussi dans une liste de cet espace	"
   "[GOFAST-8903]","Mise à jour de Jitsi Meet v1.0.6644	"
   "[GOFAST-9319]","Mise à jour Onlyoffice v7.2.2 (ligature, tableau OLE, performance des polices, ajout du portugais ... et correctifs dont format odf et sécurité)	"
   "[GOFAST-9196]","Supervision de la création des objets temporaires dans la base de données (Zabbix)	"
   "[GOFAST-8773]","Mise à jour VM2 (Comm) Java 11	"
   "[GOFAST-9225]","Mise à jour de l'agent Zabbix (v2)"
   "[GOFAST-9190]","Ajout d'une supervision Zabbix des requêtes lentes de la base de données MySQL 	"



   

Sécurité 
******************************
.. csv-table::
   :header: "Ref.", "Description"
   :widths: 1000, 60000
  
   "[GOFAST-7661]","Correction de la vulnérabilité potentielle CVE-2021-45105 (DDOS log4j)"
   "[GOFAST-9090]","Mise à jour sécurité de Tomcat en version 9.0.68"
   "[GOFAST-8434]","Remplacement dans la mesure du possible des requete exec et shell_exec"
  
   
   

Bugs 
******************************
.. csv-table::
   :header: "Ref.", "Description"
   :widths: 1000, 60000
   
   
   
   "[GOFAST-6215]","[MOUNTAINDUCK] Correction par l'éditeur d'un bug critique renommant la version serveur plutot que de versionner avec la version locale modifiée hors-ligne"
   "[GOFAST-7886]","[MOUNTAINDUCK] Correction par l'éditeur d'un bug empêchant d'ouvrir les fichiers bureautiques hors ligne	"
   "[GOFAST-8834]","[ONLYOFFICE] Correction par Onlyoffice d'une perte de retour à la ligne sur les formts ODP (OpenDocument)	"
   "[GOFAST-8736]","Amélioration de la zone vertical d'édition de texte pour les wikis	"
   "[GOFAST-7198]","Amélioration des notifications d'adhésion à un espace (thème GoFAST v4)	"
   "[GOFAST-8160]","Amélioration du message d'erreur lors de l'echec de l'envoi à Yousign pour signature	"
   "[GOFAST-8873]","Correction d'un bug faisant que dans certains cas le menu contextuel des listes d'utilisateur ne s'affichait pas	"
   "[GOFAST-8622]","Correction d'un bug occasionnel affichant un profil erroné dans le chat	"
   "[GOFAST-9329]","Correctifs de lancement des tâches workflows sur la page d'un document	"
   "[GOFAST-8794]","Correction d'un blocage des notifications par email	"
   "[GOFAST-8600]","Correction d'un bug affichant le document dans le fil d'activité lorsqu'il était partagé par email	"
   "[GOFAST-9122]","Correction d'un bug affichant une erreur lors du clic d'un élément du fil d'ariane juste après un renommage 	"
   "[GOFAST-9089]","Correction d'un bug affichant une liste supprimée null dans un espace	"
   "[GOFAST-8787]","Correction d'un bug d'affichage mélangeant les Go et To dans les statistiques	"
   "[GOFAST-9288]","Correction d'un bug de rechargement intempestif de la page d'un forum	"
   "[GOFAST-9094]","Correction d'un bug empechant de renommer un espace par le menu contextuel dans l'arborescence de gauche de l'explorateur	"
   "[GOFAST-9232]","Correction d'un bug empechant l'affichage correct des puces numérotés dans un commentaire	"
   "[GOFAST-9334]","Correction d'un bug empechant la prévisualisation sur iPAD de doc excel	"
   "[GOFAST-8796]","Correction d'un bug empechant la prévisualisation des format SVG	"
   "[GOFAST-8678]","Correction d'un bug empechant la prévisualisation sous Safari IPAD	"
   "[GOFAST-9156]","Correction d'un bug empechant occasionnellement de créer un document à partir d'un modèle	"
   "[GOFAST-9260]","Correction d'un bug empéchant affichage statistiques globales	"
   "[GOFAST-9153]","Correction d'un bug empéchant aléatoirement la synchronisation des listes d'utilisateur avec l'annuaire	"
   "[GOFAST-9136]","Correction d'un bug lors d'une recherche s’exécutant avec le mot clef du titre de la recherche sauvegardée au lieu du contenu de celle-ci"
   "[GOFAST-9180]","Correction d'un bug multipliant les requetes afin de l'amélioration de la performance des statistiques d'un espace	"
   "[GOFAST-8315]","Correction d'un bug n'affichant pas le lieu dans la notification d'une réunion/webconférence	"
   "[GOFAST-9204]","Correction d'un bug n'appliquant plus le rôle par défaut lors de l'ajout d'un utilisateur à un espace	"
   "[GOFAST-9072]","Correction d'un bug occasionnel empéchant l'ouverture du bon commentaire lors d'une ré-edition immédiate	"
   "[GOFAST-8632]","Correction d'un bug occasionnel indiquant Aucun rôle lors de l'ajout d'une liste à un espace 	"
   "[GOFAST-8942]","Correction d'un bug occasionnel lors de la publication d'un document et la prévisualisation	"
   "[GOFAST-7901]","Correction d'un bug occationnel laissant une carte supprimée dans le tableau Kanban	"
   "[GOFAST-9086]","Correction d'un bug permettant de supprimer les répertoires Wikis	"
   "[GOFAST-9244]","Correction d'un bug qui empéchait l'ouverture du volet de gauche sur la page d'accueil d'un espace pour voir les wikis	"
   "[GOFAST-9117]","Correction d'un bug sur la page d'accueil où le lien vers la documentation n'est pas le bon	"
   "[GOFAST-9205]","Correction d'un message d'erreur Cet élément ne peut pas être supprimé alors que le répertoire a bien été supprimé	"
   "[GOFAST-8367]","Correction d'un problème d'affichage qui affichait un volet gris lors du renommage d'un fichier	"
   "[GOFAST-7924]","Correction d'un problème d'affichage sur IPAD de cases à cocher rognées	"
   "[GOFAST-8765]","Correction d'un problème de document partagé avec un espace personnel	"
   "[GOFAST-8968]","Correction d'un problème de multifiling avec caractère &	"
   "[GOFAST-8881]","Correction d'un problème de performance sur les annuaires de liste d'utilisateurs	"
   "[GOFAST-8907]","Correction d'un problème de quelques logs pas dans le bon emplacement (/var/log)	"
   "[GOFAST-8265]","Correction d'un problème de synchronisation AD lorsqu'on prennait en compte la casse	"
   "[GOFAST-8820]","Correction d'un problème rare de tri des membres d'un espace par rôle 	"
   "[GOFAST-7598]","Correction d'une erreur affichant L'article est supprimé, vous ne pouvez pas afficher ces informations sur certains wikis	"
   "[GOFAST-9021]","Correction d'une limitation d'affichage avec un zoom à 110% empéchant de lancer une tache	"
   "[GOFAST-9197]","Correction d'une regression empéchant de faire un partage par email à tous les membres d'un espace	"
   "[GOFAST-8934]","Correction dans notification d'adhésion à un espace d'un doublement d'utilisateur	"
   "[GOFAST-9012]","Correction de l'affichage du menu de 2ème niveau lors d'une prévisualisation pleine page	"
   "[GOFAST-8098]","Correction de la longueur maximale du chemin limité par Windows pour ne plus prendre en compte l'encodage	"
   "[GOFAST-9112]","Correction de la perte de certaines fonctionnalités de l'éditeur riche Wiki	"
   "[GOFAST-8786]","Correction de la possibilité d'édition d'une carte Kanban supprimée au même moment par un autre utilisateur	"
   "[GOFAST-7727]","Correction de problèmes aléatoires lors de la publication	"
   "[GOFAST-8199]","Correction du cloisonnement du carnet d'adresse (en mode cloisonné)	"
   "[GOFAST-9034]","Correction du dédoublement dans certains cas des cartes Kanban et colonnes 	"
   "[GOFAST-8936]","Correction en Onlyoffice 7.1.2 d'une perte de cellule dans les formats ODS (opendocument)	"
   "[GOFAST-6813]","Correction par JITSI d'un bug empechant de sélectionner la source pour le micro	"
   "[GOFAST-8568]","DUA : impossible de mettre l'état Pré-archivé sur un document dont la catégorie a une DUA qui dépasse l'an 2038	"
   "[GOFAST-7178]","Correction d'un bug où la suppression de commentaires n'était pas l'audit	"
   "[GOFAST-8966]","Parfois mauvais menu d'action contextuel sur un document de l'explorateur de fichier	"
   "[GOFAST-8696]","Parfois, non enregistrement des liens vers documents depuis une carte Kanban	"
   "[GOFAST-7628]","Perte de formatage HTML des tableaux dans les wiki	"
   "[GOFAST-7883]","Correction d'un bug ne restreignant pas la visibilité des listes d'utilisateurs en mode cloisonnée	"
   "[GOFAST-8846]","Correction d'un bug de suppression intempestive de document dans certains cas de multi-emplacement	"
   "[GOFAST-8861]","Correction d'un bug faisant qu'on recevait les invitations de réunion en Français alors que l'utilisateur avait une autre langue par défaut "
     

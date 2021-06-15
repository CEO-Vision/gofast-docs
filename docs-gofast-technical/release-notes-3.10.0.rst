********************************************
GoFAST :  Version 3.10.0
********************************************

**[GoFAST Enterprise]** N’hésitez pas à solliciter notre support pour planifier la mise à jour (https://srv01.ceo-vision.com/osticket/index.php).


Nouvelles fonctionnalités 
*****************************
.. csv-table::
   :header: "Ref.", "Description"
   :widths: 10, 40   

   "[	GOFAST-7005 	]", "	Nouvelle option pour la prévisualisation de fichiers Excel : utilisation de la Suite OnlyOffice en lecture seule (voir 'configuration' de la plateforme, menu 'document') 	"
   "[	GOFAST-6932 	]", "	Nouvelle interface 'GoFAST Essentiel' : une interface adaptée pour les utilisateurs occasionnels "
   "[	GOFAST-6909 	]", "	Le 'super-administrateur' a la possibilité de pré-ajouter des membres dans les Espaces, avec demande de validation auprès des administrateurs métiers de ces Espaces	"
   "[	GOFAST-7092 	]", "	Fonctionnalités liées au champs 'importance' pour les documents dits 'Contenu Confidentiel' : impossible de télécharger, imprimer, partager avec l'extérieur	"
   "[	GOFAST-7034 	]", "	Workflow standard : option pour créer automatiquement la publication PDF d'un document travail avant l'étape de validation ou de signature	"
   "[	GOFAST-6925 	]", "	Evolution du module optionnel de signature via i-Parapheur (Pastell - Libriciel) : pouvoir envoyer le document au parapheur depuis un formulaire de workflow	"
   "[	GOFAST-6922 	]", "	Modèles de Workflows : Pouvoir créer/éditer des modèles de workflows (acteurs, type d'assignations, etc.) pour pouvoir lancer des processus prédéterminés 	"
   "[	GOFAST-6919 	]", "	Améliorations du Workflow standard : validation et signature séquentielle appliquées par défaut avec message explicatif	"


Améliorations 
******************************
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40

   "[	GOFAST-7095 	]", "	Amélioration du Workflow standard : ajout de la prévisualisation du document directement dans le formulaire 	"
   "[	GOFAST-7084 	]", "	Formulaire de création d'un document : empêcher de cliquer sur les 'Espaces racines' lors de la sélection d'emplacement(s) (rappel : il interdit de créer un document 'à la racine')	"
   "[	GOFAST-7063 	]", "	Etendre la restriction des droits 'Lecture Seule' d'un Espace au salon de discussion associé, empêchant d'y poster des messages	"
   "[	GOFAST-7058 	]", "	Mise à jour d'Ajax Library v5.20.5641	"
   "[	GOFAST-7017 	]", "	Workflow : ajout de l'option permettant de revenir à l'étape précédente dans le cas d'un rejeter de validation ou de signature 	"
   "[	GOFAST-7002 	]", "	Protéger la création des webconférences : le lien vers une webconférence ne peut être créé que depuis le formulaire de création d'une réunion	"
   "[	GOFAST-6974 	]", "	Bloc de gauche 'Explorateur de fichiers' sur 'GoFAST Mobile' : mise en évidence du document sur lequel on se trouve 	"
   "[	GOFAST-6959 	]", "	Mise à jour de Jitsi v2.0.5765 : nouvelle ergonomie 	"
   "[	GOFAST-6958 	]", "	Mise à jour de OnlyOffice 6.3 : nouvelles fonctionnalités et évolutions ergonomiques (consulter la release note OnlyOffice) 	"
   "[	GOFAST-6599 	]", "	Dans le cas d'une authentification via SSO : ne pas afficher les deux champs 'identifiant' et 'mot-de-passe' (uniquement le bouton 'se connecter en SSO' et le choix entre GoFAST 'Basic' ou 'Compète' 	"
   "[	GOFAST-6994 	]", "	Performances webconférence : utilisation de WebSocket pour Jicofo	"
   "[	GOFAST-6993 	]", "	Performances webconférence : adaptation du niveau de mémoire alloué à la webconférence en fonction de la mémoire disponible	"
   "[	GOFAST-7036 	]", "	Positionner l'utilisateur au niveau du commentaire généré par une annotation qui vient d'être faite	"

Sécurité
**********
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40
   
   "[	GOFAST-7069 	]", "	Mise à jour de nettle 2.7.1-9	"
   "[	GOFAST-7022	]", "	Mise à jour de wpa_supplicant CentOS 2.6-12.el7_9.2	"
   "[	GOFAST-7021 	]", "	Mise à jour de Kernel CentOS 3.10	"
   "[	GOFAST-7090 	]", "	Cacher le fichier web.config	"
   "[	GOFAST-7055 	]", "	Mise à jour de Kernel CentOS kernel-3.10.0-1160.24.1.el7.	"
   "[	GOFAST-6937 	]", "	Analyse ClamAV des nouveaux fichiers ou versions	"
   "[	GOFAST-6945 	]", "	Correction de la faille XSS dans les champs éditables CKEditor	"


Bugs
**********
.. csv-table::  
   :header: "Ref.", "Description"
   :widths: 10, 40
   
   "[	GOFAST-7059 	]", "	Permettre sur MacOS la fonctionnalité 'éditer depuis PC' pour les fichiers PDF [MacOS BIGSUR][SAFARI] 	"
   "[	GOFAST-7111	]", "	Correction d'erreur liée au multi-emplacement (partage dans plusieurs Espaces) d'un forum et d'un formulaire	"
   "[	GOFAST-7086 	]", "	Afficher le bouton 'sauvegarder sur GoFAST' depuis la Suite OnlyOffice	"
   "[	GOFAST-7073 	]", "	Après ajout/création d'un document dans un dossier 'Template', ajouter automatiquement l'étiquette 'Template' sur ce document	"
   "[	GOFAST-7072 	]", "	Ajouter le champs 'référence documentaire' à la recherche et dans les filtres d'un résultat de recherche 	"
   "[	GOFAST-6947 	]", "	Correction d'une erreur limitant la prévisualisation et l'édition via OnlyOffice aux 25 premières pages dans certains cas	"
   "[	GOFAST-7134 	]", "	Affichage des annotations dans l'aperçu et dans le commentaire associé : séparation entre le texte annoté et l'annotation faite 	"
   "[	GOFAST-5461 	]", "	Correction d'une erreur limitant la prévisualisation des fichiers tableurs (aperçu PDF sur page du document) au seul premier onglet du fichier	"
   "[	GOFAST-6016 	]", "	Correction du 'glissé-déposé' d'une nouvelle version d'un fichier (page d'un document) lors que le temps de chargement est lent	"
   "[	GOFAST-5456 	]", "	Correction des liens internes et externes sur une prévisualisation gérée par OnlyOffice	"




**Bonne utilisation de GoFAST !**






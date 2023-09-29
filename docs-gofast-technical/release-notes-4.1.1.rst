********************************************
GoFAST :  Version 4.1.1
********************************************

**[GoFAST Enterprise]** N’hésitez pas à solliciter notre support pour planifier la mise à jour.


Nouvelles fonctionnalités 
*****************************

.. csv-table::
   :header: "Ref.", "Description"
   :widths: 1000, 60000
   
   "GOFAST-10051","Nouvelle fonctionnalité : Mise en place d'une alerte de supervision en cas d'échec d'authentification"
   "GOFAST-9221","Ajouter d'un connecteur eIDAS Signature Qualifiée (DigitalSign)"
   "GOFAST-7838","Amélioration visant à autoriser l'envoi des traces techniques anonymes "
   "GOFAST-7254","Nouvelle fonctionnalité Jitsi Meet : Tableau blanc interactif "
  
Améliorations 
******************************

**Améliorations Fonctionnelles & Techniques**

.. csv-table::
   :header: "Ref.", "Description"
   :widths: 1000, 60000

   "GOFAST-10640","Amélioration : ajout de la supervision du composant ""TURN"""
   "GOFAST-10489","[ESSENTIAL] Ajout de l'icone de panier documentaire"
   "GOFAST-10412","Amélioration des processus de compression et décompression"
   "GOFAST-10411","Amélioration empêchant de demander à rejoindre un espace public dans annuaire espace"
   "GOFAST-10403","Amélioration en ajoutant de nouveaux types de champs dans les métadonnées spécifiques"
   "GOFAST-10261","Amélioration : Un message explicatif est affiché lorsque le fil d'activité est vide en raison de l'inactivité"
   "GOFAST-10214","Amélioration visant à interdire l'utilisation du slash ""/"" dans le moteur de recherche ; un message d'erreur s'affiche si vous essayez de les utiliser."
   "GOFAST-10179","Amélioration : Une info-bulle est désormais disponible lorsque vous survolez les ""lien en provenance"""
   "GOFAST-10175","Amélioration permettant de vider un champ lors d""une sélection (Importance, Catégorie, ..)"
   "GOFAST-10128","Amélioration de l'algorithme d'autocomplétion des documents (lien entre documents, ...)"
   "GOFAST-10122","Ajout d'une animation d'attente au chargement initial d'une page"
   "GOFAST-10086","Amélioration permettant de mettre des liens externes en http (en plus de https)"
   "GOFAST-9969","Amélioration générale des traductions sur GoFAST 4.1.1"
   "GOFAST-9758","Mise à jour de Jitsi Meet v1.0.7322"
   "GOFAST-9680","Amélioration : Position des en-têtes de colonne, sur la page ""membre"" d'un espace en 1440x900"
   "GOFAST-9577","[IPAD] N'autoriser que le mode paysage sauf sur la page d'un document"
   "GOFAST-9506","Amélioration : Mise à jour d'Onlyoffice v7.4.1"
   "GOFAST-8831","Ajout d'un bouton ""annuler"" dans la fenêtre de création de contenu (doc, réunion ...)"
   "GOFAST-7744","Amélioration : Sur la refonte du bloc de métadonnées spécifiques"
   "GOFAST-10279","Remplacement de COTURN par Pion TURN"
   "GOFAST-10338","Mise à jour Alfresco 7.4"




Bugs 
******************************
.. csv-table::
   :header: "Ref.", "Description"
   :widths: 1000, 60000
      
   "GOFAST-9927","Correction du problème de chargement superflu des onglets (calendrier, tâches et membres)"
   "GOFAST-9898","Annuaires : tri par défaut des éléments par ordre alphabétique (colonne 'nom') "
   "GOFAST-9862","Correction d'un problème de fiabilisation des répertoires miroir  "
   "GOFAST-9722","MàJ Synapse et utilisation plus récente version et suppression ancienne"
   "GOFAST-10650","[ESSENTIAL] Correction d'un bug, au clic sur l'onglet ""Info"" d'un document, navigation vers l'explorateur de fichier"
   "GOFAST-10645","Correction d'un bug de problème d'affichage de l'onglet tâches "
   "GOFAST-10614","Correction d'un bug, ""Erreur réseau"" affiché lors de la création d'un document depuis un modèle en format otp"
   "GOFAST-10613","Correction d'un bug, lors de la décompression des fichiers, admin est automatiquement rempli en tant qu'auteur et créateur des documents"
   "GOFAST-10587","Correction d'un bug d'affichage pour certains membres dans un espace qui n'y ont pas accès"
   "GOFAST-10578","Correction d'un bug concernant la redirection des liens des dossiers ajoutés lors de la création d'une réunion."
   "GOFAST-10575","Correction d'un bug de l'API pour l'ajout de membres (liste utilisateurs) à des espaces entrainant des erreurs"
   "GOFAST-10567","Correction d'un bug concernant un problème d'alignement de signature YouSign  "
   "GOFAST-10461","[ESSENTIAL]  Correction d'un bug de l'arborescence qui ne se déplie pas correctement après navigation "
   "GOFAST-10459","Correction d'un bug de disparition du modèle de dossier"
   "GOFAST-10457","Correction d'un bug empéchant le filtrage dans les modèles de contenus"
   "GOFAST-10455","Correction d'un bug depuis l'édition d'un PC avec LibreOffice ou Office, une fois le document fermé le verrou ne s'enlève pas et indique une erreur d'enregistrement"
   "GOFAST-10449","Correction d'un bug entrainant un ajout de fichier impossible sur les webforms  / formulaires"
   "GOFAST-10447","Correction d'un bug, le navigateur de fichier permettait dans certains cas de glisser déposer des documents dans le dossier wikis  "
   "GOFAST-10425","[ESSENTIAL] Correction d'un bug qui rend impossible de faire une recherche depuis une page erreur 404/403"
   "GOFAST-10417","[ESSENTIAL] Correction d'un bug rendant impossible l'accès à la page de recherche depuis le formulaire d'édition d'un wiki"
   "GOFAST-10415","[ESSENTIAL] Correction d'un bug, l'écran de chargement ne s'enlève pas sur la page de recherche "
   "GOFAST-10410","[ESSENTIAL] Correction d'un bug de page grise après un retour via le navigateur "
   "GOFAST-10397","Correction d'un bug d'affichage lors de l'édition d'une page d'accueil via l'arborescence des wikis"
   "GOFAST-10385","Correction d'un bug lors du lancement d'une communication vocale dans Element qui demandait un mot de passe non paramétré par l'utilisateur"
   "GOFAST-10352","Correction d'un bug lors de la réception de la notification pour rejoindre un espace par mail, le bouton rejoindre était vide "
   "GOFAST-10350","Correction d'un bug empêchant la fonctionnalité ""glisser déposer"" de fonctionner en cas de timeout"
   "GOFAST-10318","Correction d'un bug lors du téléchargement de fichiers en masse dans l'explorateur de fichier"
   "GOFAST-10313","Correction d'un bug de lenteur de l'onglet tâches"
   "GOFAST-10308","Correction d'un bug, impossibilité de vider un assigné à une tâche de ToDo List Kanban"
   "GOFAST-10301","Correction d'un bug qui effectuait une synchronisation des utilisateurs et des listes d'utilisateurs même lorsque l'annuaire distant était injoignable."
   "GOFAST-10265","Correction d'un bug, non affichage des info-bulles sur l'onglet ""membres"""
   "GOFAST-10257","Correction d'un bug pour le formulaire de configuration lié à la visibilité, qui ne sauvegarde pas les modifications "
   "GOFAST-10255","[ESSENTIAL] Correction d'un bug lors du changement de langue d'un document non visible immédiatement"
   "GOFAST-10224","Correction d'un bug pour le module API webhook si un document est déjà existant"
   "GOFAST-10222","Correction de plusieurs bugs résolvant des problèmes sur ""Contacter les administrateurs"""
   "GOFAST-10219","Correction d'un bug aléatoire empéchant l'affichage du fil d'ariane "
   "GOFAST-10215","Correction d'un bug qui affichait les contenus non prévisualisables sous forme binaire"
   "GOFAST-10199","[ESENTIAL] Correction d'un bug de non-chargement sporatique de la page d'accueil "
   "GOFAST-10194","Correction d'un bug, qui empêchait la création/suppression des colonnes dans le tableau kanban dans tâches"
   "GOFAST-10168","[ESSENTIAL] Correction d'un bug, incohérence entre l'emplacement de l'explorateur et le chemin affiché "
   "GOFAST-10162","Correction d'un bug créant un problème de création de publication pdf lorsqu'elle est multifilée/partagée dans des espaces personnels"
   "GOFAST-10139","Correction d'un bug, le menu ""plus"" du menu contextuel d'un document s'ouvre du mauvais côté"
   "GOFAST-10138","Correction d'un bug qui empêchait d'afficher le fil d'ariane sur une ligne"
   "GOFAST-10137","Amelioration performance du changement de métadonnées"
   "GOFAST-10101","[IPAD] Correction d'un bug empêchant de charger un fichier local"
   "GOFAST-10077","[ESSENTIAL] Correction d'un bug bloquant sur les webforms "
   "GOFAST-10063","Correction d'un bug d'appels Afresco ne se terminant jamais"
   "GOFAST-10061","Correctif d'un bug : problème de déclaration de l'aspect gofastMail depuis la dernière version d'Alfresco"
   "GOFAST-10033","Correction d'un bug empêchant le fonctionnement d'Element  avec un login numérique"
   "GOFAST-10023","Correction d'un bug rendant l'onglet ""Versions"" vide sur certains documents"
   "GOFAST-10019","[ESSENTIAL]  Correction de bugs concernant plusieurs effets visuels indésirables dans tâches"
   "GOFAST-9972","Correction d'un bug sur la piste d'audit qui affichait la mise à jour des métadonnées comme une consultation de document "
   "GOFAST-9953","Correction d'un bug, lors de l'édition d'un commentaire, cette modification n'était pas vue par un autre utilisateur qui était sur cette même page"
   "GOFAST-9932","Correction d'un bug, lors de l'ajout d'un commentaire on passe sur l'onglet ""Taches"" plutôt que de rester sur ""Commentaires"""
   "GOFAST-9906","Correction d'un bug, ""Modifier description de l'espace"" qui ne fonctionnait pas si on était situé dans un espace racine"
   "GOFAST-9881","Correction d'un bug, dans un commentaire les smiley ne s'affichaient pas correctement"
   "GOFAST-9751","Correction d'un bug de transformation en PDF non fonctionnel "
   "GOFAST-9750","Correction d'un bug de filtre de recherche avec des métadonnées spécifiques"
   "GOFAST-9747","Correction d'un bug où il n'était pas possible d'enregistrer une webconférence sur Jitsi "
   "GOFAST-9604","[PLUS] Correction d'un bug rendant impossible le lancement de la réindexation complète"
   "GOFAST-9600","[PLUS] Correction d'un bug pour le fonctionnement de la configuration documentaire "
   "GOFAST-9590","[MOBILE] Correction d'un bug entrainant des problèmes d'annotation"
   "GOFAST-9562","[PLUS] Correction d'un bug : l'info-bulle peut être cachée par le menu contextuel"
   "GOFAST-9441","Correction d'un bug causant un mauvais affichage lors du mirroring dans un espace personnel  "
   "GOFAST-9432","Correction d'un bug de mauvaise redirection de lien si REFERER"
   "GOFAST-9419","Correction d'un bug qui supprimait des arborescences depuis l'explorateur de fichier, ce qui posait des problèmes de performance"
   "GOFAST-9396","Correction d'un bug n'affichant plus le nom de la plateforme dans le pied de page des notifications"
   "GOFAST-9330","Correction d'un bug faisant qu'un utilisateur Support-Métier ne peut pas appliquer ce profil à un autre utilisateur"
   "GOFAST-9291","Correction d'un bug qui entrainait la juxtaposition de deux signatures (YouSign et DigitalSign)"
   "GOFAST-8975","Correction d'un bug concernant la pertinence de l'indexation des espaces "
   "GOFAST-8970","Correction d'un problème qui coupait les appels one to one Element, selon les configurations réseaux"
   "GOFAST-8721","Correction d'un problème qui déconnectait la session JITSI si port 10000 fermé"
   "GOFAST-8594","Correction d'un bug empêchant de voir les modèles de documents sur les nouvelles installations"
   "GOFAST-8280","Correction d'un bug qui empêchait d'ajouter des documents comme étant des traductions"
   "GOFAST-7423","Correction d'un bug qui permettait de se créer un compte local sur l'application Element "
   "GOFAST-3381","Correction d'un bug créant un dossier template dans l'espace racine lors de la création de nouveaux espaces"


Sécurité 
******************************
**[GoFAST Enterprise]** Contactez-nous pour obtenir la liste des correctifs sécurité  
  
     

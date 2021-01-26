GoFAST : Modules complémentaires
============================

Introduction
------------
Ce document a pour but de vous fournir une documentation sur l'utilisation des modules complémentaires que propose CEO-Vision.

Couplage GoFAST-Pastell (signature)
-----------------------------------

A la demande général, nous avons créér un couplage Pastell GoFAST pour la gestion de la signature éléctronique.
Voici comment l'utiliser:

**Configuration**

Dans l'image ci-dessous, vous pouvez voir la configuration de votre Pastell dans GoFAST (il necessite un identifiant, un mot de passe, et enfin l'URL de votre Pastell)



**Utilisation**

Lorsque vous arrivez sur un document PDF, il est possible d'envoyer le document à Pastell pour signature via le menu contextuel du document:



Vous arrivez alors sur cette modale là:



Vous devez alors choisir l'entité à laquelle vous appartenez:



Puis le processus que vous decidez d'utiliser (cela depend de la configuration de votre Pastell):



Vous pouvez maintenant envoyer à Pastell le document pour signature en cliquant sur le bouton envoyer

Le document est alors "verrouillé" (métadonnées non modifiable).

L'etat du document coté Pastell est ecrit sous forme de "Message" quand nous allons sur le document:



Une fois le processus de signature est terminé (Approuvé ou refusé), un commentaire est créé avec les differentes étapes et leurs informations:


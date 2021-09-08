***********************************
Deploiement Certificats GoFAST :
***********************************

Wildcards :
=============

MAIN :

déposez le dossier contenant les certificats dans /opt

- copiez le certificat vers /etc/pki/tls/certs/localhost.crt 
- copiez la clef vers /etc/pki/tls/private/localhost.key 
- copiez le server-chain vers /etc/pki/tls/certs/server-chain.crt 


  
COMM :

- copiez le certificat vers /etc/pki/tls/certs/localhost.crt 
- copiez la clef vers /etc/pki/tls/private/localhost.key 
- 
 .. code-block::

  cat /etc/pki/tls/certs/gofast.crt /etc/pki/tls/private/gofast.key > /etc/pki/tls/certs/gofast.pem

Tester les services (coo-édition, cadena coo-édition, visio, chat), corriger si ceux-ci ne fonctionnent plus.


Correctifs à faire (si mauvais fonctionnement des services) :
========================================================================

Problème connexion non automatique au chat Element (COMM):
------------------------------------------------------------

Commandes à exécuter sur la plateforme COMM (en ssh) pour corriger le problème de connexion non automatique au chat.

.. code-block::

  cd /opt/gofast-comm
  echo "Enter GoFAST MAIN URL (ex: gofast.ceo-vision.com):"
  read url_main
  java InstallCert $url_main
  cp jssecacerts /etc/pki/ca-trust/extracted/java/cacerts
  systemctl restart ma1sd

Problème Cadenas OnlyOffice (MAIN):
-------------------------------------

Commandes à exécuter sur la plateforme MAIN (en ssh) pour corriger le problème de cadenas qui reste fermé à la sortie d'une coédition OnlyOffice.

.. code-block::

  cd /opt
  echo "Enter GoFAST COMM URL (ex: gofast-comm.ceo-vision.com):"
  read url_comm
  java InstallCert $url_comm
  cp jssecacerts /etc/pki/ca-trust/extracted/java/cacerts
  echo "Warning la GED va redémarrer"
  sleep 2
  systemctl restart tomcat@alfresco

Problème Certificats Visio (COMM):
-------------------------------------

Commandes à exécuter sur la plateforme COMM (en ssh) pour corriger le problème de visio-conférence à trois minimum impossible.

.. code-block::

  server_name=`grep -oP "(?<=domain: \').+?(?=\')" /etc/ma1sd/ma1sd.yaml`

  echo "secret_key = mot de passe dans /etc/jitsi/jicofo/config "

  read secret_key

  rm -Rf /var/lib/prosody/*
  cd /opt/gofast-comm/update

  systemctl stop crond
  prosodyctl stop
  systemctl stop jibri
  systemctl stop jitsi-videobridge
  systemctl stop jicofo

  #Generate certificates

  prosodyctl cert generate auth.${server_name}

  echo "
  #################################################
  ## Entrez les informations suivantes
  4096
  FR
  COMM
  GOFAST
  XMPP
  auth.${server_name}

  xmpp@auth.${server_name}
  #################################################"


  mv /var/lib/prosody/auth.$server_name.crt  /var/lib/prosody/auth.crt
  mv /var/lib/prosody/auth.$server_name.key  /var/lib/prosody/auth.key
  mv /var/lib/prosody/auth.$server_name.cnf  /var/lib/prosody/auth.cnf

  ln -sf /var/lib/prosody/auth.crt /etc/pki/ca-trust/source/anchors/auth.crt

  update-ca-trust extract -f

  prosodyctl start

  prosodyctl register videobridge auth.$server_name $secret_key
  prosodyctl register jibri auth.$server_name $secret_key
  prosodyctl register recorder recorder.$server_name $secret_key
  prosodyctl register focus auth.$server_name $secret_key
  prosodyctl mod_roster_command subscribe focus.$server_name focus@auth.$server_name

  systemctl start jibri
  systemctl start jitsi-videobridge
  sleep 3
  systemctl start jicofo
  systemctl start crond
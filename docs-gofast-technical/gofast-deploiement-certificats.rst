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


Let's Encrypt :
==================



Installation du paquet pour la génération des certificats (à faire sur les deux machines) :

.. code-block::

  yum install -y certbot


MAIN :

Stop du service HTTPD + ouverture port 80 firewalld

.. code-block::

  systemctl stop httpd
  firewall-cmd --permanent --add-port=80/tcp → ouverture
  firewall-cmd --reload → reload

Test génération certificats (changer l'URL de la plateforme) :

.. code-block::

  read url_main
  read url_mobile

  certbot certonly --non-interactive --email support@ceo-vision.fr \
  --preferred-challenges http --standalone --agree-tos --renew-by-default \
  --webroot-path  /var/www/html -d $url_main --dry-run

    certbot certonly --non-interactive --email support@ceo-vision.fr \
  --preferred-challenges http --standalone --agree-tos --renew-by-default \
  --webroot-path  /var/www/html -d $url_mobile --dry-run

Si ce test réussi, vous pouvez alors éxécuter ce code :

.. code-block::

  read url_main
  read url_mobile

  certbot certonly --non-interactive --email support@ceo-vision.fr \
  --preferred-challenges http --standalone --agree-tos --renew-by-default \
  --webroot-path  /var/www/html -d $url_main

  certbot certonly --non-interactive --email support@ceo-vision.fr \
  --preferred-challenges http --standalone --agree-tos --renew-by-default \
  --webroot-path  /var/www/html -d $url_mobile --dry-run


Copie des certificats aux bons emplacements :

.. code-block::

  read url_main
  read url_mobile

  cp /etc/letsencrypt/live/$url_main/privkey.pem /etc/pki/tls/private/localhost.key
  cp /etc/letsencrypt/live/$url_main/cert.pem /etc/pki/tls/certs/localhost.crt 
  cp /etc/letsencrypt/live/$url_main/fullchain.pem /etc/pki/tls/certs/server-chain.crt 

  cp /etc/letsencrypt/live/$url_mobile/privkey.pem /etc/pki/tls/private/localhost_mobile.key
  cp /etc/letsencrypt/live/$url_mobile/cert.pem /etc/pki/tls/certs/localhost_mobile.crt

  firewall-cmd --permanent --remove-port=80/tcp → ouverture
  firewall-cmd --reload → reload

  systemctl start httpd

COMM :

Stop service coturn :

.. code-block::

  systemctl stop coturn


Test génération certificats (changer l'URL de la plateforme) :

.. code-block::

  read url_comm
  mkdir /var/www/html

  certbot certonly --non-interactive --email support@ceo-vision.fr \
  --preferred-challenges http --standalone --agree-tos --renew-by-default \
  --webroot-path  /var/www/html -d $url_comm --dry-run


Si ce test réussi, vous pouvez alors éxécuter ce code :

.. code-block::

  read url_comm
  mkdir /var/www/html

  certbot certonly --non-interactive --email support@ceo-vision.fr \
  --preferred-challenges http --standalone --agree-tos --renew-by-default \
  --webroot-path  /var/www/html -d $url_comm


Copie des certificats aux bons emplacements :

.. code-block::

  read url_comm

  cp /etc/letsencrypt/live/$url_comm/privkey.pem /etc/pki/tls/private/gofast.key
	cp /etc/letsencrypt/live/$url_comm/cert.pem /etc/pki/tls/certs/gofast.crt

	cat /etc/pki/tls/certs/gofast.crt /etc/pki/tls/private/gofast.key > /etc/pki/tls/certs/gofast.pem

  systemctl restart nginx
  sleep 2
  systemctl stat coturn

Tester les services (coo-édition, cadena coo-édition, visio, chat), corriger si ceux-ci ne fonctionnent plus.

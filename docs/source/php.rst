Installing PHP-8.1
=====================================

**Reset PHP**
--------
.. code-block:: console

    dnf module reset php
.. image:: images/php-reset.JPG
    
**Install PHP-8.1**  
-------------
.. code-block:: console

  dnf module install php:remi-8.1
.. image:: images/php-installing-1.JPG
.. image:: images/php-installing-2.JPG


**Enable CodeReady Builder REPO**
-------------
.. code-block:: console

  subscription-manager repos --enable codeready-builder-for-rhel-8-x86_64-rpms
.. image:: images/enable-codeready.JPG
 
**DNF Update**
---------------------
.. code-block:: console

  dnf update
.. image:: images/dns-update-after-php-install.JPG

**Dev Extensions**
---------------------
.. code-block:: console

  dnf install php-pdo php-pear php-devel
.. image:: images/php-pdo-pear-devel-1.JPG
.. image:: images/php-pdo-pear-devel-2.JPG
.. image:: images/php-pdo-pear-devel-2.JPG

**Check Version**
---------------------
.. code-block:: console

  php -v
.. image:: images/php-v.JPG

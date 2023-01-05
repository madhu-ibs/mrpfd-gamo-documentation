Installing Apache WebServer (HTTPD)
=====================================

**Install httpd**
--------
.. code-block:: console

    sudo yum install httpd
.. image:: images/httpd-install.JPG
    
SELinux is installed by default and runs in Enforcing mode. To allow Apache to connect to databases through SELinux, run the following command

.. code-block:: console
   
   sudo setsebool -P httpd_can_network_connect_db 1
   
Restart Apache and test the sample script

.. code-block:: console
   
   sudo apachectl restart
   
**Default RHEL Sample Site**
--------
Visit http://localhost or http://127.0.0.1 to view default httpd server sample site

.. image:: images/default-site-httpd.JPG

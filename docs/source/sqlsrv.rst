Installing PHP-SQLSRV
=====================================

**Prerequisites to install SQLSRV**
-------------------
Add MSSQL REPO
.. code-block:: console

    curl https://packages.microsoft.com/config/rhel/8/prod.repo > /etc/yum.repos.d/mssql-release.repo
.. image:: images/mssql-repo.JPG

Remove Other UNIX ODBCS to avoid conflicts
.. code-block:: console

    curl https://packages.microsoft.com/config/rhel/8/prod.repo > /etc/yum.repos.d/mssql-release.repo
.. image:: images/unixodbc-old-remove.JPG

Install MSODBC18 and MSODBC18 Tools

.. code-block:: console

    sudo ACCEPT_EULA=Y yum install -y msodbcsql18
    
.. code-block:: console
    sudo ACCEPT_EULA=Y yum install -y mssql-tools18
    
.. image:: images/msodbc-install-1.JPG
.. image:: images/msodbc-install-2.JPG

**Entension SQLSRV**
--------
.. code-block:: console

    sudo pecl install sqlsrv
.. image:: images/php-sqlsrv.JPG
    
**Entension PDO-SQLSRV**
--------
.. code-block:: console

    sudo pecl install pdo_sqlsrv
.. image:: images/php-pdo-sqlsrv.JPG

**Login to Sudo**
--------
.. code-block:: console

    sudo su

**Make PDO-SQLSRV SO**
-------------
.. code-block:: console

  echo extension=pdo_sqlsrv.so >> `php --ini | grep "Scan for additional .ini files" | sed -e "s|.*:\s*||"`/30-pdo_sqlsrv.ini
.. image:: images/make-sqlsrv.JPG
 
**Make SQLSRV SO**
-------------
.. code-block:: console

  echo extension=sqlsrv.so >> `php --ini | grep "Scan for additional .ini files" | sed -e "s|.*:\s*||"`/20-sqlsrv.ini
.. image:: images/make-sqlsrv.JPG

**Exit to check PHP version and modules**

.. code-block:: console

  exit

**Check Version**
---------------------
.. code-block:: console

  php -v
  
.. code-block:: console

  php -m
.. image:: images/php-m.JPG

Check Command: check_win_users
==============================

Check the count of users on a Windows server based on a query.

Valid Query Options
-------------------

-  AccountType
-  Caption
-  Description
-  Disabled
-  Domain
-  FullName
-  InstallDate
-  LocalAccount
-  Lockout
-  Name
-  PasswordChangeable
-  PasswordExpires
-  PasswordRequired
-  SID
-  SIDType
-  Status

Example Queries
---------------

-  List all users:

.. code-block:: console

   status like '%'

-  Show users where the Status is OK:

.. code-block:: console

   status='OK'

-  Show usernames that contains the string “EX”:

.. code-block:: console

   name like '%EX%'

-  Show usernames that start with the string “Admin”:

.. code-block:: console

   name like 'Admin%'

-  Show usernames that end with the string “test”:

.. code-block:: console

   name like '%test'

-  Show users whose full name contains the String “Exchange”:

.. code-block:: console

   fullname like '%Exchange%'

-  Show users that belong to the Domain called “TEST”:

.. code-block:: console

   Domain='TEST'

-  Show users where a password is not required:

.. code-block:: console

   PasswordRequired!='True'

-  Show users that belong to the Domain called “TEST” and that where a
   password is not required:

.. code-block:: console

   PasswordRequired!='True' AND Domain='TEST'

-  Show users that do not belong to the Domain called “TEST”:

.. code-block:: console

   Domain!='TEST'

-  Show users that have local accounts:

.. code-block:: console

   LocalAccount='True'
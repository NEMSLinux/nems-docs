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

   status like '%'

-  Show users where the Status is OK:

   status='OK'

-  Show usernames that contains the string “EX”:

   name like '%EX%'

-  Show usernames that start with the string “Admin”:

   name like 'Admin%'

-  Show usernames that end with the string “test”:

   name like '%test'

-  Show users whose full name contains the String “Exchange”:

   fullname like '%Exchange%'

-  Show users that belong to the Domain called “TEST”:

   Domain='TEST'

-  Show users where a password is not required:

   PasswordRequired!='True'

-  Show users that belong to the Domain called “TEST” and that where a
   password is not required:

   PasswordRequired!='True' AND Domain='TEST'

-  Show users that do not belong to the Domain called “TEST”:

   Domain!='TEST'

-  Show users that have local accounts:

   LocalAccount='True'
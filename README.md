django-ldap-basic-auth
======================

Simple middleware that injects the Authorization header in the request after authenticating against a ldap server

If you use BasicAuthentication in production you must ensure that your API is only available over https. You should also ensure that your API clients will always re-request the username and password at login, and will never store those details to persistent storage.

Installation
===============
You can install django-ldap-basic-auth in 2 ways: using pip or by setup.py install

.. code-block:: bash

    $ pip install django-ldap-basic-auth


Then modify your settings.py

.. code-block:: bash

    INSTALLED_APPS = INSTALLED_APPS + (
        'django_ldap_basic_auth',
    )

    AUTHENTICATION_BACKENDS = ('django_ldap_basic_auth.backends.LdapBasicAuthBackend',) + AUTHENTICATION_BACKENDS

    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
        'django_ldap_basic_auth.middleware.InjectBasicAuthMiddleware',
    )

	DJANGO_LDAP_BASIC_AUTH_ACTIVATED = True



Dependencies
============

* Django >= 1.4.x
* django-auth-ldap installed


TODO
====

* Improve tests
* Check if django-auth-ldap is installed

CHANGELOG
=========
* 0.0.1
	* first version

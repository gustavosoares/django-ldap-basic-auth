django-ldap-basic-auth
======================

Simple middleware that injects the Authorization header in the request after authenticating against a ldap server

If you use BasicAuthentication in production you must ensure that your API is only available over https. You should also ensure that your API clients will always re-request the username and password at login, and will never store those details to persistent storage.

Installation
===============
You can install django-ldap-basic-auth in 2 ways: using pip or by setup.py install


    $ pip install django-ldap-basic-auth


Then modify your settings.py


    INSTALLED_APPS = INSTALLED_APPS + (
        'django_ldap_basic_auth',
    )

    AUTHENTICATION_BACKENDS = ('django_ldap_basic_auth.backends.LdapBasicAuthBackend',) + AUTHENTICATION_BACKENDS

    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
        'django_ldap_basic_auth.middleware.InjectBasicAuthMiddleware',
    )

    DJANGO_LDAP_BASIC_AUTH_ACTIVATED = True

If you want to store the information in a http cookie, called HTTP_AUTHORIZATION, then put in your settings.py:

    DJANGO_LDAP_BASIC_AUTH_USE_COOKIES = True

You must define a django cache backend too.

Dependencies
============

* Django >= 1.4.x
* django-auth-ldap (https://pythonhosted.org/django-auth-ldap/)


TODO
====

* Improve tests
* Check if django-auth-ldap is installed

CHANGELOG
=========
* 0.0.1
	* first version
* 0.0.2
    * including request.session.modified = True to make sure that Django will persist the session
* 0.0.3
    * use http cookie to store data

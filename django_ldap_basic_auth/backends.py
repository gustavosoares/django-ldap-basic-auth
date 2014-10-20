# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
from . import settings
from . import cache_helper
from django.core.cache import cache
from django_auth_ldap.backend import LDAPBackend
import base64

LOG = logging.getLogger(__name__)

class LdapBasicAuthBackend(LDAPBackend):

    def authenticate(self, username, password):

        user = None
        try:
            user = LDAPBackend.authenticate(self, username, password)
        except Exception, e:
            LOG.exception(e)

        if settings.DJANGO_LDAP_BASIC_AUTH_ACTIVATED and user:

            base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
            cache_key = cache_helper.get_cache_key_for_instance(user)
            cache.set(cache_key, "Basic %s" % base64string, cache_helper.DEFAULT_CACHE_TIMEOUT)

        return user
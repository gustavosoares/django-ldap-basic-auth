# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging

from . import cache_helper, settings
from django.core.cache import cache

LOG = logging.getLogger(__name__)

class InjectBasicAuthMiddleware(object):
    """Middleware that gets the basic auth info and inject it in the request."""

    def process_request(self, request):

        if not request.user.is_anonymous() and request.user.is_authenticated():
            user = request.user
            cache_key = cache_helper.get_cache_key_for_instance(user)
            basic_auth = cache.get(cache_key)
            if basic_auth:
                request.session["Authorization"] = basic_auth
                request.session.modified = True
                # if use cookies is enabled, then do not remove from cache
                if not settings.DJANGO_LDAP_BASIC_AUTH_USE_COOKIES:
                    cache.delete(cache_key)

    def process_response(self, request, response):

        if settings.DJANGO_LDAP_BASIC_AUTH_USE_COOKIES and settings.DJANGO_LDAP_BASIC_AUTH_ACTIVATED:
            if not request.user.is_anonymous() and request.user.is_authenticated():
                user = request.user
                cache_key = cache_helper.get_cache_key_for_instance(user)
                basic_auth = cache.get(cache_key)
                #if basic_auth and not request.COOKIES.get('HTTP_AUTHORIZATION', None):
                if basic_auth:
                    # max_age = 365 * 24 * 60 * 60  # 10 years
                    # expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age)
                    response.set_cookie('HTTP_AUTHORIZATION', value=basic_auth, httponly=True, max_age=None, expires=None)
                    cache.delete(cache_key)

        return response



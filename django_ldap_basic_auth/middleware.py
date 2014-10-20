# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging

from . import cache_helper
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
                request.META["HTTP_AUTHORIZATION"] = basic_auth
                cache.delete(cache_key)



# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging

LOG = logging.getLogger(__name__)
DEFAULT_CACHE_TIMEOUT = 60

def get_cache_key_for_instance(instance, cache_prefix="django_ldap_basic_auth"):
    
    return "%s:%s:%s" % (cache_prefix, instance.__class__.__name__, instance.pk)
"""Settings for django-ldap_basic_auth"""
import logging
from django.conf import settings

LOG = logging.getLogger(__name__)

DJANGO_LDAP_BASIC_AUTH_ACTIVATED = getattr(settings, 'DJANGO_LDAP_BASIC_AUTH_ACTIVATED', False)
DJANGO_LDAP_BASIC_AUTH_USE_COOKIES = getattr(settings, 'DJANGO_LDAP_BASIC_AUTH_USE_COOKIES', False)

if not hasattr(settings, 'CACHES'):
    LOG.warning("no cache backend set in django! django ldap basic auth will be disabled")
    DJANGO_LDAP_BASIC_AUTH_ACTIVATED = False
import os
from setuptools import setup, find_packages

STATUS_PROD = 'Development Status :: 5 - Production/Stable'
STATUS_BETA = 'Development Status :: 4 - Beta'
STATUS_ALPHA = 'Development Status :: 3 - Alpha'

version = '0.0.2'
README = os.path.join(os.path.dirname(__file__), 'README.rst')
long_description = open(README).read()
setup(
    name='django-ldap-basic-auth',
    version=version,
    description="Simple middleware that injects the Authorization header in the request after authenticating against a ldap server.",
    long_description=long_description,
    classifiers=[
        STATUS_ALPHA,
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'],
    keywords='revisions versioning history audit',
    author='Gustavo Soares Souza',
    author_email='gustavosoares@gmail.com',
    url='https://github.com/gustavosoares/django-ldap-basic-auth',
    license='BSD',
    packages=find_packages('.', exclude=('testproject*',)),
    include_package_data=True,
)

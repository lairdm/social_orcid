from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "social_orcid: a plugin for Python Social Auth for Orcid's identity provider service."

# Long description will go up on the pypi page
long_description = """

Social OrcID
========
Social Orcid is a plugin for [Python Social Auth](https://github.com/omab/python-social-auth) to add OAuth2
support for [Orcid's](http://orcid.org) [identity provider service](https://members.orcid.org/api/oauth2).

While Python Social Auth supports multiple backends, this extension was developed specifically for
a need in Django. It may work with the other backends supported by Python Social Auth, but those
have no specifically been tested. I welcome any feedback and pull requests for improvement.

.. _README: https://github.com/lairdm/social_orcid/blob/master/README.md

License
=======
Developed by [Matthew Laird](https://github.com/lairdm/), ``social_orcid`` is protected by GPL v3 license. Check the [License](LICENSE) for details.

``python-social-auth`` and all it's components are protected by their relative
license, [please see](https://github.com/omab/python-social-auth) the individual repositories for details.

Orcid is trademarked and protected by it's usage guidelines, please consult
their [branding and guidelines](https://orcid.org/trademark-and-id-display-guidelines) page for more details.
"""

NAME = "social_orcid"
MAINTAINER = "Matthew Laird"
MAINTAINER_EMAIL = "@lairdm"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/lairdm/social_orcid"
DOWNLOAD_URL = "https://github.com/lairdm/social_orcid/archive/master.zip"
LICENSE = "GPL"
AUTHOR = "Matthew Laird"
AUTHOR_EMAIL = "@lairdm"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {}
REQUIRES = ["social"]  # python-social-auth

Social Orcid
==

About
=====

Social Orcid is a plugin for [Python Social Auth](https://github.com/omab/python-social-auth) to add OAuth2
support for [Orcid's](http://orcid.org) [identity provider service](https://members.orcid.org/api/oauth2).

While Python Social Auth supports multiple backends, this extension was developed specifically for
a need in Django. It may work with the other backends supported by Python Social Auth, but those
have no specifically been tested. I welcome any feedback and pull requests for improvement.

Installation
============

Once you have Python Social Auth installed and functioning installing this additional backend is
relatively straight forward. 

- Clone the repository and put it in the path for your app. 
- Sign up for an Orcid API key. 
- Add Social Orcid to your list of social backends

```
AUTHENTICATION_BACKENDS = (
    'social_test_app.orcid.OrcidOAuth2',
)
```

- Add the Orcid key and secret to your config.py along with your other identity providers:

```
SOCIAL_AUTH_ORCID_KEY = 'APP-XXXXXXXXXXXX'
SOCIAL_AUTH_ORCID_SECRET = '123456-abcdefg-789-xyz'
```

- Add login urls for the provider like any other provider (see templates/ for an example)

Testing Sandbox
===============

By default Social Auth points at the Orcid testing sandbox. When you're ready to go live with your app,
request access to the live authentication server and uncomment the three lines in orcid.py:

```
#    AUTHORIZATION_URL = 'https://orcid.org/oauth/authorize'
#    ACCESS_TOKEN_URL = 'https://api.orcid.org/oauth/token'
#    PROFILE_URL = 'https://pub.orcid.org/v1.2/{}/orcid-profile'
```
while commenting out the corresponding three lines pointing at the sandbox server.

Debugging
=========

SSL issues
----------

Some older versions of python are linked to an OpenSSL version that doesn't understand SNI. This can
create issues with authenticating against providers. The solution is to either upgrade to a newer
python or use pyopenssl as your OpenSSL link. Install pyopenssl and either in orcid.py or elsewhere
in your application add:

```
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()
```

need more than 1 value to unpack
--------------------------------

If you receive the error ``need more than 1 value to unpack`` during the authentication phase,
you may need to add the following to your configuration:

```
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    #'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)
```

The default pipeline name found by Python Social Auth (at least in my Django setup) is incorrectly
just my app name. After manually setting the auth pipeline things began to work. Alter the auth pipeline
to whatever components are appropriate for your setup (email authentication, etc), but the above is the
default authentication pipeline in Python Social Auth.

Limitations
===========

This library has not been extensively tested, it might be fragile and likely doesn't take advantage of all
the functionality possible through both Python Social Auth and the Orcid API. A number of the user fields
should be filled in authmatically from the API call, such as first and last name. As well a large
chunk of the profile is copied in to the exta_data field of the social auth user table which may or
may not be useful.

Dependencies
============

- [python-social-auth](https://github.com/omab/python-social-auth)
- an Orcid [API key](http://support.orcid.org/knowledgebase/articles/116739-register-a-client-application)

License
=======

Developed by [Matthew Laird](https://github.com/lairdm/), ``social_orcid`` is protected by GPL v3 license. Check the [License](LICENSE) for details.

``python-social-auth`` and all it's components are protected by their relative
license, [please see](https://github.com/omab/python-social-auth) the individual repositories for details.

Orcid is trademarked and protected by it's usage guidelines, please consult
their [branding and guidelines](https://orcid.org/trademark-and-id-display-guidelines) page for more details.

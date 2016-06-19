from social.backends.oauth import BaseOAuth2
from social.utils import handle_http_errors

class OrcidOAuth2(BaseOAuth2):
    """Orcid OAuth authentication backend"""
    name = 'orcid'
#    AUTHORIZATION_URL = 'https://orcid.org/oauth/authorize'
#    ACCESS_TOKEN_URL = 'https://api.orcid.org/oauth/token'
#    PROFILE_URL = 'https://pub.orcid.org/v1.2/{}/orcid-profile'
    AUTHORIZATION_URL = 'https://sandbox.orcid.org/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://api.sandbox.orcid.org/oauth/token'
    PROFILE_URL = 'https://api.sandbox.orcid.org/v1.2/{}/orcid-profile'
    DEFAULT_SCOPE = ['/orcid-profile/read-limited']
    SCOPE_SEPARATOR = ','
    ID_KEY = 'orcid'
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [
        ('orcid', 'id'),
        ('expires_in', 'expires'),
        ('refresh_token', 'refresh_token')
    ]

    def auth_params(self, *args, **kwargs):
        params = super(OrcidOAuth2, self).auth_params(*args, **kwargs)
        return params

    def get_user_details(self, response):
        """Find the names in the response if they exist, annoying deep hash"""
        if response.get('orcid-profile', {}).get('orcid-bio', {}).get('personal-details', None):
            personal_details = response.get('orcid-profile', {}).get('orcid-bio', {}).get('personal-details', {})
            if personal_details.get('family-name', {}).get('value', None):
                last_name = personal_details.get('family-name', {}).get('value', '')
            else:
                last_name = ''

            if personal_details.get('given-names', {}).get('value', None):
                first_name = personal_details.get('given-names', {}).get('value', '')
            else:
                first_name = ''

        """Return user details from Orcid account"""
        return {'username': response.get('orcid'),
                'email': response.get('email') or '',
                'fullname': response.get('name'),
                'first_name': first_name,
                'last_name': last_name
        }

    def extra_data(self, user, uid, response, details=None, *args, **kwargs):
        """Return access_token and extra defined names to store in
        extra_data field"""
        data = super(OrcidOAuth2, self).extra_data(user, uid, response,
            details, *args, **kwargs)
        if 'orcid-profile' in response and \
           'orcid-bio' in response['orcid-profile']:
            data['oric-bio'] = response['orcid-profile']['orcid-bio']
            
        return data

    def user_data(self, access_token, *args, **kwargs):

        """Loads user data from service"""
        url = self.PROFILE_URL.format(kwargs['response']['orcid'])
        try:
            return self.get_json(url,
                                 headers={'Content-Type': 'application/json',
                                          'Authorization': "Bearer {}".format(access_token)})
        except ValueError:
            return None

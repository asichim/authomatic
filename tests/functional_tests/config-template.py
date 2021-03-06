# -*- coding: utf-8 -*-
import datetime

import constants


# Choose and configure the browser of your choice
def get_browser():
    return webdriver.Chrome()


# The host and port where the tested ap shoud listen.
HOST = '127.0.0.1'
PORT = 8080

# The host alias set in the /etc/hosts file.
# The actual tests will navigate selenium browser to this host.
# This is necessary because some providers don't support localhost as the
# callback url.
HOST_ALIAS = 'authomatic.com'

# Only frameworks included here will be tested.
INCLUDE_FRAMEWORKS = [
    # 'django',
    'flask', # Runs with https
    # 'pyramid',
]

# Only providers included here will be tested.
INCLUDE_PROVIDERS = [
    'twitter',

    'amazon',
    # 'behance', # Behance doesn't support third party authorization anymore.
    'bitly',
    'deviantart',
    'facebook',
    'foursquare',
    'google',
    'github',
    'linkedin',
    'paypal',
    'reddit',
    'vk',
    'windowslive',
    'yammer',
    'yandex',

    'openid_yahoo',
    'openid_livejournal',
    'openid_wordpress',
    'openid_verisignlabs',
]

# Use these constants if you have the same user info by all tested providers.
EMAIL = 'andy.pipkin@littlebritain.co.uk'
FIRST_NAME = 'Andy'
LAST_NAME = 'Pipkin'
NAME = FIRST_NAME + ' ' + LAST_NAME
USERNAME = 'andypipkin'
USERNAME_REVERSE = 'pipkinandy'
NICKNAME = 'Mr. Pipkin'
BIRTH_YEAR = '1979'
BIRTH_DATE = datetime.datetime(1979, 12, 31).strftime('%x')
CITY = 'London'
COUNTRY = 'Great Britain'
POSTAL_CODE = 'EC1A1DH'
PHONE = '??????????'
PHONE_INTERNATIONAL = '0044??????????'
GENDER = constants.GENDER_MALE
LOCALE = 'en_UK'

# Common values for all providers
COMMON = {
    # Could be same if the user sets it so
    'user_birth_date': BIRTH_DATE,
    'user_login': EMAIL,
    'user_email': EMAIL,
    'user_first_name': FIRST_NAME,
    'user_last_name': LAST_NAME,
    'user_name': NAME,
    'user_username': USERNAME,
    'user_username_reverse': USERNAME_REVERSE,
    'user_nickname': NICKNAME,
    'user_birth_year': BIRTH_YEAR,
    'user_city': CITY,
    'user_country': COUNTRY,
    'user_gender': GENDER,
    'user_phone': PHONE,
    'user_postal_code': POSTAL_CODE,
    'user_locale': LOCALE,

    # It is not a good idea to have the same password for all providers
    # 'user_password': '##########',

    # Provider and user specific value
    # 'user_id': '',
    # 'user_locale': None,
    # 'user_timezone': None,

    # Provider specific format
    # 'user_picture': '',
    # 'user_link': '',

    # Provider specific value
    # 'consumer_key': '',
    # 'consumer_secret': '',
}

# Values from COMMON will be overriden by values from PROVIDERS[provider_name]
# if set.
PROVIDERS = {
    # OAuth 1.0a
    'twitter': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'user_id': '???',
        'user_password': '##########',
        'user_link': '???',
        'user_picture': '???',
        'user_username': '???',
        'user_locale': '???',
    },

    # OAuth 2.0
    'amazon': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'user_id': '??????????',
        'user_password': '##########',
    },
    # Behance doesn't support third party authorization anymore.
    # 'behance': {
    #     'consumer_key': '##########',
    #     'consumer_secret': '##########',
    #     'user_password': '##########',
    #     'user_id': '??????????',
    # },
    'bitly': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'user_password': '##########',
        'user_id': '??????????',
    },
    'deviantart': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'user_password': '##########',
    },
    'eventbrite': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'user_password': '##########',
        'user_id': '??????????',
    },
    'facebook': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'user_password': '##########',
        'user_id': '??????????',
    },
    'foursquare': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'user_password': '##########',
        'user_id': '??????????',
        # The picture URL is a random CDN URL
        'user_picture': '??????????',
    },
    'google': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'user_password': '##########',
        'user_id': '??????????',
        'user_locale': '??????????',
        # The picture URL is a random CDN URL
        'user_picture': '??????????',
    },
    'github': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'user_password': '##########',
        'user_id': '??????????',
        # GitHub requires the User-Agent header in every request.
        'access_headers': {'User-Agent': ('Authomatic.py Automated Functional '
                                          'Tests')},
    },
    'linkedin': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'user_password': '##########',
        'user_id': '??????????',
        # User link contains a slug derived from the username.
        'user_link': 'http://www.linkedin.com/in/??????????',
        # GitHub requires the User-Agent header in every request.
        'user_picture': '??????????',
        'user_phone': PHONE_INTERNATIONAL,
    },
    'paypal': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
    },
    'reddit': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'user_login': USERNAME,
        'user_id': '??????????',
        'access_headers': {'User-Agent': ('Authomatic.py Automated Functional '
                                          'Tests')}
    },
    # Viadeo doesn't support access to its API
    # http://dev.viadeo.com/documentation/authentication/request-an-api-key/
    # 'viadeo': {
    #     'consumer_key': '##########',
    #     'consumer_secret': '##########',
    # },
    'vk': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'user_password': '##########',
        'user_id': '??????????',
        # City and country are numeric IDs
        'user_city': '??????????',
        'user_country': '??????????',
        'user_gender': '2',
        'user_timezone': '1',
    },
    'windowslive': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'user_password': '##########',
        'user_id': '??????????',
    },
    'yammer': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'user_password': '##########',
        'user_id': '??????????',
        'user_picture': ('https://mug0.assets-yammer.com/mugshot/images/48x48/'
                         '??????????'),
        'user_timezone': '??????????',
        'user_locale': '??????????',
    },
    'yandex': {
        'consumer_key': '##########',
        'consumer_secret': '##########',
        'user_password': '##########',
        'user_login': USERNAME,
        'user_id': '??????????',
    },

    # OpenID
    'openid_yahoo': {
        'openid_identifier': 'me.yahoo.com',
        'user_id': '???',
        'user_login': USERNAME,
        'user_password': '##########',
        'user_email': '{0}@yahoo.com'.format(USERNAME),
    },
    'openid_livejournal': {
        'openid_identifier': '{0}.livejournal.com'.format(USERNAME),
        'user_login': USERNAME,
        'user_password': '##########',
        'user_id': 'http://{0}.livejournal.com/'.format(USERNAME)
    },
    'openid_wordpress': {
        'openid_identifier': '{0}.wordpress.com'.format(USERNAME),
        'user_login': EMAIL,
        'user_password': '##########',
        'user_id': 'https://{0}.wordpress.com/'.format(USERNAME),
        'user_nickname': NICKNAME,
    },
    'openid_verisignlabs': {
        'openid_identifier': '{0}.pip.verisignlabs.com'.format(USERNAME),
        'user_login': USERNAME,
        'user_password': '##########',
        'user_id': 'http://{0}.pip.verisignlabs.com/'.format(USERNAME),
        'user_nickname': NICKNAME,
        'user_timezone': '???', # Europe/Bratislava, Europe/Paris ...
        'user_locale': '???', # Slovak, English ...
        'user_gender': '???', # M or F
    },
}

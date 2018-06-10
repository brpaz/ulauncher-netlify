"""Netify Module"""

import requests
from cache import Cache

class Client:
    """CLass that interacts with Netlify API"""

    API_BASE_URL = "https://api.netlify.com/api/v1/"

    CACHE_TTL = 3600  # 1h

    CACHE_KEY = "netlify_sites"

    def __init__(self, access_token, logger):
        self.access_token = access_token
        self.logger = logger

    def set_access_token(self, access_token):
        self.access_token = access_token

    def filter_sites(self, sites, filter_term=None):
        """Filter the sites returned by Netlify, by the name passed in filter parameter"""
        if not filter_term:
            return sites

        filtered_sites = []
        for site in sites:
            if filter_term.lower() in site['name'].lower() or site["custom_domain"] is not None and filter_term.lower() in site['custom_domain'].lower():
                filtered_sites.append(site)

        return filtered_sites

    def get_sites(self, filter=None):
        """Gets a list of user sites from Netlify"""

        self.logger.debug("getting sites from Netlify")

        if Cache.get(self.CACHE_KEY):
            self.logger.debug("Loading from cache")
            return self.filter_sites(Cache.get(self.CACHE_KEY), filter)

        headers = {
            "Authorization": "Bearer {}".format(
                self.access_token),
            "Accept": "application/json",
            "User-Agent": "Ulauncher-Netlify"}
        r = requests.get(self.API_BASE_URL + '/sites/', headers=headers)

        if not r.ok:
            if r.status_code == 401:
                raise AuthenticationException(
                    "Failed to authenticate with access token " + self.access_token)

            raise GenericException(
                "Error connecting to Netlify API : status " + r.status_code)

        data = r.json()

        Cache.set(self.CACHE_KEY, data, self.CACHE_TTL)

        return self.filter_sites(data, filter)

class GenericException(Exception):
    pass

class AuthenticationException(Exception):
    pass

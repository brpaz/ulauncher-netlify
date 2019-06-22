"""
Netlify Extension
Provides quick access to your Netlify Projects
"""

import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from netlify import Client as NetlifyClient, AuthenticationException, GenericException

LOGGER = logging.getLogger(__name__)


class NetlifyExtension(Extension):
    """ Main Extension Class """

    def __init__(self):
        LOGGER.info('init Netlify Extension')
        super(NetlifyExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.netlify_client = NetlifyClient("", LOGGER)

    def build_results_list(self, sites):
        """ Builds the result list from a list of sites """
        items = []

        for site in sites:
            name = site["name"]
            if site["custom_domain"] is not None:
                name = site["custom_domain"]

            items.append(ExtensionResultItem(
                icon='images/icon.png',
                name=name,
                on_enter=OpenUrlAction(site["url"]),
                on_alt_enter=OpenUrlAction(site['admin_url'])
            ))

        return items


class KeywordQueryEventListener(EventListener):
    """ Handles query events """

    def on_event(self, event, extension):
        """ Handle query event """
        items = []

        try:
            extension.netlify_client.set_access_token(
                extension.preferences['access_token'])
            sites = extension.netlify_client.get_sites(event.get_argument())

            items = extension.build_results_list(sites)

        except AuthenticationException:
            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name="Authentication failed",
                    description="Please check the 'access_token' value on extension preferences",
                    on_enter=HideWindowAction()))
        except GenericException:
            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name="Error fetching information from Heroku",
                    on_enter=HideWindowAction()))
        return RenderResultListAction(items)


if __name__ == '__main__':
    NetlifyExtension().run()

# -*- coding: utf-8 -*- #
"""This provides the DeFi Llama class implementation which acts as
DeFi Llama's API client."""

import requests

# --------- Constants --------- #

BASE_URL = "https://api.llama.fi"

# --------- Constants --------- #


class DefiLlama:
    """
    DeFi Llama class to act as DeFi Llama's API client.
    All the requests can be made through this class.
    """

    def __init__(self):
        """
        Initialize the object
        """
        self.session = requests.Session()

    def _send_message(self, method, endpoint, params=None, data=None):
        """
        Send API request.
        :param method: HTTP method (get, post, delete, etc.)
        :param endpoint: Endpoint (to be added to base URL)
        :param params: HTTP request parameters
        :param data: JSON-encoded string payload for POST
        :return: dict/list: JSON response
        """
        url = BASE_URL + endpoint
        response = self.session.request(method, url, params=params,
                                 data=data, timeout=30)
        return response.json()

    def _get(self, endpoint, params=None):
        """
        Get API request
        :param endpoint: Endpoint (to be added to base URL)
        :param params: HTTP request parameters
        :return:
        """
        return self._send_message('GET', endpoint, params=params)

    def get_all_protocols(self):
        """
        Returns basic information on all listed protocols, their current
        TVL and the changes to it in the last hour/day/week.
        Endpoint: GET /protocols

        :return: JSON response
        """
        path = '/protocols'

        return self._get(path)

    def get_protocol(self, name):
        """
        Returns historical data on the TVL of a protocol along with some basic data on it.
        The fields `tokensInUsd` and `tokens` are only available for some protocols..
        Endpoint: GET /protocol/{name}

        :param: name : ID of the protocol to get (eg: uniswap, WBTC...).
            This can be obtained from the /protocols endpoint
        :return: JSON response
        """
        path = f'/protocol/{name}'

        return self._get(path)

    def get_historical_tvl(self):
        """
        Get Historical TVL of DeFi on all chains

        :return: JSON response
        """
        path = '/v2/historicalChainTvl'

        return self._get(path)

    def get_historical_tvl_chain(self, chain):
        """
        Get Historical TVL of a chain

        :return: JSON response
        """
        path = f'/v2/historicalChainTvl/{chain}'

        return self._get(path)

    def get_protocol_current_tvl(self, protocol):
        """
        Simplified endpoint that only returns a number, the current TVL of a protocol

        :param: name : ID of the protocol to get (eg: uniswap, WBTC...).
            This can be obtained from the /protocols endpoint
        :return: JSON response
        """
        path = f'/tvl/{protocol}'

        return self._get(path)

    def get_chains_current_tvl(self):
        """
        Returns list of current TVL of all chains.
        
        :return: JSON response
        """
        path = f'/v2/chains'

        return self._get(path)

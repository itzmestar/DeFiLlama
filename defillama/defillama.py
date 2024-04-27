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

    def _send_message(self, method, endpoint, params=None, data=None, full_url=False):
        """
        Send API request.
        :param method: HTTP method (get, post, delete, etc.)
        :param endpoint: Endpoint (to be added to base URL)
        :param params: HTTP request parameters
        :param data: JSON-encoded string payload for POST
        :return: dict/list: JSON response
        """
        url = BASE_URL + endpoint
        if full_url:
            url = endpoint
        response = self.session.request(method, url, params=params,
                                        json=data, timeout=30)
        return response.json()

    def _get(self, endpoint, params=None, full_url=False):
        """
        Get API request
        :param endpoint: Endpoint (to be added to base URL)
        :param params: HTTP request parameters
        :return:
        """
        return self._send_message('GET', endpoint, params=params, full_url=full_url)

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

    # ##### Yields EPs ###### #

    def get_pools(self):
        """
        Get the latest data for all pools
        """
        path = 'https://yields.llama.fi/pools'

        return self._get(path, full_url=True)

    def get_pool(self, pool: str):
        """
        Get the historical APY & TVL data for a pool
        """
        path = f'https://yields.llama.fi/chart/{pool}'

        return self._get(path, full_url=True)

    # ##### Volumes EPs ###### #

    def get_dexs(self, excludeTotalDataChart=True, excludeTotalDataChartBreakdown=True, dataType='dailyVolume'):
        """
        list all dexs
        """
        path = '/overview/dexs'
        params = {
            'excludeTotalDataChart': excludeTotalDataChart,
            'excludeTotalDataChartBreakdown': excludeTotalDataChartBreakdown,
            'dataType': dataType
        }

        return self._get(path, params=params)

    def get_chain_dexs(self, chain, excludeTotalDataChart=True, excludeTotalDataChartBreakdown=True, dataType='dailyVolume'):
        """
        list all dexs filter by chain
        """
        path = f'/overview/dexs/{chain}'
        params = {
            'excludeTotalDataChart': excludeTotalDataChart,
            'excludeTotalDataChartBreakdown': excludeTotalDataChartBreakdown,
            'dataType': dataType
        }

        return self._get(path, params=params)

    def get_dex_summary(self, protocol, excludeTotalDataChart=True, excludeTotalDataChartBreakdown=True, dataType='dailyVolume'):
        """
        get summary of dex volume with historical data
        """
        path = f'/summary/dexs/{protocol}'
        params = {
            'excludeTotalDataChart': excludeTotalDataChart,
            'excludeTotalDataChartBreakdown': excludeTotalDataChartBreakdown,
            'dataType': dataType
        }

        return self._get(path, params=params)

    def get_options_dexs(self, excludeTotalDataChart=True, excludeTotalDataChartBreakdown=True, dataType='dailyVolume'):
        """
        list all options dexs
        """
        path = '/overview/options'
        params = {
            'excludeTotalDataChart': excludeTotalDataChart,
            'excludeTotalDataChartBreakdown': excludeTotalDataChartBreakdown,
            'dataType': dataType
        }

        return self._get(path, params=params)

    def get_chain_options_dexs(self, chain, excludeTotalDataChart=True, excludeTotalDataChartBreakdown=True, dataType='dailyVolume'):
        """
        list all options dexs
        """
        path = f'/overview/options/{chain}'
        params = {
            'excludeTotalDataChart': excludeTotalDataChart,
            'excludeTotalDataChartBreakdown': excludeTotalDataChartBreakdown,
            'dataType': dataType
        }

        return self._get(path, params=params)

    def get_options_dex_summary(self, protocol, dataType='dailyPremiumVolume'):
        """
        get summary of option dex volume with historical data
        """
        path = f'/summary/options/{protocol}'
        params = {
            'dataType': dataType
        }

        return self._get(path, params=params)

    # ##### Fees & Revenue EPs ###### #

    def get_fees(self, excludeTotalDataChart=True, excludeTotalDataChartBreakdown=True, dataType='dailyFees'):
        """
                list all protocols along with summaries of their fees & revenue & dataType history data
        """
        path = f'/overview/fees'
        params = {
            'excludeTotalDataChart': excludeTotalDataChart,
            'excludeTotalDataChartBreakdown': excludeTotalDataChartBreakdown,
            'dataType': dataType
        }

        return self._get(path, params=params)

    def get_fees_chain(self, chain, excludeTotalDataChart=True, excludeTotalDataChartBreakdown=True, dataType='dailyFees'):
        """
            list all protocols along with summaries of their fees & revenue & dataType history data by chain
        """
        path = f'/overview/fees/{chain}'
        params = {
            'excludeTotalDataChart': excludeTotalDataChart,
            'excludeTotalDataChartBreakdown': excludeTotalDataChartBreakdown,
            'dataType': dataType
        }

        return self._get(path, params=params)

    def get_fees_protocol(self, protocol, dataType='dailyFees'):
        """
            Get summary of protocol fees and revenue with historical data
        """
        path = f'/overview/fees/{protocol}'
        params = {
            'dataType': dataType
        }

        return self._get(path, params=params)

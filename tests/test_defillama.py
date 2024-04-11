from unittest import TestCase

import pytest


@pytest.mark.usefixtures('llama')
class TestDefiLlama:
    """
    Test class for DefiLlama
    """

    @pytest.mark.skip(reason='TBD')
    def test__send_message(self):
        assert False

    @pytest.mark.skip(reason='TBD')
    def test__get(self):
        assert False

    def test_get_all_protocols(self, llama):
        response = llama.get_all_protocols()
        assert type(response) is list

    # @pytest.mark.skip(reason='TBD')
    def test_get_protocol(self, llama, protocol_json):
        response = llama.get_protocol(name='aave')
        assert type(response) is dict
        for k in protocol_json.keys():
            assert k in response

    # @pytest.mark.skip(reason='TBD')
    def test_get_historical_tvl(self, llama):
        response = llama.get_historical_tvl()
        assert type(response) is list
        for data in response:
            assert 'date' in data
            assert 'tvl' in data
            break

    def test_get_historical_tvl_chain(self, llama):
        response = llama.get_historical_tvl_chain('Ethereum')
        assert type(response) is list
        for data in response:
            assert 'date' in data
            assert 'tvl' in data
            break

    def test_get_protocol_current_tvl(self, llama):
        response = llama.get_protocol_current_tvl('uniswap')
        assert type(response) is float

    def test_get_chains_current_tvl(self, llama):
        response = llama.get_chains_current_tvl()
        assert type(response) is list
        for data in response:
            assert 'gecko_id' in data
            assert 'tvl' in data
            assert 'tokenSymbol' in data
            assert 'cmcId' in data
            assert 'name' in data
            assert 'chainId' in data
            break


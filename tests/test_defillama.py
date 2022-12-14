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
        response = llama.get_protocol(name='uniswap')
        assert type(response) is dict
        for k in protocol_json.keys():
            assert k in response

    # @pytest.mark.skip(reason='TBD')
    def test_get_historical_tvl(self, llama):
        response = llama.get_historical_tvl()
        assert type(response) is list
        for data in response:
            assert 'date' in data
            assert 'totalLiquidityUSD' in data

    # @pytest.mark.skip(reason='TBD')
    def test_get_protocol_tvl(self, llama):
        response = llama.get_protocol_tvl(name='uniswap')
        assert type(response) is float

    # @pytest.mark.skip(reason='TBD')
    def test_get_chain_tvl(self, llama):
        response = llama.get_chain_tvl('ethereum')
        assert type(response) is list

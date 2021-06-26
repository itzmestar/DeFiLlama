import pytest
from defillama import DefiLlama


@pytest.fixture(scope='module', autouse=True)
def llama():
    print('======================================')
    yield DefiLlama()
    print('///////////////////////////////////////')


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
    def test_get_protocol(self, llama):
        response = llama.get_protocol(name='uniswap')
        assert type(response) is dict

    # @pytest.mark.skip(reason='TBD')
    def test_get_historical_tvl(self, llama):
        response = llama.get_historical_tvl()
        assert type(response) is list

    # @pytest.mark.skip(reason='TBD')
    def test_get_protocol_tvl(self, llama):
        response = llama.get_protocol_tvl(name='uniswap')
        assert type(response) is float

import pytest
from defillama import DefiLlama
import json


@pytest.fixture(scope='session')
def llama():
    print('======================================')
    yield DefiLlama()
    print('///////////////////////////////////////')


@pytest.fixture
def protocol_json():
    data = None
    with open('tests/protocol_sample.json') as f:
        data = json.load(f)
    return data

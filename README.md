# DeFiLlama

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-31014/)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3119/)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3123/)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[![Build](https://github.com/itzmestar/DeFiLlama/actions/workflows/python-package.yml/badge.svg)](https://github.com/itzmestar/DeFiLlama/actions/workflows/python-package.yml)


### Unofficial [DeFi Llama API](https://defillama.com/home) client in python

For detailed information about the API endpoints, see [DeFi Llama API Documentation](https://defillama.com/docs/api)

### Installation:

use pip to install:

``` 
pip install DeFiLlama
```

-----------

### Authentication:

Endpoints are accessible without an API key.

-----------

### Example usage:

```
from defillama import DefiLlama

# initialize api client
llama = DefiLlama()

# Get all protocols data
response = llama.get_all_protocols()

# Get a protocol data
response = llama.get_protocol(name='uniswap')

```

Data from stablecoins dashboard

```
# List all stablecoins along with their circulating amounts
response = llama.get_stablecoins()

# Get historical mcap sum of all stablecoins in a chain
response = llama.get_stablecoins_chains_all_historical_mcap_sum(chain='Ethereum', stablecoin_id=1)
```

-------
#### Donate & Help maintain the library

[![Paypal](qrcode.png)](https://www.paypal.com/ncp/payment/KLFNJN7SH39EN)

-------
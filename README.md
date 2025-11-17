# Craftgate Python Client

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/craftgate/craftgate-python-client)

This repo contains the Python client for Craftgate API.

PyPI package: <https://pypi.org/project/craftgate/>

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/craftgate/craftgate-python-client)

## Requirements

- Python 3.6+

## Installation

~~~bash
pip install craftgate
~~~

## Usage

To access the Craftgate API you'll first need to obtain API credentials (API key & secret key). If you don't already
have a Craftgate account, you can sign up at <https://craftgate.io>.

By default the client connects to production `https://api.craftgate.io`. For testing, use the sandbox URL
`https://sandbox-api.craftgate.io`.

~~~python
from craftgate import Craftgate, RequestOptions

options = RequestOptions(
    api_key="<YOUR API KEY>",
    secret_key="<YOUR SECRET KEY>",
    base_url="https://sandbox-api.craftgate.io"
)
payment = Craftgate(options).payment()
~~~

## Example: Credit Card Payment

~~~python
import uuid
from decimal import Decimal

from craftgate import Craftgate, RequestOptions
from craftgate.model import Currency, PaymentGroup, PaymentPhase
from craftgate.request import CreatePaymentRequest
from craftgate.request.dto import Card, PaymentItem

# Configure client (use sandbox for testing)
options = RequestOptions(
    api_key="<YOUR API KEY>",
    secret_key="<YOUR SECRET KEY>",
    base_url="https://sandbox-api.craftgate.io"
)
craftgate = Craftgate(options)
payment = craftgate.payment()

# Build basket
items = []
for name, price in [("item 1", "30"), ("item 2", "50"), ("item 3", "20")]:
    pi = PaymentItem()
    pi.name = name
    pi.external_id = str(uuid.uuid4())
    pi.price = Decimal(price)
    items.append(pi)

# Card info (sandbox test card)
card = Card()
card.card_holder_name = "Haluk Demir"
card.card_number = "5258640000000001"
card.expire_year = "2044"
card.expire_month = "07"
card.cvc = "000"

# Payment request
req = CreatePaymentRequest()
req.price = Decimal("100")
req.paid_price = Decimal("100")
req.wallet_price = Decimal("0")
req.installment = 1
req.currency = Currency.TRY
req.conversation_id = "456d1297-908e-4bd6-a13b-4be31a6e47d5"
req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
req.payment_phase = PaymentPhase.AUTH
req.card = card
req.items = items

resp = payment.create_payment(req)
print(f"Create Payment Result: {resp}")
~~~

## Examples

A variety of end-to-end samples (3DS, Checkout, APM, refunds, stored cards, marketplace, pre/post-auth) live under the
`tests/` folder.

Run a single test:

~~~bash
python -m unittest tests/test_payment_sample.py::PaymentSample::test_create_payment
~~~

## Contributions

For all contributions to this client please see the contribution guide at `CONTRIBUTING.md`.

## License

MIT

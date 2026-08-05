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

## Idempotency

Mutating operations accept an optional idempotency key. Set it on the request object and the
client sends it as the `x-idempotency-key` header, so a request can be safely retried (e.g. after a timeout) without the
operation being performed twice — the server returns the result of the first request when it sees a repeated key.

Every request extends `BaseRequest`, which carries a `HeaderOptions` object, so the key is available on any request:

~~~python
import uuid

from craftgate import HeaderOptions

req = CreatePaymentRequest()
req.price = Decimal("100")
req.paid_price = Decimal("100")
req.currency = Currency.TRY
req.payment_group = PaymentGroup.LISTING_OR_SUBSCRIPTION
req.header_options = HeaderOptions(idempotency_key=str(uuid.uuid4()))
# ... other fields

resp = payment.create_payment(req)
~~~

`with_header_options()` sets it inline and returns the request, which is handy for operations whose parameters live in
the URL path:

~~~python
payment.expire_checkout_payment(
    ExpireCheckoutPaymentRequest(token="456d1297-908e-4bd6-a13b-4be31a6e47d5")
    .with_header_options(HeaderOptions(idempotency_key=str(uuid.uuid4()))))
~~~

> Use a fresh key per distinct operation, and reuse the same key when retrying that operation.

> The API honours the key on `POST`, `PATCH` and `DELETE` only. It is ignored on `PUT` endpoints, so retrying one of those is not de-duplicated.

`HeaderOptions` is sent as headers only — it never appears in the request body, the query string, or the request
signature.

## Examples

A variety of end-to-end samples (3DS, Checkout, APM, refunds, stored cards, marketplace, pre/post-auth) live under the
`tests/` folder.

Run a single test:

~~~bash
python -m unittest tests/test_payment_sample.py::PaymentSample::test_create_payment
~~~

## Contributions

For all contributions to this client please see the contribution guide at [CONTRIBUTING.md](CONTRIBUTING.md). By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Security

If you discover a security vulnerability, please review our [Security Policy](SECURITY.md) for how to report it responsibly.

## License

This project is licensed under the Apache License, Version 2.0 — see the [LICENSE](LICENSE) and [NOTICE](NOTICE.md) files for details.

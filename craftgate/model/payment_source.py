from enum import Enum


class PaymentSource(str, Enum):
    API = "API"
    CHECKOUT_FORM = "CHECKOUT_FORM"
    PAY_BY_LINK = "PAY_BY_LINK"
    JUZDAN = "JUZDAN"
    HEPSIPAY = "HEPSIPAY"
    MONO = "MONO"

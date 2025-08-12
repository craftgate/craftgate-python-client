from enum import Enum


class PaymentSource(str, Enum):
    API = "API"
    CHECKOUT_FORM = "CHECKOUT_FORM"
    PAY_BY_LINK = "PAY_BY_LINK"
    JUZDAN = "JUZDAN"
    BKM_EXPRESS = "BKM_EXPRESS"
    HEPSIPAY = "HEPSIPAY"
    MONO = "MONO"

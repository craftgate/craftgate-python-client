from enum import Enum


class PaymentGroup(str, Enum):
    PRODUCT = "PRODUCT"
    LISTING_OR_SUBSCRIPTION = "LISTING_OR_SUBSCRIPTION"

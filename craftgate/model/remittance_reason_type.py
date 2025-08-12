from enum import Enum


class RemittanceReasonType(str, Enum):
    SUBMERCHANT_SEND_RECEIVE = "SUBMERCHANT_SEND_RECEIVE"
    REDEEM_ONLY_LOYALTY = "REDEEM_ONLY_LOYALTY"

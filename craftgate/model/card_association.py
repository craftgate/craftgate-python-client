from enum import Enum


class CardAssociation(str, Enum):
    VISA = "VISA"
    MASTER_CARD = "MASTER_CARD"
    AMEX = "AMEX"
    TROY = "TROY"
    JCB = "JCB"
    UNION_PAY = "UNION_PAY"
    DISCOVER = "DISCOVER"
    DINERS_CLUB = "DINERS_CLUB"

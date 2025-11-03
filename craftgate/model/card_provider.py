from enum import Enum


class CardProvider(str, Enum):
    IYZICO = "IYZICO"
    IPARA = "IPARA"
    BIRLESIK_ODEME = "BIRLESIK_ODEME"
    MEX = "MEX"

from typing import Optional
from craftgate.model.currency import Currency

class SearchMerchantPosRequest(object):
    def __init__(
        self,
        name=None,                 # type: Optional[str]
        alias=None,                # type: Optional[str]
        currency=None,             # type: Optional[Currency]
        enable_installment=None,   # type: Optional[bool]
        enable_foreign_card=None,  # type: Optional[bool]
        bank_name=None,            # type: Optional[str]
        page=None,                 # type: Optional[int]
        size=None                  # type: Optional[int]
    ):
        self.name = name
        self.alias = alias
        self.currency = currency
        self.enable_installment = enable_installment
        self.enable_foreign_card = enable_foreign_card
        self.bank_name = bank_name
        self.page = page
        self.size = size
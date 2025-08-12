from typing import Optional

from craftgate.model.currency import Currency


class SearchMerchantPosRequest(object):
    def __init__(
            self,
            name: Optional[str] = None,
            alias: Optional[str] = None,
            currency: Optional[Currency] = None,
            enable_installment: Optional[bool] = None,
            enable_foreign_card: Optional[bool] = None,
            bank_name: Optional[str] = None,
            page: Optional[int] = None,
            size: Optional[int] = None
    ) -> None:
        self.name = name
        self.alias = alias
        self.currency = currency
        self.enable_installment = enable_installment
        self.enable_foreign_card = enable_foreign_card
        self.bank_name = bank_name
        self.page = page
        self.size = size

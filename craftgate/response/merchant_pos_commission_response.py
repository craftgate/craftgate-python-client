from typing import Optional
from decimal import Decimal
from craftgate.model.status import Status


class MerchantPosCommissionResponse(object):
    def __init__(
        self,
        id=None,  # type: Optional[int]
        status=None,  # type: Optional[Status]
        installment=None,  # type: Optional[int]
        blockage_day=None,  # type: Optional[int]
        installment_label=None,  # type: Optional[str]
        card_brand_name=None,  # type: Optional[str]
        bank_on_us_credit_card_commission_rate=None,  # type: Optional[Decimal]
        bank_not_on_us_credit_card_commission_rate=None,  # type: Optional[Decimal]
        bank_on_us_debit_card_commission_rate=None,  # type: Optional[Decimal]
        bank_not_on_us_debit_card_commission_rate=None,  # type: Optional[Decimal]
        bank_foreign_card_commission_rate=None,  # type: Optional[Decimal]
        merchant_commission_rate=None  # type: Optional[Decimal]
    ):
        self.id = id
        self.status = status
        self.installment = installment
        self.blockage_day = blockage_day
        self.installment_label = installment_label
        self.card_brand_name = card_brand_name
        self.bank_on_us_credit_card_commission_rate = bank_on_us_credit_card_commission_rate
        self.bank_not_on_us_credit_card_commission_rate = bank_not_on_us_credit_card_commission_rate
        self.bank_on_us_debit_card_commission_rate = bank_on_us_debit_card_commission_rate
        self.bank_not_on_us_debit_card_commission_rate = bank_not_on_us_debit_card_commission_rate
        self.bank_foreign_card_commission_rate = bank_foreign_card_commission_rate
        self.merchant_commission_rate = merchant_commission_rate
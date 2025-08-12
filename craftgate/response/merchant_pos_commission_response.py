from decimal import Decimal
from typing import Optional

from craftgate.model.status import Status


class MerchantPosCommissionResponse(object):
    def __init__(
            self,
            id: Optional[int] = None,
            status: Optional[Status] = None,
            installment: Optional[int] = None,
            blockage_day: Optional[int] = None,
            installment_label: Optional[str] = None,
            card_brand_name: Optional[str] = None,
            bank_on_us_credit_card_commission_rate: Optional[Decimal] = None,
            bank_not_on_us_credit_card_commission_rate: Optional[Decimal] = None,
            bank_on_us_debit_card_commission_rate: Optional[Decimal] = None,
            bank_not_on_us_debit_card_commission_rate: Optional[Decimal] = None,
            bank_foreign_card_commission_rate: Optional[Decimal] = None,
            merchant_commission_rate: Optional[Decimal] = None
    ) -> None:
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

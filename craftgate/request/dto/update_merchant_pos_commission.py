from typing import Optional

from craftgate.model.status import Status


class UpdateMerchantPosCommission(object):
    def __init__(
        self,
        card_brand_name=None,                                 # type: Optional[str]
        installment=None,                                     # type: Optional[int]
        status=None,                                          # type: Optional[Status]
        blockage_day=None,                                    # type: Optional[int]
        installment_label=None,                               # type: Optional[str]
        bank_on_us_credit_card_commission_rate=None,          # type: Optional[float]
        bank_on_us_debit_card_commission_rate=None,           # type: Optional[float]
        bank_not_on_us_credit_card_commission_rate=None,      # type: Optional[float]
        bank_not_on_us_debit_card_commission_rate=None,       # type: Optional[float]
        bank_foreign_card_commission_rate=None,               # type: Optional[float]
        merchant_commission_rate=None                         # type: Optional[float]
    ):
        self.card_brand_name = card_brand_name
        self.installment = installment
        self.status = status
        self.blockage_day = blockage_day
        self.installment_label = installment_label
        self.bank_on_us_credit_card_commission_rate = bank_on_us_credit_card_commission_rate
        self.bank_on_us_debit_card_commission_rate = bank_on_us_debit_card_commission_rate
        self.bank_not_on_us_credit_card_commission_rate = bank_not_on_us_credit_card_commission_rate
        self.bank_not_on_us_debit_card_commission_rate = bank_not_on_us_debit_card_commission_rate
        self.bank_foreign_card_commission_rate = bank_foreign_card_commission_rate
        self.merchant_commission_rate = merchant_commission_rate
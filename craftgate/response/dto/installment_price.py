from typing import Optional


class InstallmentPrice(object):
    def __init__(
        self,
        pos_alias=None,                         # type: Optional[str]
        installment_number=None,                # type: Optional[int]
        installment_price=None,                 # type: Optional[float]
        bank_commission_rate=None,              # type: Optional[float]
        merchant_commission_rate=None,          # type: Optional[float]
        total_price=None,                       # type: Optional[float]
        installment_label=None,                 # type: Optional[str]
        loyalty_supported=None,                 # type: Optional[bool]
        force3ds=None,                          # type: Optional[bool]
        cvc_required=None                       # type: Optional[bool]
    ):
        self.pos_alias = pos_alias
        self.installment_number = installment_number
        self.installment_price = installment_price
        self.bank_commission_rate = bank_commission_rate
        self.merchant_commission_rate = merchant_commission_rate
        self.total_price = total_price
        self.installment_label = installment_label
        self.loyalty_supported = loyalty_supported
        self.force3ds = force3ds
        self.cvc_required = cvc_required
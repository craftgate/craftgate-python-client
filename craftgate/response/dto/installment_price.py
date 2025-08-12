from decimal import Decimal
from typing import Optional


class InstallmentPrice(object):
    def __init__(
            self,
            pos_alias: Optional[str] = None,
            installment_number: Optional[int] = None,
            installment_price: Optional[Decimal] = None,
            bank_commission_rate: Optional[Decimal] = None,
            merchant_commission_rate: Optional[Decimal] = None,
            total_price: Optional[Decimal] = None,
            installment_label: Optional[str] = None,
            loyalty_supported: Optional[bool] = None,
            force3ds: Optional[bool] = None,
            cvc_required: Optional[bool] = None
    ) -> None:
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

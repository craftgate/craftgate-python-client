from craftgate.model.transaction_status import TransactionStatus
from craftgate.response.dto.payout import Payout

class PaymentTransactionResponse(object):
    def __init__(
        self, id=None, name=None, external_id=None, price=None, paid_price=None, wallet_price=None,
        merchant_commission_rate=None, merchant_commission_rate_amount=None,
        merchant_payout_amount=None, sub_merchant_member_id=None, sub_merchant_member_price=None,
        sub_merchant_member_payout_rate=None, sub_merchant_member_payout_amount=None,
        transaction_status=None, blockage_resolved_date=None, payout=None
    ):
        self.id = id
        self.name = name
        self.external_id = external_id
        self.price = price
        self.paid_price = paid_price
        self.wallet_price = wallet_price
        self.merchant_commission_rate = merchant_commission_rate
        self.merchant_commission_rate_amount = merchant_commission_rate_amount
        self.merchant_payout_amount = merchant_payout_amount
        self.sub_merchant_member_id = sub_merchant_member_id
        self.sub_merchant_member_price = sub_merchant_member_price
        self.sub_merchant_member_payout_rate = sub_merchant_member_payout_rate
        self.sub_merchant_member_payout_amount = sub_merchant_member_payout_amount
        self.transaction_status = TransactionStatus(transaction_status) if transaction_status else None
        self.blockage_resolved_date = blockage_resolved_date
        self.payout = Payout(**payout) if isinstance(payout, dict) else payout
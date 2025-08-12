from typing import Optional
from craftgate.model.payment_status import PaymentStatus
from craftgate.model.apm_additional_action import ApmAdditionalAction
from craftgate.response.dto.payment_error import PaymentError
from craftgate.response.dto.wallet_transaction import WalletTransaction

class ApmDepositPaymentResponse(object):
    def __init__(
        self,
        payment_id=None,         # type: Optional[int]
        redirect_url=None,       # type: Optional[str]
        payment_status=None,     # type: Optional[PaymentStatus]
        additional_action=None,  # type: Optional[ApmAdditionalAction]
        payment_error=None,      # type: Optional[PaymentError]
        wallet_transaction=None  # type: Optional[WalletTransaction]
    ):
        self.payment_id = payment_id
        self.redirect_url = redirect_url
        self.payment_status = payment_status
        self.additional_action = additional_action
        self.payment_error = payment_error
        self.wallet_transaction = wallet_transaction
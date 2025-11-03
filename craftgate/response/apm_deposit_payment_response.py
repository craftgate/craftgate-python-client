from typing import Optional

from craftgate.model.apm_additional_action import ApmAdditionalAction
from craftgate.model.payment_status import PaymentStatus
from craftgate.response.dto.payment_error import PaymentError
from craftgate.response.dto.wallet_transaction import WalletTransaction


class ApmDepositPaymentResponse(object):
    def __init__(
            self,
            payment_id: Optional[int] = None,
            redirect_url: Optional[str] = None,
            payment_status: Optional[PaymentStatus] = None,
            additional_action: Optional[ApmAdditionalAction] = None,
            payment_error: Optional[PaymentError] = None,
            wallet_transaction: Optional[WalletTransaction] = None
    ) -> None:
        self.payment_id = payment_id
        self.redirect_url = redirect_url
        self.payment_status = payment_status
        self.additional_action = additional_action
        self.payment_error = payment_error
        self.wallet_transaction = wallet_transaction

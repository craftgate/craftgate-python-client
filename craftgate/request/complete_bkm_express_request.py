from typing import Optional


class CompleteBkmExpressRequest:
    def __init__(
            self,
            status: Optional[bool] = None,
            message: Optional[str] = None,
            ticket_id: Optional[str] = None,
            bkm_express_payment_token: Optional[str] = None
    ) -> None:
        self.status = status
        self.message = message
        self.ticket_id = ticket_id
        self.bkm_express_payment_token = bkm_express_payment_token

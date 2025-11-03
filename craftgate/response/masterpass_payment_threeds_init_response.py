from typing import Optional


class MasterpassPaymentThreeDSInitResponse(object):
    def __init__(
            self,
            payment_id: Optional[int] = None,
            return_url: Optional[str] = None
    ) -> None:
        self.payment_id = payment_id
        self.return_url = return_url

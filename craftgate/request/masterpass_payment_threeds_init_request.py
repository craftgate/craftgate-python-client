from typing import Optional


class MasterpassPaymentThreeDSInitRequest(object):
    def __init__(
            self,
            reference_id: Optional[str] = None,
            callback_url: Optional[str] = None
    ) -> None:
        self.reference_id = reference_id
        self.callback_url = callback_url

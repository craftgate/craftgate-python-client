from typing import Optional


class MasterpassPaymentTokenGenerateResponse(object):
    def __init__(
            self,
            token: Optional[str] = None,
            reference_id: Optional[str] = None,
            order_no: Optional[str] = None,
            terminal_group_id: Optional[str] = None
    ) -> None:
        self.token = token
        self.reference_id = reference_id
        self.order_no = order_no
        self.terminal_group_id = terminal_group_id

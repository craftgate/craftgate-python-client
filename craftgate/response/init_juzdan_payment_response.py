from typing import Optional


class InitJuzdanPaymentResponse(object):
    def __init__(
        self,
        reference_id=None,        # type: Optional[str]
        juzdan_qr_url=None        # type: Optional[str]
    ):
        self.reference_id = reference_id
        self.juzdan_qr_url = juzdan_qr_url
from typing import Optional


class InitJuzdanPaymentResponse(object):
    def __init__(
            self,
            reference_id: Optional[str] = None,
            juzdan_qr_url: Optional[str] = None
    ) -> None:
        self.reference_id = reference_id
        self.juzdan_qr_url = juzdan_qr_url

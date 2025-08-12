from typing import Optional

from craftgate.model.loyalty import Loyalty
from craftgate.model.masterpass_validation_type import MasterpassValidationType
from craftgate.request.dto.masterpass_create_payment import MasterpassCreatePayment


class MasterpassPaymentTokenGenerateRequest(object):
    def __init__(
            self,
            msisdn: Optional[str] = None,
            user_id: Optional[str] = None,
            bin_number: Optional[str] = None,
            force_three_d_s: Optional[bool] = None,
            is_msisdn_validated: Optional[bool] = None,
            create_payment: Optional[MasterpassCreatePayment] = None,
            masterpass_integration_version: Optional[int] = None,
            loyalty: Optional[Loyalty] = None,
            validation_type: Optional[MasterpassValidationType] = None
    ) -> None:
        self.msisdn = msisdn
        self.user_id = user_id
        self.bin_number = bin_number
        self.force_three_d_s = force_three_d_s
        self.is_msisdn_validated = is_msisdn_validated
        self.create_payment = create_payment
        self.masterpass_integration_version = masterpass_integration_version
        self.loyalty = loyalty
        self.validation_type = validation_type

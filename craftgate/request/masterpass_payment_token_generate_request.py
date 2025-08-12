from typing import Optional

from craftgate.model.loyalty import Loyalty
from craftgate.model.masterpass_validation_type import MasterpassValidationType
from craftgate.request.dto.masterpass_create_payment import MasterpassCreatePayment


class MasterpassPaymentTokenGenerateRequest(object):
    def __init__(
            self,
            msisdn=None,  # type: Optional[str]
            user_id=None,  # type: Optional[str]
            bin_number=None,  # type: Optional[str]
            force_three_d_s=None,  # type: Optional[bool]
            is_msisdn_validated=None,  # type: Optional[bool]
            create_payment=None,  # type: Optional[MasterpassCreatePayment]
            masterpass_integration_version=None,  # type: Optional[int]
            loyalty=None,  # type: Optional[Loyalty]
            validation_type=None  # type: Optional[MasterpassValidationType]
    ):
        self.msisdn = msisdn
        self.user_id = user_id
        self.bin_number = bin_number
        self.force_three_d_s = force_three_d_s
        self.is_msisdn_validated = is_msisdn_validated
        self.create_payment = create_payment
        self.masterpass_integration_version = masterpass_integration_version
        self.loyalty = loyalty
        self.validation_type = validation_type

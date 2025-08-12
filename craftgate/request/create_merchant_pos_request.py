from typing import Optional, List

from craftgate.model.currency import Currency
from craftgate.model.payment_authentication_type import PaymentAuthenticationType
from craftgate.model.pos_integrator import PosIntegrator
from craftgate.model.pos_status import PosStatus
from craftgate.request.dto.create_merchant_pos_user import CreateMerchantPosUser


class CreateMerchantPosRequest(object):
    def __init__(
            self,
            status=PosStatus.AUTOPILOT,  # type: PosStatus
            name=None,  # type: Optional[str]
            client_id=None,  # type: Optional[str]
            currency=None,  # type: Optional[Currency]
            posnet_id=None,  # type: Optional[str]
            terminal_id=None,  # type: Optional[str]
            threeds_posnet_id=None,  # type: Optional[str]
            threeds_terminal_id=None,  # type: Optional[str]
            threeds_key=None,  # type: Optional[str]
            enable_foreign_card=None,  # type: Optional[bool]
            enable_installment=None,  # type: Optional[bool]
            enable_payment_without_cvc=None,  # type: Optional[bool]
            enable_loyalty=None,  # type: Optional[bool]
            new_integration=None,  # type: Optional[bool]
            order_number=None,  # type: Optional[int]
            pos_integrator=None,  # type: Optional[PosIntegrator]
            enabled_payment_authentication_types=None,  # type: Optional[List[PaymentAuthenticationType]]
            merchant_pos_users=None  # type: Optional[List[CreateMerchantPosUser]]
    ):
        self.status = status
        self.name = name
        self.client_id = client_id
        self.currency = currency
        self.posnet_id = posnet_id
        self.terminal_id = terminal_id
        self.threeds_posnet_id = threeds_posnet_id
        self.threeds_terminal_id = threeds_terminal_id
        self.threeds_key = threeds_key
        self.enable_foreign_card = enable_foreign_card
        self.enable_installment = enable_installment
        self.enable_payment_without_cvc = enable_payment_without_cvc
        self.enable_loyalty = enable_loyalty
        self.new_integration = new_integration
        self.order_number = order_number
        self.pos_integrator = pos_integrator
        self.enabled_payment_authentication_types = enabled_payment_authentication_types
        self.merchant_pos_users = merchant_pos_users

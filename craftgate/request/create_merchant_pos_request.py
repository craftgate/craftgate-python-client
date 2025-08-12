from typing import Optional, List

from craftgate.model.currency import Currency
from craftgate.model.payment_authentication_type import PaymentAuthenticationType
from craftgate.model.pos_integrator import PosIntegrator
from craftgate.model.pos_status import PosStatus
from craftgate.request.dto.create_merchant_pos_user import CreateMerchantPosUser


class CreateMerchantPosRequest(object):
    def __init__(
            self,
            status: PosStatus = PosStatus.AUTOPILOT,
            name: Optional[str] = None,
            client_id: Optional[str] = None,
            currency: Optional[Currency] = None,
            posnet_id: Optional[str] = None,
            terminal_id: Optional[str] = None,
            threeds_posnet_id: Optional[str] = None,
            threeds_terminal_id: Optional[str] = None,
            threeds_key: Optional[str] = None,
            enable_foreign_card: Optional[bool] = None,
            enable_installment: Optional[bool] = None,
            enable_payment_without_cvc: Optional[bool] = None,
            enable_loyalty: Optional[bool] = None,
            new_integration: Optional[bool] = None,
            order_number: Optional[int] = None,
            pos_integrator: Optional[PosIntegrator] = None,
            enabled_payment_authentication_types: Optional[List[PaymentAuthenticationType]] = None,
            merchant_pos_users: Optional[List[CreateMerchantPosUser]] = None
    ) -> None:
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

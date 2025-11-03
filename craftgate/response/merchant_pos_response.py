from typing import List, Optional

from craftgate.model.autopilot_state import AutopilotState
from craftgate.model.card_association import CardAssociation
from craftgate.model.currency import Currency
from craftgate.model.payment_authentication_type import PaymentAuthenticationType
from craftgate.model.pos_integrator import PosIntegrator
from craftgate.model.pos_status import PosStatus
from craftgate.response.dto.merchant_pos_user import MerchantPosUser


class MerchantPosResponse(object):
    def __init__(
            self,
            id: Optional[int] = None,
            status: Optional[PosStatus] = None,
            name: Optional[str] = None,
            alias: Optional[str] = None,
            pos_integrator: Optional[PosIntegrator] = None,
            hostname: Optional[str] = None,
            client_id: Optional[str] = None,
            pos_currency_code: Optional[str] = None,
            mode: Optional[str] = None,
            path: Optional[str] = None,
            port: Optional[int] = None,
            posnet_id: Optional[str] = None,
            terminal_id: Optional[str] = None,
            threeds_posnet_id: Optional[str] = None,
            threeds_terminal_id: Optional[str] = None,
            threeds_key: Optional[str] = None,
            threeds_path: Optional[str] = None,
            enable_foreign_card: Optional[bool] = None,
            enable_installment: Optional[bool] = None,
            enable_payment_without_cvc: Optional[bool] = None,
            enable_loyalty: Optional[bool] = None,
            new_integration: Optional[bool] = None,
            order_number: Optional[int] = None,
            autopilot_state: Optional[AutopilotState] = None,
            currency: Optional[Currency] = None,
            bank_id: Optional[int] = None,
            bank_name: Optional[str] = None,
            is_pf: Optional[bool] = None,
            merchant_pos_users: Optional[List[MerchantPosUser]] = None,
            supported_card_associations: Optional[List[CardAssociation]] = None,
            enabled_payment_authentication_types: Optional[List[PaymentAuthenticationType]] = None
    ) -> None:
        self.id = id
        self.status = status
        self.name = name
        self.alias = alias
        self.pos_integrator = pos_integrator
        self.hostname = hostname
        self.client_id = client_id
        self.pos_currency_code = pos_currency_code
        self.mode = mode
        self.path = path
        self.port = port
        self.posnet_id = posnet_id
        self.terminal_id = terminal_id
        self.threeds_posnet_id = threeds_posnet_id
        self.threeds_terminal_id = threeds_terminal_id
        self.threeds_key = threeds_key
        self.threeds_path = threeds_path
        self.enable_foreign_card = enable_foreign_card
        self.enable_installment = enable_installment
        self.enable_payment_without_cvc = enable_payment_without_cvc
        self.enable_loyalty = enable_loyalty
        self.new_integration = new_integration
        self.order_number = order_number
        self.autopilot_state = autopilot_state
        self.currency = currency
        self.bank_id = bank_id
        self.bank_name = bank_name
        self.is_pf = is_pf
        self.merchant_pos_users = merchant_pos_users
        self.supported_card_associations = supported_card_associations
        self.enabled_payment_authentication_types = enabled_payment_authentication_types

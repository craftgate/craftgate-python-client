from typing import Optional, List

from craftgate.model.pos_status import PosStatus
from craftgate.model.pos_integrator import PosIntegrator
from craftgate.model.autopilot_state import AutopilotState
from craftgate.model.currency import Currency
from craftgate.model.card_association import CardAssociation
from craftgate.model.payment_authentication_type import PaymentAuthenticationType
from craftgate.response.dto.merchant_pos_user import MerchantPosUser

class MerchantPosResponse(object):
    def __init__(
        self,
        id=None,                                       # type: Optional[int]
        status=None,                                   # type: Optional[PosStatus]
        name=None,                                     # type: Optional[str]
        alias=None,                                    # type: Optional[str]
        pos_integrator=None,                           # type: Optional[PosIntegrator]
        hostname=None,                                 # type: Optional[str]
        client_id=None,                                # type: Optional[str]
        pos_currency_code=None,                        # type: Optional[str]
        mode=None,                                     # type: Optional[str]
        path=None,                                     # type: Optional[str]
        port=None,                                     # type: Optional[int]
        posnet_id=None,                                # type: Optional[str]
        terminal_id=None,                              # type: Optional[str]
        threeds_posnet_id=None,                        # type: Optional[str]
        threeds_terminal_id=None,                      # type: Optional[str]
        threeds_key=None,                              # type: Optional[str]
        threeds_path=None,                             # type: Optional[str]
        enable_foreign_card=None,                      # type: Optional[bool]
        enable_installment=None,                       # type: Optional[bool]
        enable_payment_without_cvc=None,               # type: Optional[bool]
        enable_loyalty=None,                           # type: Optional[bool]
        new_integration=None,                          # type: Optional[bool]
        order_number=None,                             # type: Optional[int]
        autopilot_state=None,                          # type: Optional[AutopilotState]
        currency=None,                                 # type: Optional[Currency]
        bank_id=None,                                  # type: Optional[int]
        bank_name=None,                                # type: Optional[str]
        is_pf=None,                                    # type: Optional[bool]
        merchant_pos_users=None,                       # type: Optional[List[MerchantPosUser]]
        supported_card_associations=None,              # type: Optional[List[CardAssociation]]
        enabled_payment_authentication_types=None      # type: Optional[List[PaymentAuthenticationType]]
    ):
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
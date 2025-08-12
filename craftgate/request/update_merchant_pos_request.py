from typing import Optional, List

from craftgate.model.card_association import CardAssociation
from craftgate.model.payment_authentication_type import PaymentAuthenticationType
from craftgate.model.payment_phase import PaymentPhase
from craftgate.request.dto.update_merchant_pos_user import UpdateMerchantPosUser


class UpdateMerchantPosRequest(object):
    def __init__(
        self,
        name=None,                                        # type: Optional[str]
        hostname=None,                                    # type: Optional[str]
        client_id=None,                                   # type: Optional[str]
        mode=None,                                        # type: Optional[str]
        path=None,                                        # type: Optional[str]
        port=None,                                        # type: Optional[int]
        posnet_id=None,                                   # type: Optional[str]
        terminal_id=None,                                 # type: Optional[str]
        threeds_posnet_id=None,                           # type: Optional[str]
        threeds_terminal_id=None,                         # type: Optional[str]
        threeds_key=None,                                 # type: Optional[str]
        threeds_path=None,                                # type: Optional[str]
        enable_foreign_card=None,                         # type: Optional[bool]
        enable_installment=None,                          # type: Optional[bool]
        enable_payment_without_cvc=None,                  # type: Optional[bool]
        enable_loyalty=None,                              # type: Optional[bool]
        new_integration=None,                             # type: Optional[bool]
        order_number=None,                                # type: Optional[int]
        supported_card_associations=None,                 # type: Optional[List[CardAssociation]]
        enabled_payment_authentication_types=None,        # type: Optional[List[PaymentAuthenticationType]]
        merchant_pos_users=None,                          # type: Optional[List[UpdateMerchantPosUser]]
        enabled_payment_phases=None                       # type: Optional[List[PaymentPhase]]
    ):
        self.name = name
        self.hostname = hostname
        self.client_id = client_id
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
        self.supported_card_associations = supported_card_associations
        self.enabled_payment_authentication_types = enabled_payment_authentication_types
        self.merchant_pos_users = merchant_pos_users
        self.enabled_payment_phases = enabled_payment_phases
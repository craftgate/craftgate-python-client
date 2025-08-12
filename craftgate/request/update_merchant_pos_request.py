from typing import List, Optional

from craftgate.model.card_association import CardAssociation
from craftgate.model.payment_authentication_type import PaymentAuthenticationType
from craftgate.model.payment_phase import PaymentPhase
from craftgate.request.dto.update_merchant_pos_user import UpdateMerchantPosUser


class UpdateMerchantPosRequest(object):
    def __init__(
            self,
            name: Optional[str] = None,
            hostname: Optional[str] = None,
            client_id: Optional[str] = None,
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
            supported_card_associations: Optional[List[CardAssociation]] = None,
            enabled_payment_authentication_types: Optional[List[PaymentAuthenticationType]] = None,
            merchant_pos_users: Optional[List[UpdateMerchantPosUser]] = None,
            enabled_payment_phases: Optional[List[PaymentPhase]] = None
    ) -> None:
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

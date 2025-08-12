from typing import Optional, List, Dict
from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.model.payment_method import PaymentMethod
from craftgate.model.payment_phase import PaymentPhase
from craftgate.request.dto.custom_installment import CustomInstallment
from craftgate.request.dto.fraud_check_parameters import FraudCheckParameters
from craftgate.request.dto.payment_item import PaymentItem


class InitCheckoutPaymentRequest(object):
    def __init__(self,
                 price=None,                                    # type: Optional[float]
                 paid_price=None,                               # type: Optional[float]
                 currency=None,                                 # type: Optional[Currency]
                 payment_group=None,                            # type: Optional[PaymentGroup]
                 conversation_id=None,                          # type: Optional[str]
                 external_id=None,                              # type: Optional[str]
                 order_id=None,                                 # type: Optional[str]
                 callback_url=None,                             # type: Optional[str]
                 client_ip=None,                                # type: Optional[str]
                 payment_phase=PaymentPhase.AUTH,               # type: PaymentPhase
                 payment_channel=None,                          # type: Optional[str]
                 enabled_payment_methods=None,                  # type: Optional[List[PaymentMethod]]
                 masterpass_gsm_number=None,                    # type: Optional[str]
                 masterpass_user_id=None,                       # type: Optional[str]
                 card_user_key=None,                            # type: Optional[str]
                 buyer_member_id=None,                          # type: Optional[int]
                 enabled_installments=None,                     # type: Optional[List[int]]
                 always_store_card_after_payment=False,         # type: bool
                 allow_only_stored_cards=False,                 # type: bool
                 allow_only_credit_card=False,                  # type: bool
                 allow_installment_only_commercial_cards=False, # type: bool
                 force_three_ds=False,                          # type: bool
                 force_auth_for_non_credit_cards=False,         # type: bool
                 deposit_payment=False,                         # type: bool
                 ttl=None,                                      # type: Optional[int]
                 custom_installments=None,                      # type: Optional[List[CustomInstallment]]
                 items=None,                                    # type: Optional[List[PaymentItem]]
                 fraud_params=None,                             # type: Optional[FraudCheckParameters]
                 additional_params=None,                        # type: Optional[Dict[str, object]]
                 card_brand_installments=None                   # type: Optional[Dict[str, List[CustomInstallment]]]
                 ):
        self.price = price
        self.paid_price = paid_price
        self.currency = currency
        self.payment_group = payment_group
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.order_id = order_id
        self.callback_url = callback_url
        self.client_ip = client_ip
        self.payment_phase = payment_phase
        self.payment_channel = payment_channel
        self.enabled_payment_methods = enabled_payment_methods
        self.masterpass_gsm_number = masterpass_gsm_number
        self.masterpass_user_id = masterpass_user_id
        self.card_user_key = card_user_key
        self.buyer_member_id = buyer_member_id
        self.enabled_installments = enabled_installments
        self.always_store_card_after_payment = always_store_card_after_payment
        self.allow_only_stored_cards = allow_only_stored_cards
        self.allow_only_credit_card = allow_only_credit_card
        self.allow_installment_only_commercial_cards = allow_installment_only_commercial_cards
        self.force_three_ds = force_three_ds
        self.force_auth_for_non_credit_cards = force_auth_for_non_credit_cards
        self.deposit_payment = deposit_payment
        self.ttl = ttl
        self.custom_installments = custom_installments
        self.items = items
        self.fraud_params = fraud_params
        self.additional_params = additional_params
        self.card_brand_installments = card_brand_installments
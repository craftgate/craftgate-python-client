from typing import Optional, List, Dict
from craftgate.model.currency import Currency
from craftgate.model.payment_group import PaymentGroup
from craftgate.model.payment_phase import PaymentPhase
from craftgate.model.pos_apm_payment_provider import PosApmPaymentProvider
from craftgate.request.dto.fraud_check_parameters import FraudCheckParameters
from craftgate.request.dto.payment_item import PaymentItem
from craftgate.request.dto.pos_apm_installment import PosApmInstallment


class InitPosApmPaymentRequest(object):
    def __init__(
        self,
        price=None,                    # type: Optional[float]
        paid_price=None,                # type: Optional[float]
        pos_alias=None,                 # type: Optional[str]
        currency=None,                   # type: Optional[Currency]
        conversation_id=None,           # type: Optional[str]
        external_id=None,                # type: Optional[str]
        callback_url=None,               # type: Optional[str]
        payment_group=None,              # type: Optional[PaymentGroup]
        payment_phase=PaymentPhase.AUTH, # type: PaymentPhase
        payment_channel=None,            # type: Optional[str]
        buyer_member_id=None,            # type: Optional[int]
        bank_order_id=None,              # type: Optional[str]
        client_ip=None,                  # type: Optional[str]
        items=None,                      # type: Optional[List[PaymentItem]]
        additional_params=None,          # type: Optional[Dict[str, object]]
        installments=None,               # type: Optional[List[PosApmInstallment]]
        payment_provider=None,           # type: Optional[PosApmPaymentProvider]
        fraud_params=None,               # type: Optional[FraudCheckParameters]
        checkout_form_token=None         # type: Optional[str]
    ):
        self.price = price
        self.paid_price = paid_price
        self.pos_alias = pos_alias
        self.currency = currency
        self.conversation_id = conversation_id
        self.external_id = external_id
        self.callback_url = callback_url
        self.payment_group = payment_group
        self.payment_phase = payment_phase
        self.payment_channel = payment_channel
        self.buyer_member_id = buyer_member_id
        self.bank_order_id = bank_order_id
        self.client_ip = client_ip
        self.items = items or []
        self.additional_params = additional_params or {}
        self.installments = installments or []
        self.payment_provider = payment_provider
        self.fraud_params = fraud_params
        self.checkout_form_token = checkout_form_token
from typing import Optional, List
from craftgate.response.dto.bnpl_bank_offer_term import BnplBankOfferTerm

class BnplBankOffer(object):
    def __init__(
        self,
        bank_code=None,                             # type: Optional[str]
        bank_name=None,                             # type: Optional[str]
        bank_icon_url=None,                         # type: Optional[str]
        bank_table_banner_message=None,             # type: Optional[str]
        bank_small_banner_message=None,             # type: Optional[str]
        pre_approved_application_id=None,           # type: Optional[str]
        is_support_non_customer=None,               # type: Optional[bool]
        is_payment_plan_calculated_by_bank=None,    # type: Optional[bool]
        bank_offer_terms=None                       # type: Optional[List[BnplBankOfferTerm]]
    ):
        self.bank_code = bank_code
        self.bank_name = bank_name
        self.bank_icon_url = bank_icon_url
        self.bank_table_banner_message = bank_table_banner_message
        self.bank_small_banner_message = bank_small_banner_message
        self.pre_approved_application_id = pre_approved_application_id
        self.is_support_non_customer = is_support_non_customer
        self.is_payment_plan_calculated_by_bank = is_payment_plan_calculated_by_bank
        self.bank_offer_terms = bank_offer_terms
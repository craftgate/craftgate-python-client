from typing import List, Optional

from craftgate.response.dto.bnpl_bank_offer_term import BnplBankOfferTerm


class BnplBankOffer(object):
    def __init__(
            self,
            bank_code: Optional[str] = None,
            bank_name: Optional[str] = None,
            bank_icon_url: Optional[str] = None,
            bank_table_banner_message: Optional[str] = None,
            bank_small_banner_message: Optional[str] = None,
            pre_approved_application_id: Optional[str] = None,
            is_support_non_customer: Optional[bool] = None,
            is_payment_plan_calculated_by_bank: Optional[bool] = None,
            bank_offer_terms: Optional[List[BnplBankOfferTerm]] = None
    ) -> None:
        self.bank_code = bank_code
        self.bank_name = bank_name
        self.bank_icon_url = bank_icon_url
        self.bank_table_banner_message = bank_table_banner_message
        self.bank_small_banner_message = bank_small_banner_message
        self.pre_approved_application_id = pre_approved_application_id
        self.is_support_non_customer = is_support_non_customer
        self.is_payment_plan_calculated_by_bank = is_payment_plan_calculated_by_bank
        self.bank_offer_terms = bank_offer_terms

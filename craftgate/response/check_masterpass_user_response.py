from typing import Optional


class CheckMasterpassUserResponse(object):
    def __init__(
            self,
            is_eligible_to_use_masterpass: Optional[bool] = None,
            is_any_card_saved_in_customer_program: Optional[bool] = None,
            has_masterpass_account: Optional[bool] = None,
            hash_any_card_saved_in_masterpass_account: Optional[bool] = None,
            is_masterpass_account_linked_with_merchant: Optional[bool] = None,
            is_masterpass_account_locked: Optional[bool] = None,
            is_phone_number_updated_in_another_merchant: Optional[bool] = None,
            account_status: Optional[str] = None
    ) -> None:
        self.is_eligible_to_use_masterpass = is_eligible_to_use_masterpass
        self.is_any_card_saved_in_customer_program = is_any_card_saved_in_customer_program
        self.has_masterpass_account = has_masterpass_account
        self.hash_any_card_saved_in_masterpass_account = hash_any_card_saved_in_masterpass_account
        self.is_masterpass_account_linked_with_merchant = is_masterpass_account_linked_with_merchant
        self.is_masterpass_account_locked = is_masterpass_account_locked
        self.is_phone_number_updated_in_another_merchant = is_phone_number_updated_in_another_merchant
        self.account_status = account_status

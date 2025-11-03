from typing import Optional


class CreateMerchantRequest(object):
    def __init__(
            self,
            name: Optional[str] = None,
            legal_company_title: Optional[str] = None,
            email: Optional[str] = None,
            secret_word: Optional[str] = None,
            website: Optional[str] = None,
            phone_number: Optional[str] = None,
            contact_name: Optional[str] = None,
            contact_surname: Optional[str] = None,
            contact_phone_number: Optional[str] = None
    ) -> None:
        self.name = name
        self.legal_company_title = legal_company_title
        self.email = email
        self.secret_word = secret_word
        self.website = website
        self.phone_number = phone_number
        self.contact_name = contact_name
        self.contact_surname = contact_surname
        self.contact_phone_number = contact_phone_number

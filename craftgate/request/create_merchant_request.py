class CreateMerchantRequest(object):
    def __init__(
            self,
            name=None,  # type: str
            legal_company_title=None,  # type: str
            email=None,  # type: str
            secret_word=None,  # type: str
            website=None,  # type: str
            phone_number=None,  # type: str
            contact_name=None,  # type: str
            contact_surname=None,  # type: str
            contact_phone_number=None  # type: str
    ):
        self.name = name
        self.legal_company_title = legal_company_title
        self.email = email
        self.secret_word = secret_word
        self.website = website
        self.phone_number = phone_number
        self.contact_name = contact_name
        self.contact_surname = contact_surname
        self.contact_phone_number = contact_phone_number

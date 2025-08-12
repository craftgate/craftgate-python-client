class ApplePayMerchantSessionCreateRequest(object):
    def __init__(self,
                 merchant_identifier,  # type: str
                 display_name,  # type: str
                 initiative,  # type: str
                 initiative_context,  # type: str
                 validation_url  # type: str
                 ):
        self.merchant_identifier = merchant_identifier  # type: str
        self.display_name = display_name  # type: str
        self.initiative = initiative  # type: str
        self.initiative_context = initiative_context  # type: str
        self.validation_url = validation_url  # type: str

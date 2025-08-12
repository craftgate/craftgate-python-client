class ApplePayMerchantSessionCreateRequest(object):
    def __init__(
            self,
            merchant_identifier: str,
            display_name: str,
            initiative: str,
            initiative_context: str,
            validation_url: str
    ) -> None:
        self.merchant_identifier = merchant_identifier
        self.display_name = display_name
        self.initiative = initiative
        self.initiative_context = initiative_context
        self.validation_url = validation_url

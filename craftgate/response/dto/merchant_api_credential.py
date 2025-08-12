class MerchantApiCredential(object):
    def __init__(self, name=None, api_key=None, secret_key=None):
        # type: (str, str, str) -> None
        self.name = name
        self.api_key = api_key
        self.secret_key = secret_key
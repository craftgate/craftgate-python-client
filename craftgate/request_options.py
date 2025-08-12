from typing import Optional


class RequestOptions:
    def __init__(self, api_key: str, secret_key: str, base_url: str, language: Optional[str] = None) -> None:
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = base_url
        self.language = language

import random
import string
from typing import Any, Dict, Optional

from requests import __version__

from craftgate.request_options import RequestOptions
from craftgate.utils.hash_generator import HashGenerator


class BaseAdapter:
    API_VERSION_HEADER_VALUE = "v1"
    CLIENT_NAME = "craftgate-python-client"
    API_KEY_HEADER_NAME = "x-api-key"
    RANDOM_HEADER_NAME = "x-rnd-key"
    AUTH_VERSION_HEADER_NAME = "x-auth-version"
    CLIENT_VERSION_HEADER_NAME = "x-client-version"
    SIGNATURE_HEADER_NAME = "x-signature"
    LANGUAGE_HEADER_NAME = "lang"
    RANDOM_STRING_LENGTH = 8
    RANDOM_CHARS = string.ascii_letters + string.digits

    def __init__(self, request_options: RequestOptions) -> None:
        self.request_options = request_options

    def _create_headers(
            self,
            request_body: Optional[Any],
            path: str,
            custom_options: Optional[RequestOptions] = None
    ) -> Dict[str, str]:
        options = custom_options or self.request_options
        random_key = self._generate_random_string(self.RANDOM_STRING_LENGTH)

        signature = HashGenerator.generate_hash(
            base_url=options.base_url,
            api_key=options.api_key,
            secret_key=options.secret_key,
            random_string=random_key,
            request=request_body,
            path=path,
        )

        headers = {
            self.API_KEY_HEADER_NAME: options.api_key,
            self.RANDOM_HEADER_NAME: random_key,
            self.AUTH_VERSION_HEADER_NAME: self.API_VERSION_HEADER_VALUE,
            self.CLIENT_VERSION_HEADER_NAME: self.CLIENT_NAME + ":" + __version__,
            self.SIGNATURE_HEADER_NAME: signature,
        }

        if options.language:
            headers[self.LANGUAGE_HEADER_NAME] = options.language

        return headers

    def _generate_random_string(self, length: int) -> str:
        return ''.join(random.choice(self.RANDOM_CHARS) for _ in range(length))

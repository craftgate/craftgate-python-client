import uuid
from typing import Dict, Optional

from _version import VERSION
from craftgate.request.common.base_request import BaseRequest
from craftgate.request.common.header_options import HeaderOptions
from craftgate.request_options import RequestOptions
from craftgate.utils.hash_generator import HashGenerator

class BaseAdapter:
    API_VERSION_HEADER_VALUE = "v1"
    CLIENT_NAME = "craftgate-python-client"
    CLIENT_VERSION = VERSION
    API_KEY_HEADER_NAME = "x-api-key"
    RANDOM_HEADER_NAME = "x-rnd-key"
    AUTH_VERSION_HEADER_NAME = "x-auth-version"
    CLIENT_VERSION_HEADER_NAME = "x-client-version"
    SIGNATURE_HEADER_NAME = "x-signature"
    LANGUAGE_HEADER_NAME = "lang"
    IDEMPOTENCY_KEY_HEADER_NAME = "x-idempotency-key"

    def __init__(self, request_options: RequestOptions) -> None:
        self.request_options = request_options

    def _create_headers(
            self,
            request_body: Optional[BaseRequest],
            path: str,
            custom_options: Optional[RequestOptions] = None
    ) -> Dict[str, str]:
        return self._create_http_headers(
            request_body, path, custom_options, self._header_options_of(request_body))

    def _create_headers_without_body(
            self,
            request: Optional[BaseRequest],
            path: str,
            custom_options: Optional[RequestOptions] = None
    ) -> Dict[str, str]:
        return self._create_http_headers(
            None, path, custom_options, self._header_options_of(request))

    def _create_http_headers(
            self,
            request_body: Optional[BaseRequest],
            path: str,
            custom_options: Optional[RequestOptions],
            header_options: Optional[HeaderOptions]
    ) -> Dict[str, str]:
        options = custom_options or self.request_options
        random_key = self._generate_random_string()

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
            self.CLIENT_VERSION_HEADER_NAME: self.CLIENT_NAME + ":" + self.CLIENT_VERSION,
            self.SIGNATURE_HEADER_NAME: signature,
        }

        if options.language:
            headers[self.LANGUAGE_HEADER_NAME] = options.language

        self._apply_request_scoped_headers(headers, header_options)

        return headers

    @staticmethod
    def _header_options_of(request: Optional[BaseRequest]) -> Optional[HeaderOptions]:
        return request.header_options if request is not None else None

    def _apply_request_scoped_headers(
            self, headers: Dict[str, str], header_options: Optional[HeaderOptions]
    ) -> None:
        if header_options is None:
            return

        if header_options.idempotency_key is not None:
            headers[self.IDEMPOTENCY_KEY_HEADER_NAME] = header_options.idempotency_key

    def _generate_random_string(self) -> str:
        return str(uuid.uuid4())

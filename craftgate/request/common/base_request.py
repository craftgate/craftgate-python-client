from typing import Optional, TypeVar

from craftgate.request.common.header_options import HeaderOptions

T = TypeVar("T", bound="BaseRequest")

class BaseRequest(object):

    _idempotency_key: Optional[str] = None

    @property
    def idempotency_key(self) -> Optional[str]:
        return self._idempotency_key

    @idempotency_key.setter
    def idempotency_key(self, value: Optional[str]) -> None:
        self._idempotency_key = value

    def to_header_options(self) -> HeaderOptions:
        return HeaderOptions(idempotency_key=self._idempotency_key)

    def with_idempotency_key(self: T, value: Optional[str]) -> T:
        self._idempotency_key = value
        return self

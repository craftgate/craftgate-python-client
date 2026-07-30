from typing import Optional, TypeVar

T = TypeVar("T", bound="BaseRequest")


class BaseRequest(object):
    """Base class for request objects sent to the Craftgate API.

    The backing attribute is underscore-prefixed, which is what keeps it out of the
    JSON body, the request signature and query parameters.
    """

    _idempotency_key: Optional[str] = None

    @property
    def idempotency_key(self) -> Optional[str]:
        """Optional key, sent as the ``x-idempotency-key`` header so a mutating call can
        be safely retried."""
        return self._idempotency_key

    @idempotency_key.setter
    def idempotency_key(self, value: Optional[str]) -> None:
        self._idempotency_key = value

    def with_idempotency_key(self: T, value: Optional[str]) -> T:
        """Sets the idempotency key and returns the request, for inline use.

        Returns the concrete type so the result stays assignable under a type checker.
        """
        self._idempotency_key = value
        return self

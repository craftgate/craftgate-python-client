from typing import Optional, TypeVar

from craftgate.request.common.header_options import HeaderOptions

T = TypeVar("T", bound="BaseRequest")


class BaseRequest(object):

    header_options: Optional[HeaderOptions] = None

    def with_header_options(self: T, header_options: Optional[HeaderOptions]) -> T:
        self.header_options = header_options
        return self

from craftgate.response.common.list_response import ListResponse
from craftgate.response.product_response import ProductResponse


class ProductListResponse(ListResponse[ProductResponse]):
    item_type = ProductResponse

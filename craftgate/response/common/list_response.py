class ListResponse(object):
    def __init__(self, items=None, page=None, size=None, total_size=None):
        self.items = items if items is not None else []
        self.page = page
        self.size = size
        self.total_size = total_size

    @classmethod
    def from_dict(cls, data):
        return cls(
            items=data.get("items", []),
            page=data.get("page"),
            size=data.get("size"),
            total_size=data.get("totalSize")
        )

    def to_dict(self):
        return {
            "items": self.items,
            "page": self.page,
            "size": self.size,
            "totalSize": self.total_size
        }

    def __repr__(self):
        return "ListResponse(items=%r, page=%r, size=%r, total_size=%r)" % (
            self.items, self.page, self.size, self.total_size)

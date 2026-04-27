from .pagination import paginate
from .filters import apply_filter
from .sorting import apply_sort

class TableBuilder:

    def __init__(self, data):
        self.data = data

    def search(self, search: str = None):
        self.data = apply_filter(self.data, search)
        return self

    def sort(self, sort_by: str = None, sort_order: str = "asc"):
        self.data = apply_sort(self.data, sort_by, sort_order)
        return self

    def paginate(self, page: int = 1, limit: int = 10):
        self.data = paginate(self.data, page, limit)
        return self

    def build(self):
        return self.data
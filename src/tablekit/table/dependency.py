from fastapi import Request
from .schema import TableParams


def get_table_params(request: Request) -> TableParams:
    q = request.query_params

    return TableParams(
        page=int(q.get("page", 1)),
        limit=int(q.get("limit", 10)),
        search=q.get("search"),
        sort_by=q.get("sort_by"),
        sort_order=q.get("sort_order", "asc"),
    )
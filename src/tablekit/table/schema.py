from pydantic import BaseModel
from typing import Optional

class TableParams(BaseModel):
    page: int = 1
    limit: int = 10
    search: Optional[str] = None
    sort_by: Optional[str] = None
    sort_order: Optional[str] = "asc"

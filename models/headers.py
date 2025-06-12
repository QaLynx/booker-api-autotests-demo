from pydantic import BaseModel
from typing import Optional

class Headers(BaseModel):
    Accept: Optional[str] = None
    Content_Type: Optional[str] = None
    Authorization: Optional[str] = None
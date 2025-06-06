from typing import Union

from pydantic import BaseModel

class AuthRequest(BaseModel):
    username: Union[str, int]
    password: Union[str, int]
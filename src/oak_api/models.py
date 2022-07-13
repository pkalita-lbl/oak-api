from typing import Union
from pydantic import BaseModel


class OntologyClass(BaseModel):
    id: str
    label: str
    definition: Union[str, None] = None

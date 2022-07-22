from typing import Union

from pydantic import BaseModel


class OntologyClass(BaseModel):
    id: str
    label: Union[str, None] = None
    definition: Union[str, None] = None

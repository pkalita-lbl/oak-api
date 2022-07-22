from typing import Generic, List, TypeVar, Union

from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")


class OntologyClass(BaseModel):
    id: str
    label: Union[str, None] = None
    definition: Union[str, None] = None


class PaginationInfo(BaseModel):
    previous: Union[str, None] = None
    next: Union[str, None] = None


class Page(GenericModel, Generic[T]):
    data: List[T]
    pagination: PaginationInfo

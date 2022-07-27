from typing import List, Union

from fastapi import APIRouter, Depends

from ..depends import curies_list, predicates
from ..models import OntologyClass, Page, PaginationParams
from ..oak_service import OakImpl, ancestors, descendants, get_classes_from_curies
from ..settings import get_oak_implementation
from ..utils import paginate

router = APIRouter(prefix="/classes", tags=["classes"])


@router.get("/", response_model=List[OntologyClass], summary="Get multiple classes")
def get_classes(
    curies: List[str] = Depends(curies_list), impl: OakImpl = Depends(get_oak_implementation)
):
    return get_classes_from_curies(impl, curies)


@router.get("/{curie}", response_model=OntologyClass, summary="Get class by CURIE")
def get_class(curie: str, impl: OakImpl = Depends(get_oak_implementation)):
    return next(iter(get_classes_from_curies(impl, [curie])))


@router.get(
    "/{curie}/ancestors",
    response_model=Page[OntologyClass],
    summary="Get class ancestors",
)
def get_ancestors(
    curie: str,
    predicates: Union[List[str], None] = Depends(predicates),
    pagination: PaginationParams = Depends(),
    impl: OakImpl = Depends(get_oak_implementation),
):
    results = ancestors(impl, curie, predicates)
    return paginate(results, **pagination.dict())


@router.get(
    "/{curie}/descendants",
    response_model=Page[OntologyClass],
    summary="Get class descendants",
)
def get_descendants(
    curie: str,
    predicates: Union[List[str], None] = Depends(predicates),
    pagination: PaginationParams = Depends(),
    impl: OakImpl = Depends(get_oak_implementation),
):
    results = descendants(impl, curie, predicates)
    return paginate(results, **pagination.dict())

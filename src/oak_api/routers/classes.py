from fastapi import APIRouter, Depends

from .. import ontology
from ..depends import pagination, predicates
from ..models import OntologyClass, Page
from ..utils import paginate

router = APIRouter(prefix="/classes", tags=["classes"])


@router.get("/{curie}", response_model=OntologyClass, summary="Get class by CURIE")
def get_class(curie: str):
    return next(iter(ontology.get_classes_from_curies([curie])))


@router.get(
    "/{curie}/ancestors",
    response_model=Page[OntologyClass],
    summary="Get class ancestors",
)
def get_ancestors(curie: str, predicates=Depends(predicates), pagination=Depends(pagination)):
    ancestors = ontology.ancestors(curie, predicates)
    return paginate(ancestors, **pagination)


@router.get(
    "/{curie}/descendants",
    response_model=Page[OntologyClass],
    summary="Get class descendants",
)
def get_descendants(curie: str, predicates=Depends(predicates), pagination=Depends(pagination)):
    descendants = ontology.descendants(curie, predicates)
    return paginate(descendants, **pagination)

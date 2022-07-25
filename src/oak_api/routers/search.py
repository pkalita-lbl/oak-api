from fastapi import APIRouter, Depends

from .. import ontology
from ..depends import pagination
from ..models import OntologyClass, Page
from ..utils import paginate

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/", response_model=Page[OntologyClass], summary="Search for classes")
def do_search(q: str, pagination=Depends(pagination)):
    results = ontology.search(q)
    return paginate(results, **pagination)

from fastapi import APIRouter, Depends

from ..models import OntologyClass, Page, PaginationParams
from ..oak_service import OakImpl, search
from ..settings import get_oak_implementation
from ..utils import paginate

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/", response_model=Page[OntologyClass], summary="Search for classes")
def do_search(
    q: str,
    pagination: PaginationParams = Depends(),
    impl: OakImpl = Depends(get_oak_implementation),
):
    results = search(impl, q)
    return paginate(results, **pagination.dict())

from typing import List, Union

from fastapi import HTTPException, Query, Request
from oaklib.datamodels.vocabulary import (
    DEVELOPS_FROM,
    EQUIVALENT_CLASS,
    IS_A,
    PART_OF,
    RDF_TYPE,
)

PREDICATE_MAP = {
    "is_a": IS_A,
    "part_of": PART_OF,
    "develops_from": DEVELOPS_FROM,
    "rdf_type": RDF_TYPE,
    "equivalent_class": EQUIVALENT_CLASS,
}


async def curies_list(curies: str) -> List[str]:
    parsed = curies.split(",")
    if len(parsed) > 50:
        raise HTTPException(status_code=422, detail="Maximum of 50 CURIEs allowed")
    return parsed


async def predicates(predicate: Union[list[str], None] = Query(default=None)):
    if predicate is None:
        return predicate
    return [PREDICATE_MAP[p] if p in PREDICATE_MAP else p for p in predicate]


async def pagination(request: Request, limit: int = 20, page: int = Query(default=1, ge=1)):
    return {"limit": limit, "page": page, "request": request}

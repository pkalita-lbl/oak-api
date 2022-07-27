from typing import Any, Dict, List, Union

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


async def predicates(
    predicate: Union[List[str], None] = Query(default=None)
) -> Union[List[str], None]:
    if predicate is None:
        return predicate
    return [PREDICATE_MAP[p] if p in PREDICATE_MAP else p for p in predicate]

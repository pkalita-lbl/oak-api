from typing import Iterable, List

from oaklib.datamodels.search import SearchConfiguration
from oaklib.implementations import SqlImplementation
from oaklib.selector import get_implementation_from_shorthand

from .models import OntologyClass
from .settings import settings

_implementation: SqlImplementation = get_implementation_from_shorthand(settings["implementation"])  # type: ignore


def get_classes_from_curies(curies: Iterable[str]) -> Iterable[OntologyClass]:
    labeled = _implementation.labels(curies)
    return (
        OntologyClass(
            id=curie,
            label=label,
            definition=_implementation.definition(curie),
        )
        for curie, label in labeled
    )


def ancestors(curie: str, predicates: List[str]) -> Iterable[OntologyClass]:
    ancestors = _implementation.ancestors(curie, predicates)
    return get_classes_from_curies(ancestors)


def descendants(curie: str, predicates: List[str]) -> Iterable[OntologyClass]:
    descendants = _implementation.descendants(curie, predicates)
    return get_classes_from_curies(descendants)


def search(q: str) -> Iterable[OntologyClass]:
    config = SearchConfiguration(is_partial=True)
    results = _implementation.basic_search(q, config)
    return get_classes_from_curies(results)

from typing import Iterable, List, Union

from oaklib.datamodels.search import SearchConfiguration
from oaklib.interfaces.obograph_interface import OboGraphInterface
from oaklib.interfaces.search_interface import SearchInterface

from .models import OntologyClass


# just for type checking
class OakImpl(SearchInterface, OboGraphInterface):
    pass


def get_classes_from_curies(impl: OakImpl, curies: Iterable[str]) -> Iterable[OntologyClass]:
    labeled = impl.labels(curies)
    return (
        OntologyClass(
            id=curie,
            label=label,
            definition=impl.definition(curie),
        )
        for curie, label in labeled
    )


def ancestors(
    impl: OakImpl, curie: str, predicates: Union[List[str], None]
) -> Iterable[OntologyClass]:
    ancestors = impl.ancestors(curie, predicates)  # type: ignore
    return get_classes_from_curies(impl, ancestors)


def descendants(
    impl: OakImpl, curie: str, predicates: Union[List[str], None]
) -> Iterable[OntologyClass]:
    descendants = impl.descendants(curie, predicates)  # type: ignore
    return get_classes_from_curies(impl, descendants)


def search(impl: OakImpl, q: str) -> Iterable[OntologyClass]:
    config = SearchConfiguration(is_partial=True)
    results = impl.basic_search(q, config)
    return get_classes_from_curies(impl, results)

from typing import Iterable
from src.oak_api.models import OntologyClass

from src.oak_api.ontology import implementation


def get_classes_from_curies(curies: Iterable[str]) -> Iterable[OntologyClass]:
    labeled = implementation.labels(curies)
    return [
        OntologyClass(
            id=curie,
            label=label,
            definition=implementation.definition(curie),
        )
        for curie, label in labeled
    ]

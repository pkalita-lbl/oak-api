from typing import Iterable

from .models import OntologyClass
from .ontology import implementation


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

from typing import Iterable
from src.oak_api.models import OntologyClass

from src.oak_api.ontology import implementation


def get_classes_from_curies(curies: Iterable[str]) -> Iterable[OntologyClass]:
    labeled = implementation.get_labels_for_curies(curies)
    return [
        OntologyClass(
            id=curie,
            label=label,
            definition=implementation.get_definition_by_curie(curie),
        )
        for curie, label in labeled
    ]

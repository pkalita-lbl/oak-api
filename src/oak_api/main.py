import itertools
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from oaklib.datamodels.search import SearchConfiguration
from src.oak_api.models import OntologyClass
from src.oak_api.utils import get_classes_from_curies

from src.oak_api.ontology import implementation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/search", response_model=List[OntologyClass], summary="Search for classes")
def do_search(q: str):
    config = SearchConfiguration(is_partial=True)
    curies = implementation.basic_search(q, config)
    return get_classes_from_curies(curies)


@app.get("/class/{curie}", response_model=OntologyClass, summary="Get class by CURIE")
def get_class(curie: str):
    return itertools.islice(get_classes_from_curies(curie), 1)


@app.get(
    "/class/{curie}/ancestors",
    response_model=List[OntologyClass],
    summary="Get class ancestors",
)
def get_ancestors(curie: str):
    ancestors = implementation.ancestors(curie)
    return get_classes_from_curies(ancestors)


@app.get(
    "/class/{curie}/descendants",
    response_model=List[OntologyClass],
    summary="Get class descendants",
)
def get_descendants(curie: str):
    descendants = implementation.descendants(curie)
    return get_classes_from_curies(descendants)

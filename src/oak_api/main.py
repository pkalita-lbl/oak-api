from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from oaklib.datamodels.search import SearchConfiguration

from .depends import pagination, predicates
from .models import OntologyClass, Page
from .ontology import implementation
from .utils import get_classes_from_curies, paginate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/search", response_model=Page[OntologyClass], summary="Search for classes")
def do_search(q: str, pagination=Depends(pagination)):
    config = SearchConfiguration(is_partial=True)
    curies = implementation.basic_search(q, config)
    return paginate(get_classes_from_curies(curies), **pagination)


@app.get("/class/{curie}", response_model=OntologyClass, summary="Get class by CURIE")
def get_class(curie: str):
    return next(iter(get_classes_from_curies([curie])))


@app.get(
    "/class/{curie}/ancestors",
    response_model=Page[OntologyClass],
    summary="Get class ancestors",
)
def get_ancestors(curie: str, predicates=Depends(predicates), pagination=Depends(pagination)):
    ancestors = implementation.ancestors(curie, predicates)
    return paginate(get_classes_from_curies(ancestors), **pagination)


@app.get(
    "/class/{curie}/descendants",
    response_model=Page[OntologyClass],
    summary="Get class descendants",
)
def get_descendants(curie: str, predicates=Depends(predicates), pagination=Depends(pagination)):
    descendants = implementation.descendants(curie, predicates)
    return paginate(get_classes_from_curies(descendants), **pagination)

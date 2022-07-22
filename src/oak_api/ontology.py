from oaklib.implementations import SqlImplementation
from oaklib.selector import get_implementation_from_shorthand

from .settings import settings

implementation: SqlImplementation = get_implementation_from_shorthand(settings["implementation"])  # type: ignore

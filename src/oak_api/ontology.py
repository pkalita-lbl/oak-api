from oaklib.selector import get_implementation_from_shorthand
from oaklib.implementations import SqlImplementation

from src.oak_api.settings import settings

implementation: SqlImplementation = get_implementation_from_shorthand(settings["implementation"])  # type: ignore

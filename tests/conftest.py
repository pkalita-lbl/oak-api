from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from src.oak_api.main import create_app
from src.oak_api.oak_service import OakImpl
from src.oak_api.settings import get_oak_implementation


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def mock_oak_implementation() -> OakImpl:
    mock = Mock(OakImpl)
    mock.basic_search.return_value = ["a", "b", "c"]
    mock.labels.return_value = [("a", "a label"), ("b", "b label"), ("c", "c label")]
    mock.definition.return_value = "mock definition"
    mock.ancestors.return_value = ["ANCESTOR:01", "ANCESTOR:02", "ANCESTOR:03"]
    mock.descendants.return_value = ["DESCENDANT:01", "DESCENDANT:02", "DESCENDANT:03"]
    return mock


@pytest.fixture
def client(app, mock_oak_implementation) -> TestClient:
    def override_implementation():
        return mock_oak_implementation

    app.dependency_overrides[get_oak_implementation] = override_implementation
    return TestClient(app)

from fastapi.testclient import TestClient
from oaklib.datamodels.search import SearchConfiguration

from src.oak_api.oak_service import OakImpl


def test_search(client: TestClient, mock_oak_implementation: OakImpl):
    query_term = "kinase"
    response = client.get("/search", params={"q": query_term})
    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert "pagination" in body
    assert body["data"][0] == {"id": "a", "label": "a label", "definition": "mock definition"}
    mock_oak_implementation.basic_search.assert_called_with(
        query_term, SearchConfiguration(is_partial=True)
    )

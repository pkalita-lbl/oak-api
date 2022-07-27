from fastapi.testclient import TestClient

from src.oak_api.settings import OakImpl


def test_get_single_class(client: TestClient, mock_oak_implementation: OakImpl):
    curie = "TEST:000001"
    response = client.get(f"/classes/{curie}")
    assert response.status_code == 200
    body = response.json()
    assert body == {"id": "a", "label": "a label", "definition": "mock definition"}
    mock_oak_implementation.labels.assert_called_with([curie])


def test_get_multiple_classes(client: TestClient, mock_oak_implementation: OakImpl):
    curies = ["TEST:000002", "TEST:000003", "TEST:000004"]
    response = client.get("/classes/", params={"curies": ",".join(curies)})
    assert response.status_code == 200
    body = response.json()
    assert body[0] == {"id": "a", "label": "a label", "definition": "mock definition"}
    mock_oak_implementation.labels.assert_called_with(curies)


def test_get_multiple_too_many_curies(client: TestClient):
    curies = [f"TEST:{num}" for num in range(100)]
    response = client.get("/classes/", params={"curies": ",".join(curies)})
    assert response.status_code == 422


def test_get_ancestors(client: TestClient, mock_oak_implementation: OakImpl):
    curie = "TEST:000001"
    response = client.get(f"/classes/{curie}/ancestors")
    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert "pagination" in body
    assert body["data"][0] == {"id": "a", "label": "a label", "definition": "mock definition"}
    mock_oak_implementation.ancestors.assert_called_with(curie, None)
    mock_oak_implementation.labels.assert_called_with(
        ["ANCESTOR:01", "ANCESTOR:02", "ANCESTOR:03"]
    )


def test_get_ancestors_with_predicate(client: TestClient, mock_oak_implementation: OakImpl):
    curie = "TEST:000001"
    predicate = "PRED:0000001"
    response = client.get(f"/classes/{curie}/ancestors", params={"predicate": predicate})
    assert response.status_code == 200
    mock_oak_implementation.ancestors.assert_called_with(curie, [predicate])
    mock_oak_implementation.labels.assert_called_with(
        ["ANCESTOR:01", "ANCESTOR:02", "ANCESTOR:03"]
    )


def test_get_descendants(client: TestClient, mock_oak_implementation: OakImpl):
    curie = "TEST:000001"
    response = client.get(f"/classes/{curie}/descendants")
    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert "pagination" in body
    assert body["data"][0] == {"id": "a", "label": "a label", "definition": "mock definition"}
    mock_oak_implementation.descendants.assert_called_with(curie, None)
    mock_oak_implementation.labels.assert_called_with(
        ["DESCENDANT:01", "DESCENDANT:02", "DESCENDANT:03"]
    )


def test_get_descendants_with_predicate(client: TestClient, mock_oak_implementation: OakImpl):
    curie = "TEST:000001"
    predicate = "PRED:0000010"
    response = client.get(f"/classes/{curie}/descendants", params={"predicate": predicate})
    assert response.status_code == 200
    mock_oak_implementation.descendants.assert_called_with(curie, [predicate])
    mock_oak_implementation.labels.assert_called_with(
        ["DESCENDANT:01", "DESCENDANT:02", "DESCENDANT:03"]
    )

from unittest.mock import patch

import pytest

from src.oak_api.utils import paginate


@pytest.fixture
def mock_request():
    def mock_include_query_params(**kwargs):
        return kwargs["page"]

    with patch("fastapi.Request") as request:
        request.url.include_query_params.side_effect = mock_include_query_params
        yield request


def test_paginate_first_page_of_many(mock_request):
    items = range(100)
    page = paginate(items, 1, 5, mock_request)
    assert page.data == list(range(5))
    assert page.pagination.previous is None
    assert page.pagination.next == "2"


def test_paginate_first_page_of_one(mock_request):
    items = range(18)
    page = paginate(items, 1, 20, mock_request)
    assert page.data == list(items)
    assert page.pagination.previous is None
    assert page.pagination.next is None


def test_paginate_last_page_of_many(mock_request):
    items = range(75)
    page = paginate(items, 4, 20, mock_request)
    assert page.data == list(range(60, 75))
    assert page.pagination.previous == "3"
    assert page.pagination.next is None


def test_paginate_middle_page(mock_request):
    items = range(45)
    page = paginate(items, 2, 12, mock_request)
    assert page.data == list(range(12, 24))
    assert page.pagination.previous == "1"
    assert page.pagination.next == "3"

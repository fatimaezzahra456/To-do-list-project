import pytest
from src.filters import filter_by_status, search_tasks

TASKS = [
    {"id": 1, "title": "Buy milk", "done": True},
    {"id": 2, "title": "Write report", "done": False},
]


def test_filter_by_status_pending():
    assert [t["id"] for t in filter_by_status(TASKS, False)] == [2]


def test_search_is_case_insensitive():
    assert len(search_tasks(TASKS, "MILK")) == 1


def test_search_empty_keyword_returns_all():
    assert len(search_tasks(TASKS, "")) == 2
def test_search_non_string_keyword_raises():
    with pytest.raises(TypeError):
        search_tasks(TASKS, 123)
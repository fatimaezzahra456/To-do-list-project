import pytest
from src.tasks import add_task, complete_task


def test_add_task_normal():
    tasks = []
    task = add_task(tasks, "Buy milk")
    assert task["id"] == 1
    assert task["title"] == "Buy milk"
    assert task["done"] is False
    assert len(tasks) == 1


def test_add_task_empty_title_raises():
    with pytest.raises(ValueError):
        add_task([], "   ")


def test_complete_task_unknown_id_raises():
    with pytest.raises(KeyError):
        complete_task([], 99)
        
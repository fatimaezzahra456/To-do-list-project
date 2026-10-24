from src.stats import completion_percentage, count_pending


def test_completion_percentage_half():
    tasks = [{"done": True}, {"done": False}]
    assert completion_percentage(tasks) == 50.0


def test_completion_percentage_empty_list():
    assert completion_percentage([]) == 0.0


def test_count_pending():
    tasks = [{"done": False}, {"done": True}]
    assert count_pending(tasks) == 1
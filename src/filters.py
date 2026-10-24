def filter_by_status(tasks, done):
    return [t for t in tasks if t["done"] == done]


def search_tasks(tasks, keyword):
    if keyword is None:
        return list(tasks)
    if not isinstance(keyword, str):
        raise TypeError("keyword must be a string")
    if not keyword.strip():
        return list(tasks)
    k = keyword.strip().lower()
    return [t for t in tasks if k in t["title"].lower()]
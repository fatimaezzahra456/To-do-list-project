def filter_by_status(tasks, done):
    return [t for t in tasks if t["done"] == done]


def search_tasks(tasks, keyword):
    if not keyword or not keyword.strip():
        return list(tasks)
    k = keyword.strip().lower()
    return [t for t in tasks if k in t["title"].lower()]
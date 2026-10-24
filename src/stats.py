def completion_percentage(tasks):
    if not tasks:
        return 0.0

    done = sum(1 for t in tasks if t["done"])
    return round(100 * done / len(tasks), 1)


def count_pending(tasks):
    return sum(1 for t in tasks if not t["done"])
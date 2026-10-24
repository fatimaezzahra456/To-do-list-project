def add_task(tasks, title):
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Title cannot be empty")
    task = {"id": len(tasks) + 1, "title": title.strip(), "done": False}
    tasks.append(task)
    return task


def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    raise KeyError(f"Task {task_id} not found")
from task_manager import database


def get_tasks() -> list[dict]:
    return database.read()


def get_last_task_id():
    try:
        return database.read()[-1]["id"]
    except (KeyError, IndexError):
        return 0


def get_task_by_id(id_):
    tasks = get_tasks()
    for task in tasks:
        if task["id"] == id_:
            return task
    raise ValueError(f"Task with id {id_} not found")


def create_task(name: str, completed=False):
    if not isinstance(name, str):
        raise TypeError("Task name must be a string")

    if len(name) < 3:
        raise ValueError("Task name must have at least 3 characters")

    tasks = get_tasks()
    new_task = {
        "id": get_last_task_id() + 1,
        "name": name,
        "completed": completed,
    }
    tasks.append(new_task)
    database.save(tasks)


def complete_task(id_):
    tasks = get_tasks()
    for task in tasks:
        if task["id"] == id_:
            task["complete"] = True
            return database.save(tasks)
    raise ValueError(f"Task with id {id_} not found")


def delete_task(id_):
    tasks = get_tasks()
    new_tasks = [task for task in tasks if tasks["id"] != id_]
    if len(tasks) == len(new_tasks):
        raise ValueError(f"Task with id {id_} not found")
    database.save(new_tasks)

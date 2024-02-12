import json

from task_manager.constants import DATABASE_PATH


def save(content: list):
    """Saves the content to the database file

    Parameters
    __________
    content: list
        Content to be saved to the database file
    """
    if not isinstance(content, list):
        raise TypeError("Content must be a list")

    with open(DATABASE_PATH, "w") as file:
        file.write(json.dumps(content))


def read() -> list[dict]:
    """Reads and returns the content as a list of dictionaries

    Returns
    _______
    list[dict]
        Content of the database file as a list of dictionaries.
    """
    try:
        with open(DATABASE_PATH, "r") as file:
            content = file.read()
    except FileNotFoundError:
        return []

    if content.strip() == "":
        return []

    list_value = json.loads(content)

    return list_value

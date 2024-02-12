from task_manager import database


def test_read_database_is_empty_at_start():
    db_content = database.read()
    assert db_content == []

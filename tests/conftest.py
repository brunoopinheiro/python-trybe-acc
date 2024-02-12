import pytest


@pytest.fixture(autouse=True)
def patch_db_path(tmp_path, monkeypatch):
    mock_db_path = tmp_path / "database.json"
    mock_db_path.touch()
    monkeypatch.setattr("task_manager.database.DATABASE_PATH", mock_db_path)

from unittest.mock import patch
from task_manager import cli, services


def test_complete_task_should_call_services_complete_task(capsys, faker):
    fake_name = faker.sentence()
    services.create_task(fake_name)  # id = 1

    with patch("builtins.input", side_effect=["1"]):
        cli.complete_task()

    captured = capsys.readouterr()
    assert captured.out == "> Tarefa completada com sucesso!\n"

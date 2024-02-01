# Basta receber capsys como parâmetro no teste
# o pytest entende a fixture automaticamente
def test_print_to_stdout(capsys):
    print("Hello, World!")
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"


def test_error_to_stderr(capsys):
    import sys

    sys.stderr.write("Error message\n")
    captured = capsys.readouterr()
    assert captured.err == "Error message\n"


def my_function():
    return f"Você digitou {input('Digite algo: ')}!"


def test_my_function(monkeypatch):
    # Input recebe um parametro que mock_input não usa
    def mock_input(_):
        return "Python"

    # Trocamos a input do sistema pela mock_input
    monkeypatch.setattr("builtins.input", mock_input)
    output = my_function()

    assert output == "Você digitou Python!"

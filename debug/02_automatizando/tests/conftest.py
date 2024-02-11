import pytest


# Para mudar o escopo,
# basta passar o escopo desejado como argumento
# para o parâmetro scope do decorador pytest.fixture,
# por exemplo @pytest.fixture(scope="module").
@pytest.fixture
def my_list():
    return [1, 2, 3]


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: marks tests as slow")

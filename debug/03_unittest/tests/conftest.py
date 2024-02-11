import pytest


@pytest.fixture(scope="session", autouse=True)
def faker_seed():
    return "Trybe"


@pytest.fixture(scope="session", autouse=True)
# def faker_locale():
#     return "pt_BR"
def faker_session_locale():
    return ["pt_BR"]

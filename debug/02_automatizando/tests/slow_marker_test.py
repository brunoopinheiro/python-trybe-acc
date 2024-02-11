import time

import pytest


# Mark customizado - adicionado no arquivo conftest
@pytest.mark.slow
def test_slow_marker():
    time.sleep(4)

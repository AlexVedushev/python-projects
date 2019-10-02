import random
import request
import pytest

@pytest.fixture
def rnd():
    return random.random()




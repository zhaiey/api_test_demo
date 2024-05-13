from api_test.utils import read_cases
import pytest

@pytest.fixture
def getdata():
    return read_cases.LoadCase



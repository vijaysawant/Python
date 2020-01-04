import pytest

def pytest_addoption(parser):
    parser.addoption("--val1", action="store", default="default name")

@pytest.fixture(scope="module")
def input_args(request):
    name_value = request.config.getoption("--val1")
    #if name_value is None:
    #   pytest.skip()
    return name_value
import pytest


@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print("End test")


@pytest.fixture(scope="module")
def set_group():
    print("Enter system")
    yield
    print("Exit system")

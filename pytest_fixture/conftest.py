import pytest


@pytest.fixture(scope="function")
def setup(page) -> None:
    print("\nSet up method is executed")


@pytest.fixture(scope="function")
def login(page) -> None:
    print("\nlogin operation performed")

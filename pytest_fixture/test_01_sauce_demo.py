import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


def test_01_setup_and_login(setup, login) -> None:
    print("Test case 1 is executed. Setup and Login")


def test_02_setup(setup) -> None:
    print("Test case 2 is executed. Only Setup")

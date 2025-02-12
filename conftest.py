import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    """Initialize WebDriver and provide it as a fixture."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

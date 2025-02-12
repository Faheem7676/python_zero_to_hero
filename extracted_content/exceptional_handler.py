from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    ElementNotInteractableException,
    StaleElementReferenceException
)

# centerlize exception handler
class ExceptionHandler:
    def __init__(self, log):
        self.log = log

    def handle_exception(self, exception, action="performing action"):
        if isinstance(exception, TimeoutException):
            self.log.error(f"Timeout while {action}.")
        elif isinstance(exception, NoSuchElementException):
            self.log.error(f"Element not found during {action}.")
        elif isinstance(exception, ElementClickInterceptedException):
            self.log.warning(f"Click intercepted while {action}. Retrying...")
        elif isinstance(exception, ElementNotInteractableException):
            self.log.warning(f"Element not interactable during {action}.")
        elif isinstance(exception, StaleElementReferenceException):
            self.log.warning(f"Stale element encountered during {action}.")
        else:
            self.log.error(f"Unexpected error while {action}: {str(exception)}")

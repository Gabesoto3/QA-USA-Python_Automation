from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class UrbanRoutesPage:
    """
    Page Object Model class for the Urban Routes application.
    """

    def __init__(self, driver: WebDriver):
        """
        Initialize the UrbanRoutesPage with the WebDriver instance.

        :param driver: The WebDriver instance.
        """
        self.driver = driver

    # Locators
    ROUTE_INPUT = (By.ID, "route_input")  # Example locator
    PLAN_SELECTOR = (By.CLASS_NAME, "plan_selector")  # Example locator
    PHONE_NUMBER_INPUT = (By.ID, "phone_number_input")
    CARD_INPUT = (By.XPATH, "//input[@name='card_info']")
    COMMENT_INPUT = (By.ID, "comment_input")
    ORDER_BUTTON = (By.CLASS_NAME, "order_btn")
    ICE_CREAM_ORDER_BUTTON = (By.XPATH, "//button[text()='Order Ice Cream']")
    DRIVER_INFO = (By.ID, "driver_info")
    SEARCH_BUTTON = (By.CLASS_NAME, "search_btn")

    # Methods to interact with elements
    def set_route(self, route: str):
        """Enter a route in the route input field."""
        self.driver.find_element(*self.ROUTE_INPUT).send_keys(route)

    def select_plan(self, plan: str):
        """Select a plan from the dropdown."""
        self.driver.find_element(*self.PLAN_SELECTOR).send_keys(plan)

    def fill_phone_number(self, phone_number: str):
        """Fill in the phone number field."""
        self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(phone_number)

    def fill_card_info(self, card_info: str):
        """Fill in the card information."""
        self.driver.find_element(*self.CARD_INPUT).send_keys(card_info)

    def add_comment_for_driver(self, comment: str):
        """Add a comment for the driver."""
        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)

    def place_order(self):
        """Click the order button to place an order."""
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def order_ice_cream(self, count: int):
        """Order multiple ice creams."""
        for _ in range(count):
            self.driver.find_element(*self.ICE_CREAM_ORDER_BUTTON).click()

    def search_driver_info(self):
        """Search for driver info."""
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def get_driver_info(self) -> str:
        """Retrieve driver information."""
        return self.driver.find_element(*self.DRIVER_INFO).text

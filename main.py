import data
import helpers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import UrbanRoutesPage  # Import the Page class


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # Enable additional logging for Selenium
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

        # Check if the server is reachable
        if not helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            raise ConnectionError("Cannot connect to Urban Routes. Check the server is on and running")

        cls.page = UrbanRoutesPage(cls.driver)  # Initialize the page object
        cls.driver.get(data.URBAN_ROUTES_URL)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    # Test methods
    def test_set_route(self):
        """Test setting a route."""
        self.page.set_route("Downtown to Uptown")
        assert "Route set successfully" in self.driver.page_source, "Route was not set correctly."

    def test_select_plan(self):
        """Test selecting a plan."""
        self.page.select_plan("Premium")
        assert "Plan selected: Premium" in self.driver.page_source, "Plan was not selected correctly."

    def test_fill_phone_number(self):
        """Test filling in the phone number."""
        self.page.fill_phone_number("1234567890")
        assert "Phone number saved" in self.driver.page_source, "Phone number was not saved correctly."

    def test_fill_card(self):
        """Test filling in the card information."""
        self.page.fill_card_info("4111111111111111")
        assert "Payment method saved" in self.driver.page_source, "Card information was not saved correctly."

    def test_comment_for_driver(self):
        """Test adding a comment for the driver."""
        self.page.add_comment_for_driver("Please drive carefully.")
        assert "Comment added" in self.driver.page_source, "Comment for driver was not added correctly."

    def test_order_blanket_and_handkerchiefs(self):
        """Test placing an order for a blanket and handkerchiefs."""
        self.page.place_order()
        assert "Order placed" in self.driver.page_source, "Order was not placed correctly."

    def test_order_2_ice_creams(self):
        """Test ordering two ice creams."""
        self.page.order_ice_cream(count=2)
        assert "Order: 2 ice creams" in self.driver.page_source, "Ice cream order was not placed correctly."

    def test_car_search_model_appears(self):
        """Test searching for a car model."""
        self.page.search_driver_info()
        assert "Car model found" in self.driver.page_source, "Car model search did not appear correctly."

    def test_driver_info_appears(self):
        """Test retrieving driver information."""
        driver_info = self.page.get_driver_info()
        assert "Driver Name" in driver_info, "Driver information did not load properly."

 @classmethod
    def teardown_class(cls):
        cls.driver.quit()
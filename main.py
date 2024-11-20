import data
import helpers

# Check if the Urban Routes server is working
if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
    print("Connected to the Urban Routes server")
else:
    print("Cannot connect to Urban Routes. Check the server is on and still running")
    exit()  # Exit the program if the server is unreachable


# Define functions for the Urban Routes application
def test_set_route(self):
    # Add in S8
    pass


def test_select_plan(self):
    # Add in S8
    pass


def test_fill_phone_number(self):
    # Add in S8
    pass


def test_fill_card(self):
    # Add in S8
    pass


def test_comment_for_driver(self):
    # Add in S8
    pass


def test_order_blanket_and_handkerchiefs(self):
    # Add in S8
    pass


def test_order_2_ice_creams(self):
    # Add in S8
    num_ice_creams = 2  # Define the number of ice creams as a variable
    for _ in range(num_ice_creams):  # Loop based on the variable
        # Todo in S8
        pass


def test_car_search_model_appears(self):
    # Add in S8
    pass


def test_driver_info_appears(self):
    # Add in S8
    pass

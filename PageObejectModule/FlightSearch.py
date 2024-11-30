from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common .action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class FlightSearch:
    flight_tab_xpath = "//a[normalize-space()='Flights']"             #//div[@class='input-items from_flights']//span[@id='select2--container']
    one_way_trip_xpath = "//label[@for='one-way']"
    round_Trip_xpath = "//label[@for='round-trip']"
    flight_class_xpath = "//select[@id='flight_type']"
    destination_from_xpath = "(//div[@class='mt-2'])[1]"
    destination_from_input_xpath = "//input[@role='searchbox']"
    destination_choose_xpath = "//button[normalize-space()='SIN']"
    destination_to_xpath = "(//div[@class='mt-2'])[2]"
    destination_to_input_xpath = "//input[@role='searchbox']"
    departure_date_xpath = "//input[@id='departure']"
    return_date_xpath = "//input[@id='return_date']"
    travellers_box_xpath = "//section[@class='feature flights']//p[1]"
    travellers_adults_xpath = "//input[@id='fadults']"
    travellers_child_xpath = "//input[@id='fchilds']"
    travellers_infants_xpath = "//input[@id='finfant']"
    serach_box_xpath = "//button[@id='flights-search']"
    all_flight_stops_xpath = "//input[@id='all']"
    direct_flight_xpath = "//input[@id='direct']"
    price_range_from_xpath = "//span[@class='irs-handle from']"
    price_range_to_xpath = "//span[@class='irs-handle to']"
    emirates_flight_xpath = "//label[normalize-space()='Emirates']"
    srilankan_flight_xpath = "//label[normalize-space()='SriLankan Airlines']"
    singapore_flight_xpath = "//label[normalize-space()='Singapore Airlines']"
    total_flight_xpath  = "//div[@class='flex tit-travel-restriction-wrapper']/h2/span"

    def __init__(self,driver):
        self.driver = driver

    def webdriver_wait(self,xpath,timeout=10,click=False):
        element = WebDriverWait(self.driver,timeout).until(ec.presence_of_element_located((By.XPATH,xpath)))
        if click:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((By.XPATH, xpath))).click()
        return element

    def flight_tab(self):
        flight_btn = self.webdriver_wait(self.flight_tab_xpath,click=True)

    def trip_type(self, types):
        try:
            types = types.lower()
            if types == "one way":
                self.webdriver_wait(self.one_way_trip_xpath, click=True)
                self.current_trip_type = "one way"
                print("One way trip is selected.")
            elif types == "round trip":
                self.webdriver_wait(self.round_Trip_xpath, click=True)
                self.current_trip_type = "round trip"
                print("Round trip is selected.")
            else:
                raise ValueError("Invalid trip type. Please specify 'one way' or 'round trip'.")
        except Exception as e:
            print(f"Error selecting trip type: {e}")

    def flight_class(self,classes):
        flight_class_select = self.webdriver_wait(self.flight_class_xpath)
        select_class = Select(flight_class_select)
        select_class.select_by_visible_text(classes)

    def departure_from(self,country_name,abbre):
        depature_from_box = self.webdriver_wait(self.destination_from_xpath,click=True)
        from_input = self.webdriver_wait(self.destination_from_input_xpath)
        from_input.clear()
        from_input.send_keys(country_name)
        departure_choose_place = self.webdriver_wait(f"//button[normalize-space()='{abbre}']",click=True)

    def departure_to(self,country_name,abbre):
        departure_to_box = self.webdriver_wait(self.destination_to_xpath,click=True)
        to_input = self.driver.find_element(By.XPATH,self.destination_to_input_xpath)
        to_input.clear()
        to_input.send_keys(country_name)
        departure_choose_place = self.webdriver_wait(f"//button[normalize-space()='{abbre}']").click()

    def departure_date(self,date):
        departure_date_box = self.webdriver_wait(self.departure_date_xpath,click=True)
        departure_date_box.clear()
        departure_date_box.send_keys(date)

    def return_date(self,date):
        try:
            # Ensure the trip type is set to "round trip"
            if self.current_trip_type != "round trip":
                raise ValueError("Return date can only be set for a 'round trip'. Please set the trip type first.")

            # Interact with the return date input box
            return_date_box = self.webdriver_wait(self.return_date_xpath, click=True)
            return_date_box.clear()
            return_date_box.send_keys(date)
            print(f"Return date set to {date}.")
        except Exception as e:
            print(f"Error setting return date: {e}")

    def total_travellers(self,adults,childs,infants):
        travellers_box = self.webdriver_wait(self.travellers_box_xpath,click=True)
        adult_travellers = self.webdriver_wait(self.travellers_adults_xpath)
        adult_travellers.clear()
        adult_travellers.send_keys(adults)
        child_travellers_xpath = self.webdriver_wait(self.travellers_child_xpath)
        child_travellers_xpath.clear()
        child_travellers_xpath.send_keys(childs)
        infant_travellers = self.webdriver_wait(self.travellers_infants_xpath)
        infant_travellers.clear()
        infant_travellers.send_keys(infants)

    def search_btn(self):
        search = self.webdriver_wait(self.serach_box_xpath,click=True)

    def flight_stops(self):
        direct_flight = self.webdriver_wait(self.direct_flight_xpath,click=True)

    def calculate_offset(self, price, min_value, max_value, slider_width):
        """Convert the target price into a pixel offset."""
        return (price - min_value) / (max_value - min_value) * slider_width

    def price_range(self, target_price):
        """Adjust the price slider to the desired target price."""
        # Scroll into view to ensure the slider is visible

        # Define the slider range (update these values if they differ)
        min_value = 0
        max_value = 10000

        # Get the slider element and its width dynamically
        slider_element = self.webdriver_wait("//span[@class='irs-bar']")
        slider_width = slider_element.size['width']  # Total width of the slider

        # Calculate the offset for the desired price
        price_offset = self.calculate_offset(target_price, min_value, max_value, slider_width)

        # Locate the correct slider handle to adjust
        price_handle = self.webdriver_wait(self.price_range_to_xpath)

        # Move the slider handle to the desired position
        act = ActionChains(self.driver)
        act.click_and_hold(price_handle).move_by_offset(price_offset, 0).release().perform()

    def airline_type(self,name):
        element = self.webdriver_wait("//div[@class='sidebar-box mb-2 controls']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        airline_type_select = self.webdriver_wait(f"//label[normalize-space()='{name}']")

    def total_flights(self):
        total_flight = self.webdriver_wait(self.total_flight_xpath)
        print(total_flight.text)









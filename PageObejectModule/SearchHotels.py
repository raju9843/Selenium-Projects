from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common .action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SearchHotel:
    hotel_btn_xpath = "//a[normalize-space()='Hotels']"
    hotel_city_box_xpath = "//span[@id='select2-hotels_city-container']"
    check_in_box_xpath = "//input[@id='checkin']"
    check_out_box_xpath = "//input[@id='checkout']"
    passengers_rooms_box_xpath = "//a[contains(@class,'dropdown-toggle dropdown-btn travellers d-flex align-items-center waves-effect')]"
    hotel_rooms_box_xpath = "//input[@id='hotels_rooms']"
    adults_box_xpath = "//input[@id='hotels_adults']"
    childs_box_xpath = "//input[@id='hotels_childs']"
    search_button_xpath = "//form[@id='hotels-search']//button[@type='submit']"
    star_rating_xpath = "//input[@id='starRating4']"
    price_rating_slicer1_xpath = "//span[@class='irs-handle from']"
    price_rating_slicer2_xpath = "//span[@class='irs-handle to']"
    apply_filters_xpath = "//button[normalize-space()='Apply Filters']"
    hotel_name_xpath = "//strong[normalize-space()='K Hotel 1515']"

    def __init__(self,driver):
        self.driver = driver


    def webdriver_wait(self,xpath,timeout=10,click=False):
        element = WebDriverWait(self.driver,timeout).until(ec.presence_of_element_located((By.XPATH,xpath)))
        if click:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((By.XPATH, xpath))).click()
        return element


    def hotel_tab_click(self):
        hotel_tab = self.webdriver_wait(self.hotel_btn_xpath,click=True)


    def city_name(self,name):
        city = self.webdriver_wait("//span[@id='select2-hotels_city-container']",click=True)
        names = self.webdriver_wait("//input[@role='searchbox']")
        names.send_keys(name)
        city_nsme = self.webdriver_wait(f"//strong[normalize-space()='{name}']").click()


    def check_in_box(self,date1):
        check_in = self.webdriver_wait(self.check_in_box_xpath,click=False)
        check_in.clear()
        check_in.send_keys(date1)


    def check_out_box(self,date2):
        check_out = self.webdriver_wait(self.check_out_box_xpath,click=False)
        check_out.clear()
        check_out.send_keys(date2)


    def passenger_and_rooms_box(self,rooms,adults,child):
        passenger_rooms = self.webdriver_wait(self.passengers_rooms_box_xpath,click=True)
        no_of_rooms = self.webdriver_wait(self.hotel_rooms_box_xpath,click=False)
        no_of_rooms.clear()
        no_of_rooms.send_keys(rooms)
        no_of_adults = self.webdriver_wait(self.adults_box_xpath,click=False)
        no_of_adults.clear()
        no_of_adults.send_keys(adults)
        no_of_children = self.webdriver_wait(self.childs_box_xpath,click=False)
        no_of_children.clear()
        no_of_children.send_keys(child)


    def search_btn(self):
        search = self.webdriver_wait(self.search_button_xpath,click=True)



    def star_rating(self,stars):
        star = self.webdriver_wait(f"//label[normalize-space()='{stars}']")
        star.click()


    def calculate_offset(self,price, min_value, max_value, slider_width):
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
        price_handle = self.webdriver_wait(self.price_rating_slicer2_xpath)

        # Move the slider handle to the desired position
        act = ActionChains(self.driver)
        act.click_and_hold(price_handle).move_by_offset(price_offset, 0).release().perform()

    def apply_filter(self):
        element = self.webdriver_wait("//a[normalize-space()='Playstore']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element = self.webdriver_wait(self.apply_filters_xpath, timeout=15)
        self.driver.execute_script("arguments[0].click();", element)













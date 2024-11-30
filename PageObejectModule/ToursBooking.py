from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common .action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TourBooking:
    tour_tab_xpath = "//a[normalize-space()='Tours']"
    city_tab_xpath = "//span[@id='select2-tours_city-container']"   #//span[@id='select2-tours_city-container']
    city_name_input_xpath = "//input[@role='searchbox']"
    city_name_xpath = f"//strong[normalize-space()='Singapore']"
    booking_date_tab_xpath = "//input[@id='date']"
    month_year_xpath = "//div[@class='datepicker dropdown-menu']/div[1]/table/thead/tr[1]/th[2]"
    next_month_xpath = "//div[@class='datepicker-days']//th[@class='next']//*[name()='svg']"
    date_xpath = "//td[normalize-space()='17']"
    travellers_tab_xpath = "//a[@class='dropdown-toggle dropdown-btn travellers waves-effect']"
    travellers_adults_tab_xpath = "//input[@id='tours_adults']"
    travellers_childs_tab_xpath = "//input[@id='tours_child']"
    search_button_xpath = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver = driver

    def webdriver_wait(self,xpath,timeout=10,click=False):
        element = WebDriverWait(self.driver,timeout).until(ec.presence_of_element_located((By.XPATH,xpath)))
        if click:
            element.click()
        return element

    def tours_tab_click(self):
        tours_tab = self.webdriver_wait(self.tour_tab_xpath,click=True)

    def city_name(self,city_name):
        city_names_tab = self.webdriver_wait(self.city_tab_xpath,click=True)
        city_name_input = self.webdriver_wait(self.city_name_input_xpath)
        city_name_input.clear()
        city_name_input.send_keys(city_name)
        city_name_click = self.webdriver_wait(f"//strong[normalize-space()='{city_name}']").click()

    def booking_date(self, month, year, date):
        """
        Select a booking date from a calendar.

        Args:
            month (str): The name of the month (e.g., "January").
            year (str or int): The year (e.g., "2024" or 2024).
            date (str or int): The day of the month to select (e.g., "15" or 15).

        Raises:
            Exception: If the desired date is not found or another error occurs.
        """
        try:
            # Open the booking date picker
            self.webdriver_wait(self.booking_date_tab_xpath, click=True)

            # Format the target month and year
            target_month_year = f"{month} {year}"

            # Navigate through the calendar to find the correct month and year
            while True:
                # Get the currently displayed month and year
                displayed_month_year = self.webdriver_wait(self.month_year_xpath).text.strip()
                print(f"Displayed month and year: {displayed_month_year}")
                print(f"Target month and year: {target_month_year}")

                if displayed_month_year == target_month_year:
                    break  # Stop when the correct month and year are displayed

                # Click the "Next" button to move to the next month
                self.webdriver_wait(self.next_month_xpath, click=True)

            # Locate all date elements in the calendar
            date_elements = WebDriverWait(self.driver, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, "//tbody/tr/td"))
            )

            # Find and click the specified date
            for date_element in date_elements:
                if date_element.text.strip() == str(date):  # Match the text with the desired date
                    date_element.click()
                    print(f"Date selected: {date}-{month}-{year}")
                    return

            # Raise an exception if the date is not found
            raise ValueError(f"Date {date}-{month}-{year} not found in the calendar.")

        except Exception as e:
            print(f"Error selecting booking date: {e}")

    def total_travellers(self,adults,child):
        traveller_tab = self.webdriver_wait(self.travellers_tab_xpath,click=True)
        traveller_adult_tab = self.webdriver_wait(self.travellers_adults_tab_xpath)
        traveller_adult_tab.clear()
        traveller_adult_tab.send_keys(adults)
        traveller_child_tab = self.webdriver_wait(self.travellers_childs_tab_xpath)
        traveller_child_tab.clear()
        traveller_child_tab.send_keys(child)

    def search_btn(self):
        search_tab = self.webdriver_wait(self.search_button_xpath,click=True)









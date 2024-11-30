from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common .action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CarSearch:
    car_tab_xpath = "//a[normalize-space()='Cars']"
    from_location_xpath = "//div[@class='mt-1']"
    from_location_input_xpath = "//input[@role='searchbox']"
    from_location_btn_xpath = "//button[normalize-space()='BLR']"
    to_location_xpath = "//div[@class='input-items cars_location']"
    to_location_input_xpath = "//input[@role='searchbox']"
    to_location_select = "//li[@role='option']"
    pick_up_date_xpath = "//input[@id='cars_from_date']"
    month_year_xpath = "//table[@class=' table-condensed']/thead/tr[1]/th[2]"
    date_xpath = "//td[normalize-space()='18']"
    next_month_xpath = "//div[@class='datepicker-days']//th[@class='next']//*[name()='svg']"
    pick_up_time_xpath = "//select[@id='cars_from_time']"
    drop_date_xpath = "//input[@id='cars_to_date']"
    drop_time_xpath = "//select[@id='cars_to_time']"
    travellers_box_xpath = "//p[@class='m-0 d-flex align-items-center gap-2']"
    adults_xpath = "//input[@id='cars_adults']"
    child_xpath = "//input[@id='cars_child']"
    search_btn_xpath = "//button[@class='search_button w-100 btn btn-primary btn-m rounded-sm font-700 text-uppercase btn-full waves-effect']"

    def __init__(self, driver):
        self.driver = driver

    def webdriver_wait(self, xpath, timeout=10, click=False):
        element = WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((By.XPATH, xpath)))
        if click:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((By.XPATH, xpath))).click()
        return element

    def car_tab(self):
        flight_btn = self.webdriver_wait(self.car_tab_xpath, click=True)


    def from_location(self,city_name,btn_name):
        try:
            city_name_tab = self.webdriver_wait(self.from_location_xpath,click=True)
            city_input_tab = self.webdriver_wait(self.from_location_input_xpath)
            city_input_tab.clear()
            city_input_tab.send_keys(city_name)
            city_btn = self.webdriver_wait(f"//button[normalize-space()='{btn_name}']").click()
            print(f"{city_name} is selected")

        except Exception as e:
            print(f"{city_name} is not Found")
            print(e)

    def to_location(self,city_name):
        try:
            city_name_tab = self.webdriver_wait(self.to_location_xpath, click=True)
            city_input_tab = self.webdriver_wait(self.to_location_input_xpath)
            city_input_tab.clear()
            city_input_tab.send_keys(city_name)
            city_btn = self.webdriver_wait(self.to_location_select,click=False)
            if city_name in city_btn.text:
                city_btn.click()
            print(f"{city_name} is found and selected")

        except Exception as e:
            print(f"{city_name} is not found and not selected")


    def pick_up_date(self,month,year,date):
        try:
            # Open the booking date picker
            pick_up_tab = self.webdriver_wait(self.pick_up_date_xpath,click=True)

            # Format the target month and year
            target_month_year = f"{month} {year}"

            # Navigate through the calendar to find the correct month and year
            while True:
                # Get the currently displayed month and year
                displayed_month_year = self.webdriver_wait(self.month_year_xpath).text.strip()
                print(f"Displayed month and year: {displayed_month_year}")
                print(f"Target month and year: {target_month_year}")

                if displayed_month_year == target_month_year :

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


    def pick_up_time(self,time):
        pick_up_time_box = self.webdriver_wait(self.pick_up_time_xpath,click=True)
        select = Select(pick_up_time_box)
        select.select_by_value(time)


    def drop_off_date(self,date,month,year):
        try:
            # Open the booking date picker
            drop_off_box = self.webdriver_wait(self.drop_date_xpath,click=True)

            # Format the target month and year
            target_month_year = f"{month} {year}"

            # Navigate through the calendar to find the correct month and year
            while True:
                # Get the currently displayed month and year
                displayed_month_year = WebDriverWait(self.driver,10).until(ec.presence_of_element_located((By.CSS_SELECTOR,"body > div:nth-child(13) > div:nth-child(1) > table:nth-child(1) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(2)"))).text.strip()
                print(f"Displayed month and year: {displayed_month_year}")
                print(f"Target month and year: {target_month_year}")

                if displayed_month_year == target_month_year:
                    break  # Stop when the correct month and year are displayed

                # Click the "Next" button to move to the next month
                self.webdriver_wait("(//th[@class='next'])[4]", click=True)
                print(f"{month}-{year} selected")

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

    def drop_time(self,time):
        drop_time = self.webdriver_wait(self.drop_time_xpath,click=True)
        select = Select(drop_time)
        select.select_by_value(time)

    def total_travellers(self,adults,child):
        travellers_tab = self.webdriver_wait(self.travellers_box_xpath,click=True)
        adults_travellers = self.webdriver_wait(self.adults_xpath)
        adults_travellers.clear()
        adults_travellers.send_keys(adults)
        childs = self.webdriver_wait(self.child_xpath)
        childs.clear()
        childs.send_keys(child)

    def search_btn(self):
        search_btns = self.webdriver_wait(self.search_btn_xpath,click=True)








import pytest
from PageObejectModule.SearchHotels import SearchHotel
from Utilities.CustomerLogin import LogGen
import time

from test_Cases.conftest import save_screenshots


@pytest.mark.second
@pytest.mark.usefixtures("setup")
class TestLogin:
    base_url = "https://www.phptravels.net/"


    def test_login001(self,setup):
        self.loggin = LogGen().loggen()
        self.loggin.info("*************** Testing Logging Page Started *****************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp1 = SearchHotel(self.driver)
        self.driver.maximize_window()
        time.sleep(2)
        self.loggin.info("************ Booking Hotels Process **************")
        self.lp1.hotel_tab_click()
        self.lp1.city_name("Singapore")
        time.sleep(1)
        self.lp1.check_in_box("30-11-2024")
        self.lp1.check_out_box("12-12-2024")
        time.sleep(2)
        self.loggin.info("**************** Total Passengers ******************")
        self.lp1.passenger_and_rooms_box("3","4","2")
        time.sleep(2)
        self.lp1.search_btn()
        self.lp1.star_rating("3")
        self.loggin.info("****************** Flight ticket price *************")
        self.lp1.price_range(-1500)
        time.sleep(2)
        self.lp1.apply_filter()
        self.loggin.info("*****************Hotel Booking Process Finished **********")
        time.sleep(3)
        screeshots = save_screenshots(self.driver,"hotel_booking_page.png")
        self.driver.close()



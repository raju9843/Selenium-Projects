import pytest
from PageObejectModule.ToursBooking import TourBooking
from Utilities.CustomerLogin import LogGen
from TestData.Basename import TestData
import time

from test_Cases.conftest import save_screenshots


@pytest.mark.fourth
@pytest.mark.usefixtures("setup")
class TestLogin:
    base_url = TestData.BASE_URL


    def test_login001(self,setup):
        self.loggin = LogGen().loggen()
        self.loggin.info("*************** Testing Booking Tours Started *****************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.tbs = TourBooking(self.driver)
        self.driver.maximize_window()
        time.sleep(2)
        self.loggin.info("************ Booking Tour Process **************")
        self.tbs.tours_tab_click()
        time.sleep(2)
        self.tbs.city_name("Singapore")
        self.tbs.booking_date("December","2025","13")
        self.tbs.total_travellers(4,2)
        time.sleep(2)
        self.tbs.search_btn()
        self.loggin.info("************* Testing Booking Process Finished **************")
        time.sleep(2)
        screeshots = save_screenshots(self.driver,"tour_search.png")
        self.driver.close()
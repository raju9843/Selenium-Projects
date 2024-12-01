import pytest
from PageObejectModule.CarSearch import CarSearch
from Utilities.CustomerLogin import LogGen
from TestData.Basename import TestData
import time

from test_Cases.conftest import save_screenshots


@pytest.mark.fifth
@pytest.mark.usefixtures("setup")
class TestLogin:
    base_url = TestData.BASE_URL


    def test_login001(self,setup):
        self.loggin = LogGen().loggen()
        self.loggin.info("*************** Testing Booking Cars Started *****************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.cbs = CarSearch(self.driver)
        self.driver.maximize_window()
        self.loggin.info("***************** Opening Websites ***************")
        self.cbs.car_tab()
        self.loggin.info("***************** Opening Car Tab for Booking ***************")
        time.sleep(2)
        self.cbs.from_location("Bangalore","BLR")
        self.cbs.to_location("Chennai")
        self.cbs.pick_up_date("November","2025","25")
        self.cbs.pick_up_time("10:00")
        time.sleep(2)
        self.cbs.drop_off_date("28","November","2025")
        self.cbs.drop_time("16:30")
        self.cbs.total_travellers("3","1")
        self.cbs.search_btn()
        self.loggin.info("************ Car Booking Finished ***********")
        time.sleep(2)
        screeshots = save_screenshots(self.driver,"car_booking.png")
        self.driver.close()

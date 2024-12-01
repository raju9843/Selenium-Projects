import pytest
from PageObejectModule.FlightSearch import FlightSearch
from Utilities.CustomerLogin import LogGen
from TestData.Basename import TestData
import time

from test_Cases.conftest import save_screenshots


@pytest.mark.third
@pytest.mark.usefixtures("setup")
class TestLogin:
    base_url = TestData


    def test_login001(self,setup):
        self.loggin = LogGen().loggen()
        self.loggin.info("*************** Testing Logging Page Started *****************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.fls = FlightSearch(self.driver)
        self.driver.maximize_window()
        time.sleep(2)
        self.loggin.info("************ Booking Flight ticket  Process **************")
        self.fls.flight_tab()
        self.fls.trip_type("one way")
        self.fls.flight_class("Economy")
        self.fls.departure_date("30-11-2024")
        self.fls.return_date("15-12-2024")
        time.sleep(2)
        self.fls.departure_from("Singapore", "SIN")
        self.fls.departure_to("Dubai", "DXB")
        time.sleep(2)
        self.fls.total_travellers(5,3,1)
        self.fls.search_btn()
        self.loggin.info("************* Ticket Booking Process Finished **************")
        time.sleep(3)
        self.fls.flight_stops()
        self.fls.price_range(-5000)
        time.sleep(2)
        self.loggin.info("************** Flight Type ****************")
        self.fls.airline_type("Emirates")
        self.fls.total_flights()
        time.sleep(2)
        screeshots = save_screenshots(self.driver,"flight_search.png")
        self.driver.close()

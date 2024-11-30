import pytest
from PageObejectModule.LoginPage import Login_001
from Utilities.CustomerLogin import LogGen
import time

from test_Cases.conftest import save_screenshots


@pytest.mark.first
@pytest.mark.usefixtures("setup")
class TestLogin:
    base_url = "https://www.phptravels.net/"


    def test_login001(self,setup):
        self.loggin = LogGen().loggen()
        self.loggin.info("*************** Testing Logging Page Started *****************")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = Login_001(self.driver)
        self.lp.account_btn_click()
        time.sleep(2)
        head_001 = 'PHPTRAVELS'
        assert self.driver.title == head_001
        if head_001:
            self.loggin.info("****************** Login title name success *******************")
        else:
            self.loggin.error("****************** Login title name failed *******************")

        self.loggin.info("************** Creating Logging Account *************")
        self.lp.login_click()
        self.lp.user_details("user@phptravels.com","demouser")
        self.lp.continue_btn()
        time.sleep(2)
        head_002 = "Dashboard"
        assert head_002 == self.driver.title
        if head_002:
            self.loggin.info("***************** Test Login Success *******************")
        else:
            self.loggin.error("***************** Test Login Failed """"""""""""""""""")
        time.sleep(2)
        screeshots = save_screenshots(self.driver, "login_page.png")
        self.loggin.info("**************** Test Loggin Finished ****************")
        time.sleep(2)
        self.lp.logout_click()
        self.loggin.info("**************** Test Logout Success ***************")
        self.driver.close()





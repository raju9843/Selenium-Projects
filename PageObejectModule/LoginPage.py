from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Login_001:
    account_btn_xpath = "//a[@class='bg-light nav-link dropdown-toggle btn btn-outline-secondary px-0 ps-3 text-center d-flex align-items-center justify-content-center gap-2 border waves-effect']"
    login1_btn_xpath = "//a[@href='https://www.phptravels.net/login']"
    email_box_xpath = "//input[@id='email']"
    password_box_xpath = "//input[@id='password']"
    login2_btn_xpath = "//button[@id='submitBTN']"
    logout_btn_xpath = "//a[contains(text(),'Logout')]"


    def __init__(self,driver):
        self.driver = driver


    def webdriver_wait(self,xpath,timeout=10,click = False):
        element = WebDriverWait(self.driver,timeout).until(ec.presence_of_element_located((By.XPATH,xpath)))
        if click:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((By.XPATH, xpath))).click()
        return element

    def account_btn_click(self):
        accont_btn = self.webdriver_wait(self.account_btn_xpath,click=True)


    def login_click(self):
        login_btn = self.webdriver_wait(self.login1_btn_xpath,click = True)


    def user_details(self,user_email,user_password):
        email = self.webdriver_wait(self.email_box_xpath,click=False)
        email.clear()
        email.send_keys(user_email)
        password = self.webdriver_wait(self.password_box_xpath,click=False)
        password.clear()
        password.send_keys(user_password)


    def continue_btn(self):
        continue_btn = self.webdriver_wait(self.login2_btn_xpath,click=True)


    def logout_click(self):
        account = self.webdriver_wait(self.account_btn_xpath,click=True)
        logout = account.find_element(By.XPATH,self.logout_btn_xpath)
        logout.click()

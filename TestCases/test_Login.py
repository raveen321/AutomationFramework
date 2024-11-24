import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PageObjects.LoginPageDebug import LoginPage


from selenium import webdriver
import pytest


@pytest.fixture
def setup():
    serv_tag = Service("C:\\Users\\panra\\OneDrive - Otis Elevator\\Documents\\Technical\\Softwares\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_tag)
    return driver


class Test_001_Login:
    baseurl = "https://10.184.54.114/auth/realms/ems/protocol/openid-connect/auth?client_id=ems-web&redirect_uri=https%3A%2F%2F10.184.54.114%2F%23%2Fabout%2Fversions&state=02aa441b-e678-4b55-8ac3-51411bd7a5c0&response_mode=fragment&response_type=code&scope=openid&nonce=4575abbc-e643-490d-8e09-004854df668a"
    username = "otis"
    password = "mViyL3Vi*2"

    def test_Login(self,setup):
        self.driver=setup
    @pytest.mark.Sanity
    @pytest.mark.Regression
    def test_Login(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "details-button").click()
        self.driver.find_element(By.ID, "proceed-link").click()
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_Title = self.driver.title
        self.driver.close()
        if act_Title == "OTIS EMS PANORAMA 2.0":
            assert True
        else:
            assert False





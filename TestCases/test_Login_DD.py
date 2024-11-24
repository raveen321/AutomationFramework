import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import readconfig
from Utilities.customLogger import LogGen
from Utilities import utilxls

@pytest.fixture
def setup():
    serv_tag = Service("C:\\Users\\panra\\OneDrive - Otis Elevator\\Documents\\Technical\\Softwares\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_tag)
    return driver


class Test_002_Login_DD:
    baseurl = readconfig.getApplicationURL()
    path=".//TestData/Logindata.xlsx"

    logger=LogGen.logGen()


    @pytest.mark.Regression
    def test_LoginDD(self,setup):
        self.logger.info("*********TEST002**********")
        self.logger.info("*********Verify Login**********")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "details-button").click()
        self.driver.find_element(By.ID, "proceed-link").click()
        # # self.lp = LoginPage(self.driver)

        self.rows=utilxls.getRowCount(self.path,"Sheet1")

        for r in range(2,self.rows+1):
            self.lp = LoginPage(self.driver)
            self.user=utilxls.gerReadData(self.path,"Sheet1",r,1)
            self.password = utilxls.gerReadData(self.path, "Sheet1", r, 2)
            self.exp = utilxls.gerReadData(self.path, "Sheet1", r, 3)
            print(self.user)
            print(self.password)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(10)
            act_Title = self.driver.title
            exp_title="OTIS EMS PANORAMA 2.0"
            if act_Title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("**********Passed********")
                    self.driver.close()
                elif self.exp=="Fail":
                    self.logger.info("**********Failed********")
                    time.sleep(10)
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_Login1.png")
                    self.driver.close()







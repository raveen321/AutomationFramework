from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage:
    textbox_username_id="username"
    textbox_password_id="password"
    button_login_id="kc-login"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.username=username
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(self.username)


    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys("mViyL3Vi*2")

    def clickLogin(self):
        self.driver.find_element(By.ID,self.button_login_id).click()




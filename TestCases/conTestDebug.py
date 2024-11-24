from selenium import webdriver
import pytest


@pytest.fixture
def setup():
    serv_tag = Service("C:\\Users\\panra\\OneDrive - Otis Elevator\\Documents\\Technical\\Softwares\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_tag)
    return driver
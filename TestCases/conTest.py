from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if brower=="chrome":
        serv_tag = Service("C:\\Users\\panra\\OneDrive - Otis Elevator\\Documents\\Technical\\Softwares\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_tag)
    else browser=="firefox":
    driver = webdriver.Firefox()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

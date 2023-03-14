from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data.data import Revathi_Data
from Test_Locator.locator import Revathi_Locator
from time import sleep
import pytest

class Test_Revathi:
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    def test_TC_Login_01(self, boot):
        self.driver.implicitly_wait(10)
        self.driver.get(Revathi_Data().B)
        self.driver.find_element(by = By.NAME, value = Revathi_Locator().A).send_keys(Revathi_Data().C)
        self.driver.find_element(by = By.NAME, value = Revathi_Locator().B).send_keys(Revathi_Data().D)
        self.driver.find_element(by = By.XPATH, value = Revathi_Locator().C).click()
        assert (self.driver.title == Revathi_Data().A)
        print("Status = Successful")

    def test_TC_Login_02(self, boot):
        self.driver.implicitly_wait(10)
        self.driver.get(Revathi_Data().B)
        self.driver.find_element(by = By.NAME, value = Revathi_Locator().A).send_keys(Revathi_Data().E)
        self.driver.find_element(by = By.NAME, value = Revathi_Locator().B).send_keys(Revathi_Data().F)
        self.driver.find_element(by = By.XPATH, value = Revathi_Locator().C).click()
        assert (self.driver.title == "OrangeHHRM")
        # print("Status = Successful")

    def test_TC_PIM_01(self, boot):
        self.driver.implicitly_wait(10)
        self.test_TC_Login_01(self)
        self.driver.find_element(by = By.XPATH, value = Revathi_Locator().D).click()
        self.driver.find_element(by = By.LINK_TEXT, value = Revathi_Locator().E).click()
        self.driver.find_element(by = By.NAME, value = Revathi_Locator().F).send_keys(Revathi_Data().G)
        self.driver.find_element(by = By.NAME, value = Revathi_Locator().G).send_keys(Revathi_Data().H)
        self.driver.find_element(by = By.NAME, value = Revathi_Locator().H).send_keys(Revathi_Data().I)
        self.driver.find_element(by = By.XPATH, value = Revathi_Locator().I).click()
        self.driver.find_element(by = By.LINK_TEXT, value = Revathi_Locator().J).click()
        self.driver.find_element(by = By.XPATH, value = Revathi_Locator().K).send_keys(Revathi_Data().J)
        self.driver.find_element(by = By.XPATH, value = Revathi_Locator().L).send_keys(Revathi_Data().K)
        self.driver.find_element(by = By.XPATH, value = Revathi_Locator().M).send_keys(Revathi_Data().L)
        self.driver.find_element(by = By.XPATH, value = Revathi_Locator().N).send_keys(Revathi_Data().M)
        self.driver.find_element(by = By.XPATH, value = Revathi_Locator().O).send_keys(Revathi_Data().N)
        self.driver.find_element(by = By.XPATH, value = Revathi_Locator().P).send_keys(Revathi_Data().O)
        self.driver.find_element(by = By.XPATH, value = Revathi_Locator().Q).send_keys(Revathi_Data().P)
        self.driver.find_element(by = By.XPATH, value = Revathi_Locator().R).click()
        self.driver.implicitly_wait(10)
        assert (self.driver.title == Revathi_Data().A)
        print("Status = Successful")

# pytest -v -s --capture=sys --html=C:\Users\tmztm\Desktop\Capstone\Report\Test_1.html testRevathi.py
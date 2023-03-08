from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pytest as pytest
from selenium import webdriver


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    sendValue = (By.CSS_SELECTOR, "input[placeholder='Search for Vegetables and Fruits']")
    # self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search for Vegetables and Fruits']").send_keys("be")
    searchValues = (By.CSS_SELECTOR, "button[class='search-button']")
    # self.driver.find_element(By.CSS_SELECTOR, "button[class='search-button']").click()
    clickPluses = (By.XPATH, "//div[@class='stepper-input']")
    # self.driver.find_elements(By.XPATH, "//div[@class='stepper-input']")
    clickProducts = (By.XPATH, "//div[@class='products']/div")
    # self.driver.find_elements(By.XPATH, "//div[@class='products']/div")
    cartClick = (By.CSS_SELECTOR, "a[class='cart-icon']")
    # self.driver.find_element(By.CSS_SELECTOR, "a[class='cart-icon']").click()
    proceedToCheckout = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    # self.driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()


    def sendValue1(self):
        return self.driver.find_element(*HomePage.sendValue)

    def searchValues1(self):
        return self.driver.find_element(*HomePage.sendValue)

    def clickPluses1(self):
        return self.driver.find_elements(*HomePage.clickPluses)

    def clickProducts1(self):
        return self.driver.find_elements(*HomePage.clickProducts)

    def cartClick1(self):
        return self.driver.find_element(*HomePage.cartClick)

    def proceedToCheckout1(self):
        return self.driver.find_element(*HomePage.proceedToCheckout)


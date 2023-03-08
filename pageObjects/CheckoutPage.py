from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pytest as pytest
from selenium import webdriver


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    promoCode = (By.CSS_SELECTOR, "input[class='promoCode']")
    # self.driver.find_element(By.CSS_SELECTOR, "input[class='promoCode']").send_keys("rahulshettyacademy")
    promoButton = (By.CSS_SELECTOR, "button[class='promoBtn']")
    # self.driver.find_element(By.CSS_SELECTOR, "button[class='promoBtn']").click()
    codeAplliedVerification = (By.XPATH, "//span[text()='Code applied ..!']")
    # codeApllied = self.driver.find_element(By.XPATH, "//span[text()='Code applied ..!']").text
    totalsVerification = (By.XPATH, "//tr/td[5]/p")
    # totals = self.driver.find_elements(By.XPATH, "//tr/td[5]/p")
    amountVerification = (By.CSS_SELECTOR, "span[class='totAmt']")
    # amount = int(self.driver.find_element(By.CSS_SELECTOR, "span[class='totAmt']").text)
    discountVerification = (By.CSS_SELECTOR, "span[class='discountAmt']")



    def promoCode1(self):
        return self.driver.find_element(*CheckoutPage.promoCode)

    def promoButton1(self):
        return self.driver.find_element(*CheckoutPage.promoButton)

    def codeAplliedVerification1(self):
        return self.driver.find_element(*CheckoutPage.codeAplliedVerification)

    def totalsVerification1(self):
        return self.driver.find_elements(*CheckoutPage.totalsVerification)

    def amountVerification1(self):
        return self.driver.find_element(*CheckoutPage.amountVerification)

    def discountVerification1(self):
        return self.driver.find_element(*CheckoutPage.discountVerification)








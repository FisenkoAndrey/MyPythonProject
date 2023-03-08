import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")

class TestFirst(BaseClass):

    def test_end2end(self):

        self.driver.implicitly_wait(4)
        homePage = HomePage(self.driver)
        homePage.sendValue1().send_keys("be")
        time.sleep(2)
        homePage.searchValues1().click()
        list = ['Cucumber - 1 Kg', 'Beetroot - 1 Kg', 'Beans - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
        actualList = []

        pluses = homePage.clickPluses1()
        count = len(pluses)
        print(count)
        assert count > 0
        for plus in pluses:
            plus.find_element(By.XPATH, "a[@class='increment']").click()

        products = homePage.clickProducts1()
        count = len(products)
        print(count)
        assert count > 0
        time.sleep(5)
        for product in products:
            actualList.append(product.find_element(By.XPATH, "h4").text)
            product.find_element(By.XPATH, "div/button").click()

        assert list == actualList
        time.sleep(5)
        homePage.cartClick1().click()
        homePage.proceedToCheckout1().click()

        checkoutPage = CheckoutPage(self.driver)
        checkoutPage.promoCode1().send_keys("rahulshettyacademy")
        checkoutPage.promoButton1().click()
        time.sleep(5)
        codeApllied = checkoutPage.codeAplliedVerification1().text
        print(codeApllied)

        totals = checkoutPage.totalsVerification1()
        totalsSum = len(totals)
        print(totalsSum)
        sum = 0
        for total in totals:
            sum = sum + int(total.text)
        print(sum)
        amount = int(checkoutPage.amountVerification1().text)
        assert sum == amount

        discount = float(checkoutPage.discountVerification1().text)
        assert amount > discount



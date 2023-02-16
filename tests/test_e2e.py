#Imports
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import CommonClass


@pytest.mark.myfile
class TestEndtoEnd(CommonClass):

    def test_e2e(self):
        #Object of all the PO's
        homePage = HomePage(self.driver)
        checkoutPage = CheckoutPage(self.driver)
        confirmPage = ConfirmPage(self.driver)

        #logger object
        log = self.getLogs()


        homePage.shopItem().click()
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        log.info("Getting the titles")

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            log.info(productName + " This is the product ")
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        log.info("Entering country name")
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verifyLink("Indiaa")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        log.info("Getting the alert text for assertion")
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in successText




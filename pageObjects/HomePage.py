from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # Elements
    shop = (By.CSS_SELECTOR, " a[href*='shop']")


    def shopItem(self):
        return self.driver.find_element(*HomePage.shop)

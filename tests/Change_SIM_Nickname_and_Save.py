from tests.base_test import BaseTest


class Test(BaseTest):
    def __init__(self, driver, base_url, module):
        super(Test, self).__init__(driver, base_url, module)

    def run(self):
        """
        Runs the tests. this is what will be getting called by run.py
        """
        self.driver.get(self.base_url)
        (self.driver.find_element_by_id("mobile_number")).send_keys(self.username)
        (self.driver.find_element_by_id("password")).send_keys(self.password)
        (self.driver.find_element_by_xpath(self.submitButtonLocator)).click()
        (self.driver.find_element_by_xpath(self.amaysimLogoLocator)).click()
        self.driver.implicitly_wait(10)
        (self.driver.find_element_by_xpath(self.amaysimLoginLocator)).click()
        self.driver.implicitly_wait(10)
        (self.driver.find_element_by_xpath(self.activatePopUpLocator)).click()
        self.driver.implicitly_wait(30)
        (self.driver.find_element_by_xpath(self.leftNaviagtionMySettingLocator)).click()
        self.driver.implicitly_wait(10)
        (self.driver.find_element_by_xpath(self.editSIMNickNameLocator)).click()
        (self.driver.find_element_by_xpath(self.inputSIMNickNameEditLocator)).clear()
        (self.driver.find_element_by_xpath(self.inputSIMNickNameEditLocator)).send_keys("testuser")
        self.driver.implicitly_wait(30)
        (self.driver.find_element_by_xpath(self.submitButtonLocator)).click()
        
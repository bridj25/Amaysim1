"""A test class for others to inherit to prevent duplicate code."""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


class BaseTest(object):
    def __init__(self, driver, base_url, module):
        """Init

        Parameters
        ----------
        driver : object
            The selenium web driver
        base_url : string
            The base url of the web page we will be visiting.
        module
            The module currently being executed
        """
        self.driver = driver
        self.base_url = base_url
        self.module = module
        self.wait = WebDriverWait(driver, 10)
        self.username = "0468827174"
        self.password = "theHoff34"
        #define xpath here
        self.submitButtonLocator = "//input[@name='commit' and @type='submit']"
        self.amaysimLogoLocator="//div[@class='logo-container']/a[@href='https://www.amaysim.com.au/']"
        self.amaysimLoginLocator="//a[@href='https://www.amaysim.com.au/my-account/my-amaysim/login']"
        self.activatePopUpLocator="//div[@class='road-blocker-container']"
        self.leftNaviagtionMySettingLocator="//a[@href='/my-account/my-amaysim/settings']"
        self.labelSIMNickNameLocator="//div[@class='small-12 columns bold' and contains(text(),'SIM Nickname')]"
        self.setSIMNicknameLocator="//div[@class='small-12 columns bold' and contains(text(),'SIM Nickname')]/following-sibling::div[@class='small-12 columns margin-top-half bold setting-option-details-text']"
        self.editSIMNickNameLocator="//a[@id='edit_settings_phone_label']"
        self.inputSIMNickNameEditLocator="//input[@id='my_amaysim2_setting_phone_label']"
        self.buttonSIMNickNameCancelEditLocator="//a[@id='show_settings_sim_nickname']"
        self.editRechargePINLocator="//a[@id='edit_settings_recharge_pin']"
        self.inputRechargePINEditLocator="//input[@id='my_amaysim2_setting_topup_pw']"
        self.buttonRechargePINCancelEditLocator="//a[@class='grey text-center medium-text-right' and contains(text(),'Cancel')]"
        self.labelRechargePINLocator="//div[@class='small-12 columns bold' and contains(text(),'Recharge PIN')]"
        self.setRechargePINLocator="//div[@class='small-12 columns bold' and contains(text(),'Recharge PIN')]/following-sibling::div[@class='small-12 columns margin-top-half bold setting-option-details-text']"
        self.editCallFrwdingLocator="//a[@id='edit_settings_call_forwarding']"
        self.labelCallFrwdingLocator="//div[@class='small-12 columns bold' and contains(text(),'Recharge PIN')]"
        self.setCallFrwdingLocator="//div[@class='small-12 columns bold setting-option-details-text' and contains(text(),'Forward calls to')]"
        self.buttonPopUpconfirmLocator="//a[@class='confirm_popup_confirm button-green-action small-12 columns text-center']"
        self.buttonPopUpcancelLocator="//a[@class='confirm_popup_cancel close-reveal-modal ama-grey grey small-12 columns text-left padding-left margin-left']"
        self.radioCallFrwdNoLocator="//label[@class='radio small-6 columns']/span[text()='No']"
        self.radioCallFrwdYesLocator="//label[@class='radio small-6 columns']/span[text()='Yes']"
        self.popUpSuccessChangeLocator="//h1[@class='ama-hero-heading popup-success white']"
        self.popUpSuccessChangeXLocator="//a[@class='close-reveal-modal']"
        self.labelRoamingLocator="//div[@class='small-8 columns bold padding-top-q' and contains(text(),'International roaming')]"
        self.labelAutoRechargeLocator="//div[@class='small-12 columns bold' and contains(text(),'Auto-recharge')]"
        
        
    def confirm_in_url(self, path):
        """Confirm the path appears in the URL

        Parameters
        -------------
        path: string
            The string that should appear in the URL
        """
        if(self.keep_trying(lambda: (True if path not in self.driver.current_url else False),
           fallback=True, unsatisfactory=True)):
            self.failed("We did not end up on the " + path + " page when we should have")


    def Page_Should_Contain_Element(self, xpath):
        """Confirm the path appears in the URL

        Parameters
        -------------
        xpath: string
        xpath of element that should be in the page
        """
    
        page_wrap = self.check_exists_by_xpath(xpath)

        if page_wrap == False:
            self.failed(xpath + " did not appear in the page")
    
    def check_exists_by_xpath(self, xpath):    
        
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        
        return True


    def confirm_in_page(self, text, page_class):
        """Confirm the path appears in the URL

        Parameters
        -------------
        text: string
            The string that should appear in the page
        page_class: string
            The page class used for identifying the search area
        """
        page_wrap = self.keep_trying(lambda: self.driver.find_element(By.CLASS_NAME, page_class))

        if(self.keep_trying(lambda: (True if text not in page_wrap.text else False),
           fallback=True, unsatisfactory=True)):
            self.failed(text + " did not appear in the page")

    def failed(self, error_message):
        """Print a generic message when a test has failed, take a screenshot and end the test.
        Parameters
        ----------
        error_message : string
            A message describing what went wrong with the test.
        """
        print("Failed: " + self.module  + ": " + error_message)
        self.take_screenshot()
        self.driver.quit()
        exit()

    def keep_trying(self, function, attempts=60, fallback=None, unsatisfactory=None):
        """Continues to try the function without errors for a number of attempts before continuing. This solves
        The problem of Selenium being inconsistent and erroring out because a browser is slow.

        Parameters
        ----------
        assertion : lambda
            A lambda function that should at some point execute successfully.
        attempts : Integer
            The number of attempts to keep trying before letting the test continue
        unsatisfactory : Any
            Value that is unsatisfactory as a return value
        fallback : Any
            The fallback return value if the function did return a satisfactory value within the given
            number of attempts.

        Returns the return value of the function we are trying.
        """
        for i in xrange(attempts):
            try:
                result = function()
                # It will only return if the assertion does not throw an error
                if(result is not unsatisfactory): return result
            except:
                pass
            time.sleep(1)  # This makes the function wait a second between attempts

        return fallback

    def passed(self):
        """Print a generic message when a test has passed
        """
        print("Passed: " + self.module)

    def take_screenshot(self):
        """Take a screenshot with a defined name based on the time and the browser"""
        millis = int(round(time.time() * 1000))
        if(self.driver.name):
            driver_name = self.driver.name
        else:
            driver_name = ""
        self.driver.save_screenshot("screenshots/" + driver_name + "-" + str(millis) + "-screenshots.png")

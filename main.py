"""
    Author: Shahram Khalid
    Date: 2nd of February, 2020
    Day: Sunday
    Version: 1.0
    Description: This script can be used to automate sending SMS via Google Messages.
                 coming update can be Used for bulk messaging.
                 You must have Google Messages installed on your phone to use this script.
                 This script is powered by Selenium and Python
                 Feel free to contribute in this open source project.
                 Description on how to use this script will be posted soon.
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from keyboard import press
from time import sleep


class AutoSMS:
    phone_number_to_send_sms_to = "03001234567"
    message = '''
        Testing: This is an automated message.
    '''

    SIM_to_use = 'telenor'

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get("https://messages.google.com/web")

    start_chat_button = '''/html/body/mw-app/div/main/mw-main-container/div[1]/mw-main-nav/div/mw-fab-link/a/span/div[2]'''
    confirm_send_sms_to = '''/html/body/mw-app/div/main/mw-main-container/div[1]/mw-new-conversation-container/div/mw-contact-selector-button/button'''
    select_sim_button = '''/html/body/mw-app/div/main/mw-main-container/div[1]/mw-conversation-container/div/div/mws-message-compose/div/div[2]/div/mws-sim-info-picker/button'''
    type_sms_here = '''/html/body/mw-app/div/main/mw-main-container/div[1]/mw-conversation-container/div/div/mws-message-compose/div/div[2]/div/mws-autosize-textarea/textarea'''

    def __init__(self, sim_to_send_from, send_msg_to_number, msg_to_send):
        self.phone_number_to_send_sms_to = send_msg_to_number
        self.message = msg_to_send
        self.SIM_to_use = sim_to_send_from
        self.algorithm(self)

    @classmethod
    def waitForElement(self, xpath: str):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
        except:
            pass

    @classmethod
    def findElement(self, xpath: str) -> bool:
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    @classmethod
    def useSIM(self, SIM: str):
        sim1_telenor_27 = '''//*[@id="mat-menu-panel-27"]/div/button[1]'''
        sim2_ufone_27 = '''//*[@id="mat-menu-panel-27"]/div/button[2]'''
        sim1_telenor_28 = '''//*[@id="mat-menu-panel-28"]/div/button[1]'''
        sim2_ufone_28 = '''//*[@id="mat-menu-panel-28"]/div/button[2]'''
        if SIM == 'telenor':
            if self.findElement(sim1_telenor_27):
                self.waitForElement(sim1_telenor_27)
                self.driver.find_element_by_xpath(sim1_telenor_27).click()
            else:
                self.waitForElement(sim1_telenor_28)
                self.driver.find_element_by_xpath(sim1_telenor_28).click()
        elif SIM == 'ufone':
            if self.findElement(sim2_ufone_27):
                self.waitForElement(sim2_ufone_27)
                self.driver.find_element_by_xpath(sim2_ufone_27).click()
            elif self.findElement(sim2_ufone_28):
                self.waitForElement(sim2_ufone_28)
                self.driver.find_element_by_xpath(sim2_ufone_28).click()

    @staticmethod
    def algorithm(self):
        self.waitForElement(self.start_chat_button)
        self.driver.find_element_by_xpath(self.start_chat_button).click()

        send_sms_to = '''//*[@id="mat-chip-list-0"]/div/input'''
        self.waitForElement(send_sms_to)
        self.driver.find_element_by_xpath(send_sms_to).send_keys(self.phone_number_to_send_sms_to)

        self.waitForElement(self.confirm_send_sms_to)
        self.driver.find_element_by_xpath(self.confirm_send_sms_to).click()

        self.waitForElement(self.select_sim_button)
        self.driver.find_element_by_xpath(self.select_sim_button).click()

        self.useSIM('telenor')

        self.waitForElement(self.type_sms_here)
        self.driver.find_element_by_xpath(self.type_sms_here).send_keys(self.message)

        press("enter")

        sleep(10)
        self.driver.quit()


autoSMSobject = AutoSMS('telenor', '03314450555', 'message')

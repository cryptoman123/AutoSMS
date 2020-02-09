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

phone_number_to_send_sms_to = "+923001234567"
message = '''
    This is where you type your message
'''

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from keyboard import press
from time import sleep

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://messages.google.com/web")


def waitForElement(xpath:str):
    try:
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        pass

def findElement(xpath:str)->bool:
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def useSIM(SIM:str):
    sim1_telenor_27 = '''//*[@id="mat-menu-panel-27"]/div/button[1]'''
    sim2_ufone_27 = '''//*[@id="mat-menu-panel-27"]/div/button[2]'''
    sim1_telenor_28 = '''//*[@id="mat-menu-panel-28"]/div/button[1]'''
    sim2_ufone_28 = '''//*[@id="mat-menu-panel-28"]/div/button[2]'''
    if SIM == 'telenor':
        if findElement(sim1_telenor_27):
            waitForElement(sim1_telenor_27)
            driver.find_element_by_xpath(sim1_telenor_27).click()
        else:
            waitForElement(sim1_telenor_28)
            driver.find_element_by_xpath(sim1_telenor_28).click()
    elif SIM == 'ufone':
        if findElement(sim2_ufone_27):
            waitForElement(sim2_ufone_27)
            driver.find_element_by_xpath(sim2_ufone_27).click()
        elif findElement(sim2_ufone_28):
            waitForElement(sim2_ufone_28)
            driver.find_element_by_xpath(sim2_ufone_28).click()

start_chat_button = '''/html/body/mw-app/div/main/mw-main-container/div[1]/mw-main-nav/div/mw-fab-link/a/span/div[2]'''
waitForElement(start_chat_button)
driver.find_element_by_xpath(start_chat_button).click()

send_sms_to = '''//*[@id="mat-chip-list-0"]/div/input'''
waitForElement(send_sms_to)
driver.find_element_by_xpath(send_sms_to).send_keys(phone_number_to_send_sms_to)

confirm_send_sms_to = '''/html/body/mw-app/div/main/mw-main-container/div[1]/mw-new-conversation-container/div/mw-contact-selector-button/button'''
waitForElement(confirm_send_sms_to)
driver.find_element_by_xpath(confirm_send_sms_to).click()

select_sim_button = '''/html/body/mw-app/div/main/mw-main-container/div[1]/mw-conversation-container/div/div/mws-message-compose/div/div[2]/div/mws-sim-info-picker/button'''
waitForElement(select_sim_button)
driver.find_element_by_xpath(select_sim_button).click()

useSIM('ufone')

type_sms_here = '''/html/body/mw-app/div/main/mw-main-container/div[1]/mw-conversation-container/div/div/mws-message-compose/div/div[2]/div/mws-autosize-textarea/textarea'''
waitForElement(type_sms_here)
driver.find_element_by_xpath(type_sms_here).send_keys(message)

press("enter")

sleep(10)
driver.quit()

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
class SWait:
    def __init__(self, driver):
        self.driver = driver
    
    # By Xpath 
    def get_element_by_xpath(self,limit_time,xpath):
        try:
            WebDriverWait(self.driver, limit_time).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element_by_xpath(xpath)
        except TimeoutException as exception: 
            return 'timeout'
    def get_elements_by_xpath(self,limit_time,xpath):
        try:
            WebDriverWait(self.driver, limit_time).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return self.driver.find_elements_by_xpath(xpath)
        except TimeoutException as exception: 
            return 'timeout'
    def click_by_xpath(self,limit_time,xpath):
        try:
            WebDriverWait(self.driver, limit_time).until(EC.visibility_of_element_located((By.XPATH, xpath))).click()
            return 'success'
        except TimeoutException as exception: 
            return 'timeout'
            
    def send_keys_by_xpath(self,limit_time,xpath,text):
        try:
            WebDriverWait(self.driver, limit_time).until(EC.visibility_of_element_located((By.XPATH, xpath))).send_keys(text)
            return 'success'
        except TimeoutException as exception: 
            return 'timeout'
    def get_attribute_by_xpath(self,limit_time,xpath,attribute):
        try:
            str = WebDriverWait(self.driver, limit_time).until(EC.visibility_of_element_located((By.XPATH, xpath))).get_attribute(attribute)
            return str if str != None else 'attribute_not_found'
        except TimeoutException as exception: 
            return 'timeout'
    def wait_until_by_xpath(self,limit_time,xpath):
        try:
            WebDriverWait(self.driver, limit_time).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            return 'success'
        except TimeoutException as exception: 
            return 'timeout'
            
    # By ID 
    def click_by_id(self,limit_time,id):
        try:
            WebDriverWait(self.driver, limit_time).until(EC.visibility_of_element_located((By.ID, id))).click()
            return 'success'
        except TimeoutException as exception: 
            return 'timeout'
    def send_keys_by_id(self,limit_time,id,text):
        try:
            WebDriverWait(self.driver, limit_time).until(EC.visibility_of_element_located((By.ID, id))).send_keys(text)
            return 'success'
        except TimeoutException as exception: 
            return 'timeout'
    def get_attribute_by_id(self,limit_time,id,attribute):
        try:
            str = WebDriverWait(self.driver, limit_time).until(EC.visibility_of_element_located((By.ID, id))).get_attribute(attribute)
            return str if str != None else 'attribute_not_found'
        except TimeoutException as exception: 
            return 'timeout'
    def switch_to_frame_by_id(self,limit_time,id):
        try:
            WebDriverWait(self.driver, limit_time).until(EC.frame_to_be_available_and_switch_to_it((By.id,id)))
            return 'success'
        except TimeoutException as exception: 
            return 'timeout'
    def wait_until_by_xpath(self,limit_time,id):
        try:
            WebDriverWait(self.driver, limit_time).until(EC.visibility_of_element_located((By.ID,id)))
            return 'success'
        except TimeoutException as exception: 
            return 'timeout'
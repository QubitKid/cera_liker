
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import math
from cryptography.fernet import Fernet

driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')

email_input = driver.find_element_by_name('email')
password_input = driver.find_element_by_name('pass')


key = open("secret.key", "rb").read()
f = Fernet(key)
dec_password =  f.decrypt() #place secret key to decrypt here but not public

password_input.send_keys(dec_password.decode())
email_input.send_keys(). # facebook email address goes here in parentheses
email_input.send_keys(Keys.RETURN)
password_input.send_keys(Keys.RETURN)


#sleep so the page has time to load
time.sleep(8)

#search
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/label/input"))).send_keys('The Same Photo of Micheal Cera')
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/div/div/div/label/input"))).send_keys(Keys.RETURN)

time.sleep(8)
page_link = driver.find_element_by_link_text('The Same Photo of Michael Cera Every Day')
page_link.click()

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/a[3]/div[1]"))).click()
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[4]/div/div/div[3]/div/div/div/div[2]/div[1]/div/a/div/div/img"))).click()

#like the picture
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div[1]"))).click()

#comment
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[5]/div/div[2]/div/div/div/div/form/div/div/div[2]/div"))).send_keys('King (Python Response)')
confirm = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[3]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[5]/div/div[2]/div/div/div/div/form/div/div/div/div')
confirm.send_keys(Keys.ENTER)
driver.close()

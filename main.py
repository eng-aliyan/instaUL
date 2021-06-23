#!/usr/bin/python3

from selenium import webdriver
from time import sleep

#username = input('user: ')
username = 'amirh._.aliyan'

#password = input('pass: ')
password = 'CIV8kvub3z'

#account = input('IG id: ')
account = 'zahrahairstyl'

url = 'https://www.instagram.com/%s/followers/'
inPath = '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[%d]/div/label/input'

driver = webdriver.Firefox()
driver.get('https://www.instagram.com/')
sleep(2)

driver.find_element_by_xpath(inPath %1).send_keys(username)
driver.find_element_by_xpath(inPath %2).send_keys(password)
login = driver.find_element_by_xpath(
    '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
login.click()
sleep(3)

driver.get(url %account)
sleep(2)

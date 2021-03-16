import os, sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time 
from time import sleep
import pytest
from pytest import ExitCode
import unittest

link='http://suninjuly.github.io/registration1.html' 

def first(link):
    
    browser = webdriver.Chrome("C:\\Users\\Avdoshkina.T\\chromedriver")
    browser.implicitly_wait(7)    
    browser.get(link)    

    firstname=browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.first_class > input")    
    firstname.send_keys("FirstName")    
    #assert firstname!="FirstName", "no1"  
    #test_iinput("FirstName",firstname)    

    Lastname=browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.second_class > input")    
    Lastname.send_keys("LastName")    
    #assert Lastname!="LastName", "no2"    

    #test_input("LastName",Lastname)   

    email=browser.find_element_by_css_selector("body > div > form > div.first_block > div.form-group.third_class > input")    
    email.send_keys("FirstName@mail.com")    
    #assert email!="FirstName@mail.com", "error3"

    sub1=browser.find_element_by_css_selector("body > div > form > button")    
    sub1.click()    
    # находим элемент, содержащий текст

    welcome_text_elt = browser.find_element_by_tag_name("h1")    
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text  
    return (welcome_text)
    #print(result)
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text  
first(link)
    #print(ExitCode)

  

   
time.sleep(2)    
    
    #browser.quit()

from selenium import webdriver
import time 
navegador = webdriver.Chrome()
navegador.get('https://www.netflix.com/br/')
navegador.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div/div/div/div[1]/div/a').click()
time.sleep(3)
navegador.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[2]/div[1]/a').click()
time.sleep(2)
navegador.find_element_by_xpath('//*[@id="id_email_hero_fuji"]').click
navegador.find_element_by_xpath('//*[@id="id_email_hero_fuji"]').send_keys('anonimo@gmail.com')
navegador.find_element_by_xpath('//*[@id="appMountPoint"]/div/div/div/div/div/div[2]/div[1]/div[2]/form/div/div/button/span[1]').click()
   


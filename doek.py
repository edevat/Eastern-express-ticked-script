import time
import unittest
import sys
import pygame.mixer
import os

from pygame.mixer import *
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.quit()
pygame.mixer.init()
fpsTime = pygame.time.Clock()
fpsTime.tick(60)

from array import array
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.errorhandler import ErrorHandler


"""
kütüphaneleri nmp install v.b ile kurmalısınız
"""

print "basliyom"
browser = webdriver.Chrome("chromedriver.exe") #selenium için chromedriver
browser.get('https://ebilet.tcddtasimacilik.gov.tr')
WebDriverWait(browser,10000).until(EC.visibility_of_element_located((By.TAG_NAME,'body')))


while 1:	
	nereden = browser.find_element_by_id('nereden')
	nereye = browser.find_element_by_id('nereye')
	trh = browser.find_element_by_id('trCalGid_input')
	ys = browser.find_element_by_xpath("//span[@class='ui-icon ui-icon-triangle-1-n']")
	if not nereden.get_attribute('value'):
		ys.click()
		ys.click()
		ys.click()
	nereden.clear()
	nereden.send_keys("Ankara Gar")
	nereye.clear()	
	nereye.send_keys("Kars")
	trh.clear()	
	trh.send_keys("23.01.2019")	#bilet aranan tarih
	
	btn = browser.find_element_by_id('btnSeferSorgula')	
	browser.execute_script("arguments[0].click();", btn)
	time.sleep(5)
	try:
		element = browser.find_element_by_id('btnSeferSorgula')
		print("yok.s.s")
	except NoSuchElementException:
		pygame.mixer.music.load('at.mp3') #uyarı sesi
		pygame.mixer.music.play(0)
		while pygame.mixer.music.get_busy():
			print('AL')
			
		
	

	
	
	



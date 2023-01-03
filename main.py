from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time
from intcomp import intspeedtweet
chrome_driver_path="C:/Users/arora/OneDrive/Desktop/chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)

x=intspeedtweet()

x.tweet()
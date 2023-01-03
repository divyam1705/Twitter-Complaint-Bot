from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time
twittermail="divyam1705"
twitterpass=""
chrome_driver_path="C:/Users/arora/OneDrive/Desktop/chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)
class intspeedtweet:
    def __init__(self,up=None,down=None):
        self.down=down
        self.up=up

    def get_int_speed(self):
        driver.get("https://www.speedtest.net/")
        go=driver.find_element_by_class_name("start-text")
        go.click()
        time.sleep(45)
        self.down=float(driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.up=float(driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)
        print(self.down)
        print(self.up)
        driver.quit()
    def tweet(self):
        driver.get("https://twitter.com/home?lang=en-in")
        time.sleep(11)
        id=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        id.send_keys(twittermail)
        next=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div')
        next.click()
        time.sleep(2)
        pass1=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        pass1.send_keys(twitterpass)

        subm=driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
        subm.click()
        time.sleep(4)
        inbox=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        inbox.send_keys(f"Hey internet provider why is my int speed ** when I pay for (idkwhat).\n so this is a twitter complaint bot, whenever my internet speed gets below a certain point it tweets and tags the company")
        submit=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        submit.click()
        driver.quit()
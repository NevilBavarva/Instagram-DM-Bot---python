from selenium import webdriver
from time import sleep


driver = webdriver.Chrome('location of your chromedriver application')


Name = 'Username'
pas = 'Password'

class instabot:
    def __init__(self , username , pw):
        self.driver = webdriver.Chrome()
        self.driver.get('https://instagram.com')
        self.Name = Name
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(Name)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pas)
        self.driver.find_element_by_xpath("//button[@type='submit']")\
            .click()
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text() , 'Not Now')]")\
            .click()
        sleep(5)
        # It will click on dm svg icon
        self.driver.find_element_by_xpath("//a[@class='xWeGp']")\
            .click()
        sleep(5)
        # It will select the user and open its messaging panel
        self.driver.find_element_by_xpath("//div[contains(text(), 'Username of user you want to DM')]")\
            .click()
        sleep(1)

        ## messages to send ....
        counterindex = 0
        mesglist= ['messages', 'your', 'want', 'to', 'send', 'to', 'user']
        
        j=0
        number_of_times_you_want_to_send_single_word_from_mesglist =0
        while(counterindex !=len(mesglist)):
            while(j!=number_of_times_you_want_to_send_single_word_from_mesglist):
                self.driver.find_element_by_xpath("//textarea[@placeholder='Message...']")\
                    .send_keys(mesglist[counterindex])
                sleep(1)
                self.driver.find_element_by_xpath("//button[contains(text() , 'Send')]")\
                        .click()
                sleep(1)
                j=j+1
            
            counterindex = counterindex + 1
            j=0
           
  



       

mybot = instabot(Name,pas)

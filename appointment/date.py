import random
import threading
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# below to handle properly filling input field
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .reading import ReadWrite # to read inputed file
from .output import write_result
import pyautogui as pg # this is for mouse move and take action like human pip install pyautogui "print(pg.position())" "pg.moveTo(728, 906, 2)"


class UsaDate:
    service_obj = Service(ChromeDriverManager().install())
    # service_obj = Service(os.path.join('appointment/chromedriver.exe'))
    options = Options()

    options.add_experimental_option("excludeSwitches", ["enable-automation"])  # one
    options.add_experimental_option('useAutomationExtension', False)  # two
    options.add_argument('--disable-blink-features=AutomationControlled')  # three  these three option is called "Removing Navigator.Webdriver Flag"
    options.add_argument('--disable-notifications')  # one this is to stop showing notificationn like "Save password" (working)
    prefs = {"profile.default_content_setting_values.notifications": 2}  # two
    options.add_experimental_option("prefs", prefs)  # three above three lines of code ignoring the "Save password" popup from chrome (called browser notifictaion)
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    def __init__(self):
        pass

    def delay(self):
        time.sleep(random.randint(2, 4))

    def wait60sec(self, driver):
        driver.implicitly_wait(60)

    def read_csv(self):
        read = ReadWrite()
        self.user_list = read.data_list
        read.read_data()



    def login(self, user_name, pass_word, driver):
        '''This method is suppose to solve login and login captcha problem'''
        driver.implicitly_wait(2)
        time.sleep(5)
        email = driver.find_element(By.XPATH, "//input[@class='stylizedInput1']")
        print(user_name)
        time.sleep(2)
        email.send_keys(user_name)
        time.sleep(2)
        password = driver.find_element(By.XPATH, "//input[@type='password']")
        time.sleep(2)
        password.send_keys(pass_word)
        time.sleep(5)
        pg.moveTo(1006, 645, 2) # go to the checkbox
        driver.find_element(By.XPATH, "//input[@type='checkbox']").click()  # click on check box
        #form data mission country name
        # mission = driver.find_element(By.XPATH, "//input[@id='Mission']")
        # driver.execute_script("arguments[0].setAttribute('value','GJZ8UZVM+guclLYeCIytdQ==')", mission)
        # print(mission.get_attribute('value'))
        # country = driver.find_element(By.XPATH, "//input[@id='Country']")
        # driver.execute_script("arguments[0].setAttribute('value', 'LuPeffehutdAFt+0k6EVBw==')", country)
        # print(country.get_attribute('value'))

        self.delay()
        driver.implicitly_wait(5)
        time.sleep(30) # here the waiting is for manual captcha input
        pg.moveTo(728, 906, 2) # go to the loginbutton
        driver.find_element(By.XPATH, "//input[@type='submit']").click() # clicked on Login button

    def pick_time(self, driver):
        '''this method will check time check box'''
        driver.find_element(By.XPATH, "//input[@type='checkbox']").click()

        # now submit the schedule appointment button
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='thePage:SiteTemplate:theForm:addItem']").click()

    def repeat_work(self, driver):
        # first click on reschedule link
        self.wait60sec(driver)
        self.delay()
        reschedule_button = driver.find_element(By.XPATH, "//li/a[text()='Reschedule Appointment']")
        reschedule_button.click()

        #  Now search for the desired month value
        while True:
            try:
                first_group = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-group ui-datepicker-group-first']")
                year_value = first_group.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text.strip()
                if year_value == '2022':
                    month_value = first_group.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text.strip()
                    if month_value == 'April':
                        date_list = first_group.find_elements(By.XPATH, "//td[@class=' ']")
                        for date in date_list:
                            date_value = date.find_element(By.XPATH, "//a[@class='ui-state-default']").text.strip()
                            if date_value == '21':
                                date_button = date.find_element(By.XPATH, "//a[@class='ui-state-default']")
                                date_button.click()
                                break;
            except:
                time.sleep(30)
                driver.refresh()


        # Now select time button





    def pickdate(self, user_name, pass_word):
        driver = webdriver.Chrome(service=self.service_obj, options=self.options)
        driver.maximize_window()

        self.wait60sec(driver)
        driver.get('https://cgifederal.secure.force.com/?language=English&country=Bangladesh')
        self.login(user_name, pass_word, driver) # loggedIn from here
        driver.get_cookies()
        time.sleep(10)
        self.repeat_work(driver)
        self.pick_time(driver)
        data = [user_name, pass_word]
        write_result(data)

    def run(self):
        self.read_csv()
        for line in self.user_list:
            # print("line")
            # if line["status"] == '1':
            #     print("line completed")
            #     continue
            user_name = line['User Name'].strip()
            pass_word = line['Password'].strip()

            # starting here
            t = threading.Thread(target=self.pickdate, args=(user_name, pass_word))
            # time.sleep(3)
            t.start()
            time.sleep(30)
            break;










# =============== run the script =====#
# if __name__ =='__main__':
#     bot = UsaDate()
#     bot.run()

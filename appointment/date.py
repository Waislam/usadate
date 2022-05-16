import random
import threading
import os
import time
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# below to handle properly filling input field
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appointment.reading import ReadWrite # to read inputed file
from appointment.output import write_result
import pyautogui as pg # this is for mouse move and take action like human pip install pyautogui "print(pg.position())" "pg.moveTo(728, 906, 2)"

#hacapsol CNN
from appointment.mycnn import Capsol

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
        time.sleep(random.randint(2, 3))

    def wait60sec(self, driver):
        driver.implicitly_wait(60)

    def read_csv(self):
        read = ReadWrite()
        self.user_list = read.data_list
        read.read_data()

    def cnnsol(self):
        cnn = Capsol()
        solution = cnn.hcap()
        return solution

    def download_img(self, src):
        '''method to download img from hcaptcha and read that'''
        rq = requests.get(src)
        filename = os.path.join('appointment/new.jpg')
        with open(filename, 'wb') as f:
            f.write(rq.content)

    def click_on_image(self, driver):
        ''' this method supposed  to click on hcaptcha images'''
        time.sleep(1.5)
        header_text = driver.find_element(By.XPATH, "//div[@class='prompt-text']").text.strip().split(' ')[-1].strip()
        print(header_text)

        wrapper_list = driver.find_elements(By.XPATH, "//div[@class='task-image']")

        for wrapper in wrapper_list:
            img_url = wrapper.find_element(By.XPATH, ".//div[@class='image-wrapper']/div[@class='image']")  # .value_of_css_property('background'))
            absolute_url = img_url.value_of_css_property('background').lstrip('url("').rstrip('") 50% 50% / 120px 120px no-repeat;')
            ##position: absolute; top: 50%; left: 50%; z-index: 5; width: 120px; height: 120px; margin-left: -60px; margin-top: -60px; background: url("https://imgs.hcaptcha.com/hkU58HCFb0rUffs2pbe0mrzH2Hj1KZjVgM0wEhoGhzxVlxtU3DKn3KFx2AgJgHpKvXSiHbaPpdB/bdOm8l/ELy5xX7OlZjEpFgXwA1iOSwdo4FXV9cwWQ1fVEjeFd6z1Aqv589X++mDFfKw1rZWrMfBQl1oFQBIjwbGYYqCRx8bawGCZIqanjLMtP10=YqWJHLWg/GU+jTrl") 50% 50% / 120px 120px no-repeat;
            # print(absolute_url)
            # ls = absolute_url.lstrip('gba(0, 0, 0, 0) url("')
            ls = absolute_url.lstrip('gba(0, 0, 0, 0) url(')
            # rs = ls.rstrip('") no-repeat scroll 50% 50% / 123.333px 123.333px padding-box border-b')
            rs = ls.rstrip(') no-repeat scroll 50% 50% / 123.333px 123.333px padding-box border-b')
            src = rs.strip('"')

            time.sleep(0.1)
            self.download_img(src)
            ###################################################### check from here
            time.sleep(1)
            img_id = str(self.cnnsol())
            print('Everything working')
            img_id = img_id.strip()
            print(img_id)

            time.sleep(1)

            if header_text == 'motorbus':
                print('motorbus')
                if img_id == '0':
                    wrapper.click()
                    print('clicked')
                    time.sleep(1)

            elif header_text == 'motorcycle':
                print('motorcycle')
                if img_id == '1':
                    wrapper.click()
                    print('clicked')
                    time.sleep(1)

            elif header_text == 'airplane':
                print('airplane')
                if img_id == '2':
                    wrapper.click()
                    print('clicked')
                    time.sleep(1)

            elif header_text == 'truck':
                print('truck')
                if img_id == '3':
                    wrapper.click()
                    print('clicked')
                    time.sleep(1)

            elif header_text == 'bicycle':
                print('bicycle')
                if img_id == '4':
                    wrapper.click()
                    print('clicked')
                    time.sleep(1)

            elif header_text == 'seaplane':
                print('seaplane')
                if img_id == '5':
                    wrapper.click()
                    print('clicked')
                    time.sleep(1)

            elif header_text == 'boat':
                print('boat')
                if img_id == '6':
                    wrapper.click()
                    print('clicked')
                    time.sleep(1)

            elif header_text == 'train':
                print('train')
                if img_id == '7':
                    wrapper.click()
                    print('clicked')
                    time.sleep(1)

            else:
                print('else close executed')
                continue;

    def hcapsolution(self, driver):
        '''this is the method to solve hcaptcha'''
        # capsol = HcapSolution()
        # capsol.runhcap(driver)
        self.delay()
        driver.implicitly_wait(2)
        iframe = driver.find_element(By.XPATH, "//iframe[@title='widget containing checkbox for hCaptcha security challenge']")
        driver.switch_to.frame(iframe)
        # self.delay()
        time.sleep(2)
        check_box = driver.find_element(By.XPATH, "//div[@id='checkbox']")
        #print(pg.position()) #Point(x=732, y=715)
        #pg.moveTo(732, 715, 1)
        check_box.click() # clicked on the check box of hcaptcha



        print(' 1st in the hcap')
        #============================wiating time
        time.sleep(2)
        #=======================waiting time end


        # switch to iframe of hcaptcha image content(main content)
        driver.switch_to.default_content()
        iframe_image = driver.find_element(By.XPATH, "//iframe[@title='Main content of the hCaptcha challenge']")
        driver.switch_to.frame(iframe_image) # switched to the captcha image content
        driver.implicitly_wait(5)
        # self.delay()
        # header_text = driver.find_element(By.XPATH, "//div[@class='prompt-text']").text.strip().split(' ')[-1].strip()
        # print(header_text)
        #clear till this line
        self.delay()
        while True:
            try:
                time.sleep(2)
                driver.implicitly_wait(5)
                self.click_on_image(driver)
                #value_of_css_property("background-image")
                # bg_url = div.value_of_css_property('background-image')  # 'url("https://i.xxxx.com/img.jpg")'
                # # strip the string to leave just the URL part
                # bg_url = bg_url.lstrip('url("').rstrip('")')
                # https://i.xxxx.com/img.jpg

                time.sleep(3)
                next_challenge = driver.find_element(By.XPATH, "//div[@title='Next Challenge']")
                next_challenge.click()
                driver.implicitly_wait(5)
                self.delay()
                self.click_on_image(driver)
                driver.implicitly_wait(5)
                self.delay()
                verify_button = driver.find_element(By.XPATH, "//div[@title='Submit Answers']")
                verify_button.click()
                print('verified button is clicked')
            except:
                print('no more captcha')
                # print(e)
                break;

        time.sleep(1)


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
        time.sleep(2)
        #pg.moveTo(1006, 645, 2) # go to the policy checkbox
        driver.find_element(By.XPATH, "//input[@type='checkbox']").click()  # click on check box
        #form data mission country name
        # mission = driver.find_element(By.XPATH, "//input[@id='Mission']")
        # driver.execute_script("arguments[0].setAttribute('value','GJZ8UZVM+guclLYeCIytdQ==')", mission)
        # print(mission.get_attribute('value'))
        # country = driver.find_element(By.XPATH, "//input[@id='Country']")
        # driver.execute_script("arguments[0].setAttribute('value', 'LuPeffehutdAFt+0k6EVBw==')", country)
        # print(country.get_attribute('value'))

        time.sleep(1)
        driver.implicitly_wait(5)
        # here the waiting is for manual captcha input
        ##########===========================captcha solve start===============
        # now it is time to solve hcaptcha
        while True:
            driver.implicitly_wait(5)
            self.delay()
            try:
                self.hcapsolution(driver)
            except:
                print('There is no captcha or captcha is solved')
                time.sleep(2)
                break;
        driver.switch_to.default_content()
        ##########===========================captcha solve start===============

        #=======================click on login button start=========================
        # pg.moveTo(728, 906, 2) # go to the loginbutton
        driver.find_element(By.XPATH, "//input[@type='submit']").click() # clicked on Login button
        # =======================click on login button end=========================

    def pick_time(self, driver):
        '''this method will check time check box'''
        driver.find_element(By.XPATH, "//input[@type='checkbox']").click()

        # now submit the schedule appointment button
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='thePage:SiteTemplate:theForm:addItem']").click()

    def repeat_work(self, driver, year, month, month2):
        # first click on reschedule link
        self.wait60sec(driver)
        self.delay()
        reschedule_button = driver.find_element(By.XPATH, "//li/a[text()='Reschedule Appointment']")
        reschedule_button.click()

        #===========================here capcha solution start==========================

        #===========================here capcha solution end==========================

        #  Now search for the desired month value
        while True:
            time.sleep(1)
            try:
                # try:
                #     while True:
                #         error = driver.find_element(By.XPATH, "//span[@style='font-family: Verdana; font-size: medium; font-weight: bold;']").text.strip()
                #         if error == 'We are down for maintenance.':
                #             time.sleep(30)
                #             driver.refresh()
                # except:
                while True:
                    try:
                        self.hcapsolution(driver)
                        driver.switch_to.default_content()
                        time.sleep(1)
                        driver.find_element(By.XPATH, "//input[@class='button']").click()
                        time.sleep(2)
                    except:
                        print('repeat captcha not here')
                        break;

                first_group = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-group ui-datepicker-group-first']")
                year_value = first_group.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text.strip()
                print('working till here')
                if year_value == year:
                    print(year)
                    month_value = first_group.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text.strip()
                    if month_value == month or month_value == month2:
                        date_list = first_group.find_elements(By.XPATH, "//td[@class=' ']")

                        #click on first date from this month
                        date_list[0].click()
                        break;

                        # # for date in date_list:
                        # #     date_value = date.find_element(By.XPATH, "//a[@class='ui-state-default']").text.strip()
                        # #     if date_value == '21':
                        # #         date_button = date.find_element(By.XPATH, "//a[@class='ui-state-default']")
                        # #         date_button.click()
                        #         break;
            except:
                time.sleep(30)
                print('what is happennig here')
                # driver.refresh()
                reschedule_button = driver.find_element(By.XPATH, "//li/a[text()='Reschedule Appointment']")
                reschedule_button.click()


        # Now select time button





    def pickdate(self, user_name, pass_word, year, month, month2):
        driver = webdriver.Chrome(service=self.service_obj, options=self.options)
        driver.maximize_window()

        self.wait60sec(driver)
        driver.get('https://cgifederal.secure.force.com/?language=English&country=Bangladesh')
        self.login(user_name, pass_word, driver) # loggedIn from here
        driver.get_cookies()
        time.sleep(10)
        self.repeat_work(driver, year, month, month2)
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
            year = line['Year'].strip()
            month = line['Month'].strip()
            month2 = line['Month2'].strip()

            # starting here
            t = threading.Thread(target=self.pickdate, args=(user_name, pass_word, year, month, month2))
            # time.sleep(3)
            t.start()
            time.sleep(30)
            break;










# =============== run the script =====#
# if __name__ =='__main__':
#     bot = UsaDate()
#     bot.cnnsol()

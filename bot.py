
""" Class to provide a bot wpp integration"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import os
import time
from time import sleep
from toolbox import config
from datetime import datetime


class Wppbot:

    #* Actual path of files
    dir_path = os.getcwd()
    chromedriver = os.path.join(dir_path, "files/chromedriver.exe")
    profile = os.path.join(dir_path, "profile", "wpp")

    def __init__(self):
        """Contructor of the class"""

        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument(
            r"user-data-dir={}".format(self.profile))
        user_agent = config.get("user_agent")
        headless = config.is_headless()
        if headless:
            self.options.add_argument('--headless')
        self.options.add_argument("--user-agent=" + user_agent)
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("window-size=1400,2100")
        self.driver = webdriver.Chrome(
            self.chromedriver, chrome_options=self.options)

    def send(self, number, msg):
        link = f"https://web.whatsapp.com/send?phone={number}"
        escope = config.get("escope_class")
        msg_box = config.get("msg_box_class")
        send_button = config.get("send_button_class")
        try:
            self.driver.get(link)
            start_time = time.time()
            while(True):
                if (time.time() - start_time) > 30:
                    print ("Exceding time limit!!!!")
                    break
                try:
                    self.escope = self.driver.find_element_by_class_name(escope)
                    break
                except NoSuchElementException:
                    pass
            self.escope.click()
            sleep(1)
            self.msg_box = self.driver.find_elements(By.CLASS_NAME, msg_box)[-1]
            self.msg_box.send_keys(msg)
            sleep(1)
            #self.driver.save_screenshot("srn2.png")
            self.send_button = self.driver.find_elements(By.CLASS_NAME, send_button)[-1]
            self.send_button.click()
            time_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            sleep(2)
            print("[INFO]")
            print(f"|---> Mensagem: {msg}")
            print(f"|---> Destinatario: {number}")
            print(f"|---> Horário: {time_now}")
            print("|---> Status: {}".format("Ok"))
        except:
            #TODO: Write except
            print("ERROR undefined")

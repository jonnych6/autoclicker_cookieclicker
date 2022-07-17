from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_WEB_DRIVER_PATH = "D:\Computer Functions\WebDevelopment/chromedriver.exe"
ser = Service(CHROME_WEB_DRIVER_PATH)
driver = webdriver.Chrome(service=ser)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

######
COOKIE_BUTTON = driver.find_element(By.ID, "cookie")


######


class CookieFunctions():

    def __init__(self):
        self.upgrades_list = []
        self.upgrades_name = []
        self.upgrade_dict = {}
        self.money = 0

    def quit_game(self):
        driver.quit()

    def find_money(self):
        self.money = float(driver.find_element(By.ID, "money").text.replace(",", "")
)


    def click_cookie(self):
        COOKIE_BUTTON.click()

    def get_upgrades(self):
        upgrades = driver.find_elements(By.CSS_SELECTOR, "#store b")
        upgrades.pop()
        for x in upgrades:
            new_value = x.text.replace(" ", "").split("-")[1].replace(",", "")
            self.upgrades_list.append(int(new_value))

        self.upgrades_list = self.upgrades_list[::-1]
        #print(self.upgrades_list)


    def get_upgrades_names(self):
        names = driver.find_elements(By.CLASS_NAME, "grayed")
        names.pop()
        self.upgrades_name = [names.get_attribute("id") for names in names]
        self.upgrades_name = self.upgrades_name[::-1]
        #print(self.upgrades_name)

    def dictionary_it(self):
        self.upgrade_dict = dict(zip(self.upgrades_name, self.upgrades_list))

        # self.upgrade_dict = {self.upgrades_name[i]: self.upgrades_list[i] for i in range(len(self.upgrades_name))}
        #print(self.upgrade_dict)

    def prepare_settings(self):
        self.get_upgrades()
        self.get_upgrades_names()
        self.dictionary_it()



    def check_upgrades(self):
        self.find_money()
        #print(self.upgrade_dict)
        #print(self.upgrade_dict.items())

        for value in self.upgrade_dict.values():
            if self.money >= value:
                key = self.get_key(value)
                upgrade_click = driver.find_element(By.ID, f"{key}")
                upgrade_click.click()
                break



    def get_key(self, val):
        for key, value in self.upgrade_dict.items():
            if val == value:
                return key
        return None


import unittest
import random
from selenium.webdriver.chrome.options import Options
from create_xml import *
from read_xml import *
from home_page import *



TIME_WAITING = 5

class TestBuyMy(unittest.TestCase):

    CONFIG = None

    @classmethod
    def setUpClass(cls):
        if cls.CONFIG.get_text("browser_type") == "chrome":
            opsions = Options()
            opsions.add_argument("--disable-extensions")
            opsions.add_argument("--incognito")
            opsions.add_argument("--disable-popup-blocking")
            cls.driver = webdriver.Chrome(options=opsions)

        elif cls.CONFIG.get_text("browser_type") == "safari":
            cls.driver = webdriver.Safari(executable_path='/usr/bin/safaridriver')

        cls.driver.maximize_window()
        cls.driver.implicitly_wait(TIME_WAITING)
        HomePageBuyMe.init_class()
        cls.driver.get("https://buyme.co.il")
        cls.home_page_factory = HomePageBuyMe(cls.driver)


    def test_registration_passed_successfully(self):
        self.home_page_factory.insert_first_name(self.CONFIG.get_text("first_name"))
        self.home_page_factory.insert_mail(self.CONFIG.get_text("mail"))
        self.home_page_factory.insert_password(self.CONFIG.get_text("password"))
        self.home_page_factory.insert_confirm_password(self.CONFIG.get_text("password_confirm"))
        self.home_page_factory.click_to_final_confirm()
        title = self.driver.title
        self.assertEqual(title, self.CONFIG.get_text("excepted_title"))
        self.assertTrue(self.home_page_factory.exit_my_account_button(self.driver))


NEW_NUM = random.randint(1, 10000)
INPUT = {"browser_type": "chrome", "excepted_title": "BUYME אתר המתנות והחוויות הגדול בישראל |\xa0Gift Card", "first_name": "David",
         'mail': f"David{NEW_NUM}@gmail.com", "password": f"David{NEW_NUM}@gmail.com", "password_confirm": f"David{NEW_NUM}@gmail.com"}

def main():
    config = CreateConfig("buy_me_website")
    for key, value in INPUT.items():
        config.add_child(key, INPUT[key])
    config.write_to_file("/Users/davidrotenberg/Desktop/main/config_buy_me.xml")

    TestBuyMy.CONFIG = ReadConfig("/Users/davidrotenberg/Desktop/main/config_buy_me.xml")
    with open("/Users/davidrotenberg/Desktop/main/tests_result.txt", "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)

if __name__ == '__main__':
    main()
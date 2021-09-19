from selenium import webdriver

class HomePageBuyMe:

    @classmethod
    def init_class(cls):
        cls.xpath_or_css_elements = {"main register button": '//*[@id="ember957"]/div/ul[1]/li[3]/a/span[2]',
                                    "register button": '//*[@id="ember924"]/div/div[1]/div/div/div[3]/div[1]/span',
                                    "first_name": 'input[id="ember1482"]',
                                    "mail": 'input[id="ember1485"]',
                                    "password": 'input[id="valPass"]',
                                    "password_confirm": 'input[id="ember1491"]',
                                    "final_confirm": 'button[id="ember1493"]',
                                     "my_account_button": 'li[id="ember1530"]'}

    def __init__(self, driver):
        driver.find_element_by_xpath(self.xpath_or_css_elements["main register button"]).click()
        driver.find_element_by_xpath(self.xpath_or_css_elements["register button"]).click()
        self.__first_name_box = driver.find_element_by_css_selector(self.xpath_or_css_elements["first_name"])
        self.__mail_box = driver.find_element_by_css_selector(self.xpath_or_css_elements["mail"])
        self.__password_box = driver.find_element_by_css_selector(self.xpath_or_css_elements["password"])
        self.__password_confirm_box = driver.find_element_by_css_selector(self.xpath_or_css_elements["password_confirm"])
        self.__final_confirm_box = driver.find_element_by_css_selector(self.xpath_or_css_elements["final_confirm"])

    def insert_first_name(self, first_name):
        self.__first_name_box.send_keys(first_name)

    def insert_mail(self,mail):
        self.__mail_box.send_keys(mail)

    def insert_password(self,password):
        self.__password_box.send_keys(password)

    def insert_confirm_password(self,confirm_password):
        self.__password_confirm_box.send_keys(confirm_password)

    def click_to_final_confirm(self):
        self.__final_confirm_box.click()

    def exit_my_account_button(self, driver):
        try:
            driver.find_element_by_css_selector(self.xpath_or_css_elements["my_account_button"])
            return True
        except():
            return False
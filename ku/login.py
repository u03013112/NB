# encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
class Login:
    def init(self):
        option = webdriver.FirefoxOptions()
        # option.add_argument("-headless")
        # option.set_preference('permissions.default.image', 2)
        # option.set_preference('permissions.default.stylesheet',2)
        self.driver = webdriver.Remote(
            # command_executor="http://selenium-hub:4444/wd/hub",
            command_executor="http://127.0.0.1:4444/wd/hub",
            options=option,
            desired_capabilities=DesiredCapabilities.FIREFOX
        )
        self.driver.set_page_load_timeout(100)
        self.driver.set_script_timeout(100)
    def exit(self):
        self.driver.quit()
    def closeAll(self):
        handles = driver.window_handles
        # for 
    def login(self):
        driver = self.driver
        try:
            url = "https://ku.ku5168.com/?open=true"
            driver.get(url)
            print(driver.title)
            wait(driver,100).until(EC.presence_of_element_located((By.ID,'loginbutton')))
            driver.find_element_by_id("loginbutton").click()
            driver.get_screenshot_as_file('01.png')
            print('accountId ...')
            wait(driver,100).until(EC.presence_of_element_located((By.ID,'accountId')))
            username = driver.find_element_by_id("accountId")
            username.send_keys("U03013112")
            print('accountPwd ...')
            wait(driver,100).until(EC.presence_of_element_located((By.NAME,'accountPwd')))
            passwd = driver.find_element_by_name("accountPwd")
            passwd.send_keys("123456a131")
            print('signin ...')
            wait(driver,100).until(EC.presence_of_element_located((By.ID,'signin')))
            loginButton = driver.find_element_by_id("signin").click()
            driver.get_screenshot_as_file('02.png')
            wait(driver,100).until(EC.presence_of_element_located((By.ID,'UserMenu')))
            driver.get_screenshot_as_file('03.png')
        except BaseException as msg:
            print("error:",msg)
            self.exit()
    def intoCaiPiao(self):
        driver = self.driver
        handles = driver.window_handles
        print("handles0:",handles)  # 输出句柄集合
        try:
            wait(driver,100).until(EC.visibility_of_element_located((By.LINK_TEXT,'彩票游戏')))
            cp = driver.find_element_by_link_text("彩票游戏")
            ac = ActionChains(driver)
            cp.click()
            ac.move_to_element(cp)
            ac.perform()
            time.sleep(2)
            # driver.get_screenshot_as_file('04.png')

            wait(driver,100).until(EC.visibility_of_element_located((By.ID,'BB_Ball_loto_maintain')))
            driver.find_element_by_id("BB_Ball_loto_maintain").click()
            wait(driver,100).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='fancybox-skin']//input[@class='FT_button_w50L']")))
            wait(driver,100).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='fancybox-skin']//input[@class='FT_button_w50L']")))

            # driver.get_screenshot_as_file('05.png')
            btn = driver.find_element_by_xpath("//div[@class='fancybox-skin']//input[@class='FT_button_w50L']")
            
            btn.click()
            # driver.get_screenshot_as_file('06.png')
            handles = driver.window_handles
            print("handles1:",handles)  # 输出句柄集合
            driver.switch_to.window(handles[-1])
            print(driver.title)
            print(driver.current_window_handle)
            wait(driver,100).until(EC.title_is('全球彩票'))
            listCookies = driver.get_cookies()
            print(listCookies)
            cookie = [item["name"] + "=" + item["value"] for item in listCookies]
            cookiestr = '; '.join(item for item in cookie)
            print(cookiestr)
            return cookiestr
        except BaseException as msg:
            print("error:",msg)
            self.exit()
        return ""
    def getCookies(self):
        l = Login()
        l.init()
        l.login()
        cookiestr = l.intoCaiPiao()
        l.exit()
        return cookiestr


if __name__=='__main__':
    l = Login()
    l.init()
    l.login()
    l.intoCaiPiao()
    l.exit()
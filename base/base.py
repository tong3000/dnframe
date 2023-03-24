from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from common.Log import framelog
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.log = framelog().log()

    # 定位元素
    # def findele(self,*args):
    #     self.log.info("定位元素方式"+args[0])
    #     self.log.info("定位元素属性值" + args[1])
    #     return self.driver.find_element(*args)
    def findele(self, *args):
        try:
            self.log.info("定位元素方式" + args[0])
            self.log.info("定位元素属性值" + args[1])
            # return self.driver.find_element(*args)
            return WebDriverWait(self.driver, 5).until(ex.visibility_of(self.driver.find_element(*args)))
        except:
            self.log.error("找不到元素" + args[1])

    # 等待元素可见(tupleEle:例如(By.NAME,"username"))
    # def waitelevisible(self, bytype, element):
    #     WebDriverWait(self.driver, 5).until(ex.visibility_of_element_located((bytype, element)))

    def wait_url_is(self, url):
        WebDriverWait(self.driver, 5).until(ex.url_to_be(url))

    # click方法
    def click(self, *args):
        self.findele(*args).click()

    # 输入值
    def sendkey(self, *args, value):
        self.findele(*args).send_keys(value)

    # #id定位元素
    # def by_id(self,ele):
    #     return self.driver.find_element(By.ID,ele)
    # #name定位元素
    # def by_name(self,ele):
    #     return self.driver.find_element(By.NAME, ele)
    # #xpath定位元素
    # def by_xpath(self,ele):
    #     return self.driver.find_element(By.XPATH, ele)
    # #css定位元素
    # def by_css(self,ele):
    #     return self.driver.find_element(By.CSS_SELECTOR, ele)
    # #linktext
    # def by_linktext(self,ele):
    #     return self.driver.find_element(By.LINK_TEXT, ele)
    # #partiallinktext
    # def by_partialtext(self,ele):
    #     return self.driver.find_element(By.PARTIAL_LINK_TEXT, ele)
    # #tagname
    # def by_tagname(self,ele):
    #     return self.driver.find_element(By.TAG_NAME, ele)
    # #classname
    # def by_classname(self,ele):
    #     return self.driver.find_element(By.CLASS_NAME, ele)

    # 获取url
    def url(self):
        return self.driver.current_url

    # 切换FRAME
    def switchframe(self, name):
        return self.driver.switch_to.frame(name)

    # 返回默认frame
    def defaultcontent(self):
        return self.driver.switch_to.default_content()

    # 窗口最大化
    def maxwin(self):
        self.driver.maximize_window()

    # 全屏
    def fulwin(self):
        self.driver.fullscreen_window()

    # 最小化
    def minwin(self):
        self.driver.minimize_window()

    # 切换窗口:针对两个窗口进行切换
    def newtab(self):
        h = self.driver.window_handles
        self.driver.switch_to.window(h[-1])

    # 获取文本
    def gettext(self, *args):
        return self.findele(*args).text

    # 下拉框
    def select(self, *args, value):
        se = self.findele(*args)
        Select(se).select_by_value(value)

    # alert
    def alert(self):
        self.driver.switch_to.alert.accept()

    # 获取属性
    def getattr(self, *args, attr):
        return self.findele(*args).get_attribute(attr)

    # 鼠标右键
    def contextclick(self, *args):
        ActionChains(self.driver).context_click(self.findele(*args)).perform()

    # 鼠标左键
    def clickhold(self, *args):
        ActionChains(self.driver).click_and_hold(self.findele(*args)).perform()

    # 双击
    def doubleclick(self, *args):
        ActionChains(self.driver).double_click(self.findele(*args)).perform()

    # 悬停
    def moveto(self, *args):
        ActionChains(self.driver).move_to_element(self.findele(*args)).perform()

    # 拖拽操作
    def drag(self, *args, x, y):
        ActionChains(self.driver).drag_and_drop_by_offset(self.findele(*args), x, y).perform()

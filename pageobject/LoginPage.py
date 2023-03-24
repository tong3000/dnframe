from selenium.webdriver.common.by import By

from base.base import Base
from common.util import projjectpath
from common.fateadm_api import TestFunc


# 继承
class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.ele_username = (By.NAME, "username")
        self.ele_password = (By.NAME, "password")
        self.ele_verifycode = (By.NAME, "validateCode")
        self.ele_loginbtn = (By.ID, "btnSubmit")
        self.ele_codeimg = (By.CLASS_NAME, "imgcode")
        # 携程注册申请-验证滑动条
        self.ele_sour = (By.CSS_SELECTOR, "#slideCode > div.cpt-drop-box > div.cpt-drop-btn")
        self.ele_slide = (By.CSS_SELECTOR, "#slideCode")

    # 用户名
    def user_name(self):
        return self.findele(self.ele_username[0], self.ele_username[1])

    # def waitvisible_username(self):
    #     self.waitelevisible(self.ele_username[0], self.ele_username[1])

    # 密码
    def passwd(self):
        return self.findele(self.ele_password[0], self.ele_password[1])

    # def waitvisible_passwd(self):
    #     self.waitelevisible(self.ele_password[0], self.ele_password[1])

    # 验证码
    def verifycode(self):
        return self.findele(self.ele_verifycode[0], self.ele_verifycode[1])

    # def waitvisible_verifycode(self):
    #     self.waitelevisible(self.ele_verifycode[0], self.ele_verifycode[1])

    # 验证码图片
    def codeimg(self):
        return self.findele(self.ele_codeimg[0], self.ele_codeimg[1])

    # def waitvisible_codeimg(self):
    #     self.waitelevisible(self.ele_codeimg[0], self.ele_codeimg[1])

    # 登录按钮
    def loginbtn(self):
        return self.findele(self.ele_loginbtn[0], self.ele_loginbtn[1])

    # def waitvisible_loginbtn(self):
    #     self.waitelevisible(self.ele_loginbtn[0], self.ele_loginbtn[1])

    # 将进度条拉满到100%
    def dragele(self):
        slide = self.findele(self.ele_slide[0], self.ele_slide[1])
        self.drag(self.ele_sour[0], self.ele_sour[1], x=slide.size['width'], y=slide.size['height'])

    # 登录功能
    def login(self, name, passwd):
        self.log.info("开始测试登录功能")
        self.maxwin()
        self.log.info("用户名")
        # self.waitvisible_username()
        self.user_name().clear()
        self.user_name().send_keys(name)
        self.log.info("密码")
        # self.waitvisible_passwd()
        self.passwd().clear()
        self.passwd().send_keys(passwd)
        # self.log.info("验证码截图")
        # self.waitvisible_codeimg()
        # path = projjectpath()+"pic\\"+"pic.png"
        # self.codeimg().screenshot(path)
        # self.log.info("验证码识别与验证码填写")
        # self.verifycode().send_keys(TestFunc(path))
        self.log.info("登录按钮")
        # self.waitvisible_loginbtn()
        self.loginbtn().click()
        self.log.info("进入首页")
        self.wait_url_is("http://localhost/index")

        return self.url()

# 角色管理
from selenium.webdriver.common.by import By

from base.base import Base


class SysPage(Base):
    # 系统管理
    def sysmanage(self):
        return self.findele(By.CSS_SELECTOR, "#side-menu > li:nth-child(3) > a > span.nav-label")

    # def waitvisible_sysmanage(self):
    #     self.waitelevisible(By.CSS_SELECTOR, "#side-menu > li:nth-child(3) > a > span.nav-label")

    # 角色管理
    def rolemanage(self):
        return self.findele(By.CSS_SELECTOR, "#side-menu > li.active > ul > li:nth-child(2) > a")

    # def waitvisible_rolemanage(self):
    #     self.waitelevisible(By.CSS_SELECTOR, "#side-menu > li.active > ul > li:nth-child(2) > a")

    # 进入角色管理页面
    def role(self):
        # self.waitvisible_sysmanage()
        self.sysmanage().click()
        # self.waitvisible_rolemanage()
        self.rolemanage().click()

# 新增角色
from base.base import Base
from selenium.webdriver.common.by import By


class NewRole(Base):
    # 新增角色
    def newrolebtn(self):
        return self.findele(By.CSS_SELECTOR, "#toolbar > a.btn.btn-success > i")

    # def waitvisible_newrolebtn(self):
    #     self.waitelevisible(By.CSS_SELECTOR, "#toolbar > a.btn.btn-success > i")

    # rolename
    def newrolename(self):
        return self.findele(By.NAME, "roleName")

    # def waitvisible_newrolename(self):
    #     self.waitelevisible(By.NAME, "roleName")

    # rolekey
    def newrolekey(self):
        return self.findele(By.NAME, "roleKey")

    # def waitvisible_newrolekey(self):
    #     self.waitelevisible(By.NAME, "roleKey")

    # rolesort
    def newrolesort(self):
        return self.findele(By.NAME, "roleSort")

    # def waitvisible_newrolesort(self):
    #     self.waitelevisible(By.NAME, "roleSort")

    # 确定
    def newroleok(self):
        return self.findele(By.CSS_SELECTOR,
                            "#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0")

    # def waitvisible_newroleok(self):
    #     self.waitelevisible(By.CSS_SELECTOR,
    #                         "#layui-layer1 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0")

    # 新增role功能
    def addrole(self, rolename, rolekey, rolesort):
        self.log.info("角色新增")
        self.log.info("点击新增")
        self.switchframe("iframe3")
        # self.waitvisible_newrolebtn()
        self.newrolebtn().click()
        self.defaultcontent()
        self.log.info("添加角色弹窗-输入角色名称")
        self.switchframe("layui-layer-iframe1")
        # self.waitvisible_newrolename()
        self.newrolename().send_keys(rolename)
        self.log.info("添加角色弹窗-输入权限字符")
        # self.waitvisible_newrolekey()
        self.newrolekey().send_keys(rolekey)
        self.log.info("添加角色弹窗-输入角色顺序")
        # self.waitvisible_newrolesort()
        self.newrolesort().send_keys(rolesort)
        self.defaultcontent()
        self.log.info("添加角色弹窗-点击确定")
        # self.waitvisible_newroleok()
        self.newroleok().click()

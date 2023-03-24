from base.unitbase import unitbase
from pageobject.LoginPage import LoginPage
from pageobject.RolePage import NewRole
from pageobject.SysPage import SysPage
from common.ExcelUtil import ExcelUtil
from common.util import projjectpath
import time

path = projjectpath() + "data\\" + "testdata.xlsx"
ex = ExcelUtil(path, "role")
dic = ex.ExcelDic()


class loginunit(unitbase):
    def test01(self):
        l = LoginPage(self.driver)
        url = l.login(dic[1][0], dic[1][1])
        time.sleep(3)
        self.assertIn("index", url)

    def test02(self):
        s = SysPage(self.driver)
        s.role()

    def test03(self):
        n = NewRole(self.driver)
        n.addrole(dic[1][2], dic[1][3], int(dic[1][4]))

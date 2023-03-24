import unittest, HTMLTestRunner
from time import sleep

from common.ExcelUtil import ExcelUtil
from pageobject.LoginPage import LoginPage
from common.util import projjectpath, get_driver, get_curry_dir, configAdress
from pageobject.RolePage import NewRole
from pageobject.SysPage import SysPage

path = projjectpath() + "data\\" + "testdata.xlsx"
ex = ExcelUtil(path, 'role')
dic = ex.ExcelDic()


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        # cls.driver.get("http://localhost/")
        cls.driver.get(configAdress("testUrl", "url"))

    def test01(self):
        l = LoginPage(self.driver)
        url = l.login(dic[1][0], dic[1][1])
        self.assertIn("index", url)

    def test02(self):
        s = SysPage(self.driver)
        s.role()

    def test03(self):
        n = NewRole(self.driver)
        n.addrole(dic[1][2], dic[1][3], int(dic[1][4]))

    def test04(self):
        self.driver.get("https://passport.ctrip.com/user/reg/home")
        sleep(5)
        l = LoginPage(self.driver)
        l.dragele()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("test over")


if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover(get_curry_dir(), 'logintest.py', top_level_dir=None)
    file_name = projjectpath() + "reports\\" + "dntest.html"
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="dntest_report", description="web test")
    runner.run(discover)

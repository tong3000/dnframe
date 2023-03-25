from os.path import dirname
import sys, pytest

# 加入环境变量
path = dirname(__file__)
sys.path.insert(0,path.split("testcases")[0])

import unittest, os, HTMLTestRunner
from common.util import projjectpath

path = os.getcwd()
print(path)


def allcase():
    discover = unittest.defaultTestLoader.discover(path, 'logintest.py', top_level_dir=None)
    return discover

if __name__ == '__main__':
    print(sys.path)
    # file_name =  projjectpath()+"reports\\"+"dntest.html"
    # fp = open(file_name, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="dntest_report", description="web test")
    # runner.run(allcase())

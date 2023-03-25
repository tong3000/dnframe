from os.path import dirname, abspath, split
import sys

path = abspath(dirname(__file__))
rootPath = split(path)[0]
sys.path.insert(0, rootPath)


import unittest, os, HTMLTestRunner
from common.util import projjectpath

# path = os.getcwd()
# print(path)


def allcase():
    discover = unittest.defaultTestLoader.discover(path, 'logintest.py', top_level_dir=None)
    return discover


if __name__ == '__main__':
    file_name = projjectpath() + "reports\\" + "dntest.html"
    fp = open(file_name, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="dntest_report", description="web test")
    runner.run(allcase())

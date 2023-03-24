import configparser
import os
import xlrd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# excel读取返回字典
def ReadExcelDic(path, sheetname):
    xls = xlrd.open_workbook(path)
    sheet = xls.sheet_by_name(sheetname)
    dic = {}
    # {"0":"["admin","admin123"]"}
    for r in range(sheet.nrows):
        list = []
        for c in range(sheet.ncols):
            list.append(sheet.row_values(r)[c])
        dic[r] = list
    return dic


# excel读取返回列表【{“”：”“}，{“”：“”}】
def ExcelList(path, sheetname):
    xls = xlrd.open_workbook(path)
    sheet = xls.sheet_by_name(sheetname)
    list = []
    # {"0":"["admin","admin123"]"}
    for r in range(sheet.nrows):
        dic = {}
        if r > 0:
            dic["username"] = sheet.row_values(r)[0]
            dic["password"] = sheet.row_values(r)[1]
            list.append(dic)
    return list


# 获取项目路径
def projjectpath():
    return os.path.split(os.path.abspath(__file__))[0].split('c')[0]
    # os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 获取当前工作目录
def get_curry_dir():
    return os.getcwd()


# 获取谷歌驱动所在路径
def get_driver_directory():
    return projjectpath() + "\\driver\\chromedriver.exe"


# 获取webdriver实例对象
def get_driver():
    path = Service(get_driver_directory())
    return webdriver.Chrome(service=path)


# 获取配置文件内容
def configAdress(key, value):
    config = configparser.ConfigParser()
    config.read(projjectpath() + "config.ini")
    return config.get(key, value)


if __name__ == "__main__":
    # dic = ReadExcelDic(r"D:\Environment\dntest\py\lesson05\testdata.xlsx", "role")
    # 转换成int类型
    # print(dic[1][1])
    # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print(projjectpath())
    print(configAdress("testUrl", "url"))
    print(configAdress("driver", "driverpath"))

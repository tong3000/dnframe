import xlrd

from common.util import projjectpath


class ExcelUtil:
    def __init__(self, excelpath=None, sheet=None):
        self.excelpath = excelpath
        if sheet == None:
            sheet = "Sheet1"
        self.workbook = xlrd.open_workbook(self.excelpath)
        self.sheet = self.workbook.sheet_by_name(sheet)

    # 行数
    def getrows(self):
        rows = self.sheet.nrows
        if rows >= 1:
            return rows
        return None

    # 列数
    def getcols(self):
        cols = self.sheet.ncols
        if cols >= 1:
            return cols
        return None

    # 获取单元格数据
    def getcell(self, row, col):
        if self.getrows() > row:
            data = self.sheet.cell(row, col).value
            return data
        return None

    # 一次性读取全部值存放字典中
    def ExcelDic(self):
        dic = {}
        for r in range(self.getrows()):
            list = []
            for c in range(self.getcols()):
                list.append(self.sheet.row_values(r)[c])
            dic[r] = list
        return dic


if __name__ == "__main__":
    path = projjectpath() + "data\\" + "testdata.xlsx"
    # ex = ExcelUtil(r"D:\Environment\dntest\py\lesson05\testdata.xlsx", "role")
    ex = ExcelUtil(path, 'role')
    # print(ex.getcols())
    # print(ex.getrows())
    # print(ex.getcell(2,0))
    dic = ex.ExcelDic()
    print(dic[0])
    print(dic[1][1])

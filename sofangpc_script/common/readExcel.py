import xlrd

class ReadExcel():
    def __init__(self,excelPath,sheetName = "Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        self.keys = self.table.row_values(0)
        # print(self.keys)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j=1
            for i in range(1,self.rowNum):
                s = {}
                values = self.table.row_values(j)
                for x in range(self.colNum):
                  s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r
if __name__ == "__main__":
    filepath = "D:\\data.xlsx"
    data = ReadExcel(filepath)
    print(data.dict_data())
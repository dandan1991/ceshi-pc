import os
import unittest
from common import HTMLTestRunner_cn
from BeautifulReport import BeautifulReport
from tomorrow import threads

path1 = os.path.dirname(os.path.realpath(__file__))
case_path = os.path.join(path1,"script")
# reportpath = os.path.join(path1, "report")
def addcase():
    pattent = "test*.py"
    discover = unittest.defaultTestLoader.discover(start_dir=case_path,pattern=pattent)
    return discover

@threads(2)
def runcase(discover):
    result = BeautifulReport(discover)
    result.report(filename='report.html', description='测试deafult报告',log_path='report')

if __name__ == "__main__":
    discover = addcase()
    for i in discover:
        runcase(i)
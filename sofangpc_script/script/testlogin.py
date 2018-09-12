import unittest
import ddt
from selenium import webdriver
from Pages.loginpage import Login,login_url
from common.readExcel import ReadExcel
import mysql.connector

# datalist = [
#                 {"username": "15910304557", "pwd": "123456", "type": "1", "tishi": "您好，15910304557"},
#                 {"username": "15910304557", "pwd": "123458", "type": "2", "tishi": "密码输入错误"},
#                 {"username": "15910304550", "pwd": "123458", "type": "2", "tishi": "您输入的账号不存在"},
#            ]
#

# filepath = "D:\\data.xlsx"
# data = ReadExcel(filepath)
# datalist = data.dict_data()


datalist = [
                ("15910304557","123456","1", "您好，15910304557"),
                ("15910304557","123458","2","密码输入错误"),
                ("15910304550","123458","2","您输入的账号不存在")
           ]



@ddt.ddt
class LoginP(unittest.TestCase):
    '''测试登录'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.loginpa = Login(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.driver.delete_all_cookies() # 退出登录
        self.driver.refresh()


    @ddt.data(*datalist)
    def test_01(self,data):
        '''登录成功'''
        self.loginpa.logins(data[0],data[1],data[2],data[3])

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
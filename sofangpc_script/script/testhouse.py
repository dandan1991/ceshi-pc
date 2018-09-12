import unittest

from Pages.loginpage import Login,login_url
from Pages.luruhousepage import *


class house(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        logincls = Login(cls.driver)
        cls.driver.get(login_url)
        logincls.denglu('15910304557', '123456')
        time.sleep(2)
        cls.luruhouse = Luru(cls.driver)
        cls.luruhouse.check_firstlevel("二手房")
        cls.luruhouse.check_secondlevel("录入房源")

    def test_01(self):
        '''测试区域为必填项'''
        self.luruhouse.inpu_housingInspectionNum("")
        tishi = self.luruhouse.must_inpu_tishi(1)
        self.assertTrue(tishi == "请填写省份和城市")

    def test_02(self):
        '''验证地址为必填项'''
        self.luruhouse.inpu_address(" ")
        # self.luruhouse.inpu_area(" ")
        tishi = self.luruhouse.must_inpu_tishi(4)
        self.assertTrue(tishi == "请填写内容")

    def test_021(self):
        '''测试地址必须为有效的'''
        self.luruhouse.inpu_address("1234555")
        self.luruhouse.inpu_area("")
        tishi = self.luruhouse.must_inpu_tishi(4)
        self.assertTrue(tishi == "您填写的地址获取不准确，请点击地图获取详细地址")

    def test_03(self):
        '''验证面积为必填项'''
        self.luruhouse.inpu_area(" ")
        self.luruhouse.inpu_price2(" ")
        tishi = self.luruhouse.must_inpu_tishi(5)
        self.assertTrue(tishi == "请填写内容")

    def test_031(self):
        '''验证面积必须为正整数'''
        self.luruhouse.inpu_area("0")
        self.luruhouse.inpu_price2("")
        tishi = self.luruhouse.must_inpu_tishi(5)
        self.assertTrue(tishi == "请填写正数并不超过5位,最多保留2位小数")

    def test_032(self):
        '''验证面积必须为小于6位正整数'''
        self.luruhouse.inpu_area("123456")
        self.luruhouse.inpu_price2("")
        tishi = self.luruhouse.must_inpu_tishi(5)
        self.assertTrue(tishi == "请填写正数并不超过5位,最多保留2位小数")

    def test_033(self):
        '''验证面积只能保留两位小数'''
        self.luruhouse.inpu_area("12345.991")
        self.luruhouse.inpu_price2("")
        tishi = self.luruhouse.must_inpu_tishi(5)
        self.assertTrue(tishi == "请填写正数并不超过5位,最多保留2位小数")

    # def test_04(self):
    #     '''验证价格不能为空'''
    #     self.luruhouse.inpu_price2(" ")
    #     self.luruhouse.inpu_area("")
    #     tishi = self.luruhouse.must_inpu_tishi(6)
    #     self.assertTrue(tishi == "请填写内容")
    #
    # def test_041(self):
    #     '''验证价格不能为0'''
    #     self.luruhouse.inpu_price2("0")
    #     self.luruhouse.inpu_area("")
    #     tishi = self.luruhouse.must_inpu_tishi(6)
    #     self.assertTrue(tishi == "请填写正整数,并不超过6位数")
    #
    # def test_042(self):
    #     '''验证价格不能为负数'''
    #     self.luruhouse.inpu_price2("-3")
    #     self.luruhouse.inpu_area("")
    #     tishi = self.luruhouse.must_inpu_tishi(6)
    #     self.assertTrue(tishi == "请填写正整数,并不超过6位数")
    #
    # def test_043(self):
    #     '''验证价格只能保留两位小数'''
    #     self.luruhouse.inpu_price2("11.323")
    #     self.luruhouse.inpu_area("")
    #     tishi = self.luruhouse.must_inpu_tishi(6)
    #     self.assertTrue(tishi == "请填写正整数,并不超过6位数")
    #
    # def test_044(self):
    #     '''验证价格最多为6为正整数'''
    #     self.luruhouse.inpu_price2("1234564")
    #     self.luruhouse.inpu_area("")
    #     tishi = self.luruhouse.must_inpu_tishi(6)
    #     self.assertTrue(tishi == "请填写正整数,并不超过6位数")
    #
    # def test_05(self):
    #     '''验证居为必填项'''
    #     self.luruhouse.inpu_houseRoom("")
    #     self.luruhouse.inpu_hall("")
    #     tishi = self.luruhouse.must_inpu_tishi(7)
    #     self.assertTrue(tishi == "请填写内容")
    #
    # def test_051(self):
    #     '''验证居不能为0'''
    #     self.luruhouse.inpu_houseRoom("0")
    #     self.luruhouse.inpu_hall("")
    #     tishi = self.luruhouse.must_inpu_tishi(7)
    #     self.assertTrue(tishi == "请填写不为0的个位数")
    #
    # def test_052(self):
    #     '''验证居只能是一位数'''
    #     self.luruhouse.inpu_houseRoom("12")
    #     self.luruhouse.inpu_hall("")
    #     tishi = self.luruhouse.must_inpu_tishi(7)
    #     self.assertTrue(tishi == "请填写不为0的个位数")
    #
    # def test_06(self):
    #     '''验证厅为必填项'''
    #     self.luruhouse.inpu_hall("")
    #     self.luruhouse.inpu_toilet("")
    #     tishi = self.luruhouse.must_inpu_tishi(7)
    #     self.assertTrue(tishi == "请填写内容")
    #
    # def test_061(self):
    #     '''验证厅不能为0'''
    #     self.luruhouse.inpu_hall("0")
    #     self.luruhouse.inpu_toilet("")
    #     tishi = self.luruhouse.must_inpu_tishi(7)
    #     self.assertTrue(tishi == "请填写不为0的个位数")
    #
    # def test_062(self):
    #     '''验证厅只能是一位数'''
    #     self.luruhouse.inpu_hall("12")
    #     self.luruhouse.inpu_toilet("")
    #     tishi = self.luruhouse.must_inpu_tishi(7)
    #     self.assertTrue(tishi == "请填写不为0的个位数")
    #
    # def test_07(self):
    #     '''验证卫为必填项'''
    #     self.luruhouse.inpu_toilet("")
    #     self.luruhouse.inpu_kitchen("")
    #     tishi = self.luruhouse.must_inpu_tishi(7)
    #     self.assertTrue(tishi == "请填写内容")
    #
    # def test_071(self):
    #     '''验证卫不能为0'''
    #     self.luruhouse.inpu_toilet("0")
    #     self.luruhouse.inpu_kitchen("")
    #     tishi = self.luruhouse.must_inpu_tishi(7)
    #     self.assertTrue(tishi == "请填写不为0的个位数")
    #
    # def test_072(self):
    #     '''验证卫只能是一位数'''
    #     self.luruhouse.inpu_toilet("12")
    #     self.luruhouse.inpu_kitchen("")
    #     tishi = self.luruhouse.must_inpu_tishi(7)
    #     self.assertTrue(tishi == "请填写不为0的个位数")
    #
    # def test_08(self):
    #     '''验证卫为必填项'''
    #     self.luruhouse.inpu_kitchen("")
    #     self.luruhouse.inpu_protype("")
    #     tishi = self.luruhouse.must_inpu_tishi(7)
    #     self.assertTrue(tishi == "请填写内容")
    #
    # def test_081(self):
    #     '''验证卫不能为0'''
    #     self.luruhouse.inpu_kitchen("0")
    #     self.luruhouse.inpu_protype("")
    #     tishi = self.luruhouse.must_inpu_tishi(7)
    #     self.assertTrue(tishi == "请填写不为0的个位数")
    #
    # def test_082(self):
    #     '''验证卫只能是一位数'''
    #     self.luruhouse.inpu_kitchen("12")
    #     self.luruhouse.inpu_protype("")
    #     tishi = self.luruhouse.must_inpu_tishi(7)
    #     self.assertTrue(tishi == "请填写不为0的个位数")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()


import random
from Pages.loginpage import *


class Luru(Base):

    def check_firstlevel(self,name):
        '''点击一级菜单'''
        loc1 = ("link text","%s"%name)
        self.clickEle(loc1)

    def check_secondlevel(self,name):
        '''点击二级菜单'''
        loc1 = ("link text","%s"%name)
        self.clickEle(loc1)

    def inpu_quyu(self,shengvalue):
        '''输入省'''
        loc1 = ("link text","选择省")
        self.clickEle(loc1)
        loc2 = ("xpath","//div[@id='proId']/div/ul/li[%s]"%shengvalue)
        self.clickEle(loc2)

    def inpu_city(self,cityvalue):
        '''选择城市'''
        time.sleep(1)
        loc1 = ("link text","选择市")
        self.clickEle(loc1)
        loc2 = ("xpath","//div[@id='cityId']/div/ul/li[%s]"%cityvalue)
        self.clickEle(loc2)

    def inpu_cityarea(self,cityareavalue):
        '''选择区'''
        time.sleep(1)
        loc1 = ("link text","选择区")
        self.clickEle(loc1)
        time.sleep(1)
        loc2 = ("xpath","//div[@id='cityareaId']/div/ul/li[%s]"%cityareavalue)
        self.clickEle(loc2)

    def inpu_businessArea(self,businessAreavalue):
        '''选择商圈'''
        time.sleep(1)
        loc1 = ("link text","选择商圈")
        self.clickEle(loc1)
        loc2 = ("xpath","//div[@id='businessAreaId']/div/ul/li[%s]"%businessAreavalue)
        self.clickEle(loc2)

    def inpu_housingInspectionNum(self,housingInspectionNum):
        '''输入检验编号'''
        time.sleep(1)
        loc1 = ("xpath",".//*[@id='oldsale']/div[1]/ul/li[2]/input")
        self.sendKey(loc1,housingInspectionNum)

    def inpu_address(self,address):
        '''输入地址'''
        loc1 = ("id","address")
        if address!=" ":
            self.sendKey(loc1,address)
        else:
            self.clickEle(loc1)

    def inpu_area(self,area):
        '''输入建筑面积'''
        loc1 = ("name","area")
        if area!=" ":
            self.sendKey(loc1,area)
        else:
            self.clickEle(loc1)

    def inpu_price2(self,price2):
        '''输入售价'''
        loc1 = ("name","price2")
        if price2 != " ":
            self.sendKey(loc1,price2)
        else:
            self.clickEle(loc1)

    def inpu_houseRoom(self,houseRoom):
        '''输入室'''
        loc1 = ("id","houseRoom")
        if houseRoom != " ":
            self.sendKey(loc1,houseRoom)
        else:
            self.clickEle(loc1)

    def inpu_hall(self,hall):
        '''输入厅'''
        loc1 = ("id","hall")
        if hall != " ":
            self.sendKey(loc1,hall)
        else:
            self.clickEle(loc1)

    def inpu_toilet(self,toilet):
        '''输入卫'''
        loc1 = ("id","toilet")
        if toilet != " ":
            self.sendKey(loc1,toilet)
        else:
            self.clickEle(loc1)

    def inpu_kitchen(self,kitchen):
        '''输入厨'''
        loc1 = ("id","kitchen")
        if kitchen != " ":
            self.sendKey(loc1,kitchen)
        else:
            self.clickEle(loc1)

    def inpu_protype(self,protype):
        '''输入物业类型
        protype：1:普宅 2:经济适用房  3:商住楼  4:别墅  5:豪宅  6:平房 7:四合院
        '''
        loc1 = ("link text","物业类型")
        self.clickEle(loc1)
        if protype != " ":
            loc2 = ("xpath",".//*[@id='oldsale']/div[1]/ul/li[8]/div[1]/div[1]/ul/li[%s]"%protype)
            self.clickEle(loc2)

    def inpu_dec_con(self,deccon):
        '''输入装修状况
        deccon： 1：毛坯  2：简装  3：中装修  4：精装修  5：豪华装修
        '''
        loc1 = ("link text","装修状况")
        self.clickEle(loc1)
        loc2 = ("xpath",".//*[@id='oldsale']/div[1]/ul/li[8]/div[2]/div[1]/ul/li[%s]"%deccon)
        self.clickEle(loc2)

    def inpu_orientain(self,orientain):
        '''输入朝向
        orientain：1：东  2：南  3：西  4：北  5:南北  6:东南  7:西南  8:东北  9:西北  10:东西
        '''
        loc1 = ("link text","朝向")
        self.clickEle(loc1)
        loc2 = ("xpath",".//*[@id='oldsale']/div[1]/ul/li[8]/div[3]/div[1]/ul/li[%s]"%orientain)
        self.clickEle(loc2)

    def inpu_currentFloor(self,currentFloor):
        '''输入第几层'''
        loc1 = ("name","currentFloor")
        self.sendKey(loc1,currentFloor)

    def inpu_totalFloor(self,totalFloor):
        '''输入总楼层'''
        loc1 = ("name","totalFloor")
        self.sendKey(loc1,totalFloor)
        self.clickEle(loc1)

    def inpu_firstPay(self,firstPay):
        '''输入首付'''
        loc1 = ("name","firstPay")
        self.sendKey(loc1,firstPay)

    def inpu_Property(self,Property):
        '''选择个人产权
        Property： 1：个人产权  2：使用权  3：经济适用房  4:单位产权  5:央产房  6:军产房  7:其它  8:限价房
        '''
        loc1 = ("xpath",".//*[@id='oldsale']/div[2]/ul/li[2]/div/a")
        self.clickEle(loc1)
        loc2 = ("xpath",".//*[@id='oldsale']/div[2]/ul/li[2]/div/div/ul/li[%s]"%Property)
        self.clickEle(loc2)

    def inpu_buildYear(self,buildYear):
        '''输入建筑年代'''
        loc1 = ("name","buildYear")
        self.sendKey(loc1,buildYear)

    def inpu_radio(self,n):
        '''选择配套设施'''
        loc1 = ("class name","radio")
        a = self.findElements(loc1)
        while n > 0:
            i = random.randint(1,10)
            a[i].click()
            n = n-1

    def inpu_biaoqian(self,m):
        '''选择标签
        n:  选择标签的数量
        num:选择标签的数量
        '''
        while m > 0:
            n = random.randint(1,6)
            if n == 1:
                xiaoqubiao = self.findElement(("xpath","//*[@id='con_a_1']/li"))
                j = random.randint(0,14)
                if(xiaoqubiao[j].get_attribute("class")=="color8d"):
                    continue
                else:
                    xiaoqubiao[j].click()
                    m = m-1
            elif n == 2:
                self.clickEle(("id","a2"))
                huxingbiao = self.findElement(("xpath","//*[@id='con_a_2']/li"))
                i = random.randint(0,18)
                if(huxingbiao[i].get_attribute("class")=="color8d"):
                    continue
                else:
                    huxingbiao[i].click()
                    m = m-1
            elif n == 3:
                self.clickEle(("id","a3"))
                jiegoubiao = self.findElement(("xpath","//*[@id='con_a_3']/li"))
                k = random.randint(0,15)
                if(jiegoubiao[k].get_attribute("class")=="color8d"):
                    continue
                else:
                    jiegoubiao[k].click()
                    m = m-1
            elif n == 4:
                self.clickEle(("id","a4"))
                weizhibiao = self.findElement(("xpath","//*[@id='con_a_4']/li"))
                s = random.randint(0,9)
                if(weizhibiao[s].get_attribute("class")=="color8d"):
                    continue
                else:
                    weizhibiao[s].click()
                    m = m-1
            elif n == 5:
                self.clickEle(("id","a5"))
                zhuxiubiao = self.findElement(("xpath","//*[@id='con_a_5']/li"))
                d = random.randint(0,4)
                if(zhuxiubiao[d].get_attribute("class")=="color8d"):
                    continue
                else:
                    zhuxiubiao[d].click()
                    m = m-1
            elif n == 6:
                self.clickEle(("id","a6"))
                qitabiao = self.findElement(("xpath","//*[@id='con_a_6']/li"))
                f = random.randint(0,16)
                if(qitabiao[f].get_attribute("class")=="color8d"):
                    continue
                else:
                    qitabiao[f].click()
                    m = m-1

    def inpu_titlename(self,titlename):
        '''输入房源标题'''
        loc1 = ("xpath",".//*[@id='oldsale']/div[4]/ul/li[1]/input")
        self.sendKey(loc1,titlename)

    def inpu_uppic(self):
        '''上传图片'''
        loc1 = ("xpath","//*[@id='indoor']/div[2]/input")
        self.sendKey(loc1, r"D:\2.jpg")


    def inpu_biaotipic(self):
        '''选择标题图'''
        loc1 = ("xpath",".//*[@id='setTitle_WU_FILE_0']")
        self.clickEle(loc1)

    def inpu_linkman(self,linkman):
        '''输入联系人'''
        loc1 = ("name","linkman")
        self.sendKey(linkman)

    def inpu_linkmobile(self,linkmobile):
        '''输入联系电话'''
        loc1 = ("name","linkmobile")
        self.sendKey(loc1,linkmobile)

    def inpu_submit(self):
        '''保存到待发布'''
        time.sleep(2)
        loc1 = ("xpath",".//*[@id='oldsale']/p/input")
        self.clickEle(loc1)

    def must_inpu_tishi(self,ci):
        try:
            tishi = self.findElement(("xpath",".//*[@id='oldsale']/div[1]/ul/li[%s]/span/em"%ci)).text
            return tishi
        except:
            tishi = ""
            return tishi

if __name__ == "__main__":
        driver = webdriver.Firefox()
        driver.get("http://my.soufang.85cc/majorLogin?type=2")
        logins(driver,'15910304557','123456')
        luru = Luru(driver)
        luru.check_firstlevel("二手房")
        luru.check_secondlevel("录入房源")
        luru.inpu_quyu(1)
        luru.inpu_city(1)
        luru.inpu_cityarea(1)
        luru.inpu_businessArea(1)
        luru.inpu_address("东三环北路甲2号")
        luru.inpu_area(100)
        luru.inpu_price2(200)
        luru.inpu_houseRoom(3)
        luru.inpu_hall(2)
        luru.inpu_toilet(1)
        luru.inpu_kitchen(1)
        luru.inpu_protype(1)
        luru.inpu_dec_con(2)
        luru.inpu_orientain(2)
        luru.inpu_currentFloor(2)
        luru.inpu_totalFloor(10)
        times = time.time()
        luru.inpu_titlename("发布房源住宅房子，低价出售%s"%times)
        luru.inpu_uppic()
        luru.inpu_biaotipic()
        luru.inpu_submit()
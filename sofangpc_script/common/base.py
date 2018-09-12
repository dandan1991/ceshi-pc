from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image


class Base():

    def __init__(self,driver):
        self.driver = driver
        self.timeout = 50
        self.jiangetime = 0.5

    def findElement(self,locator):
        ele = WebDriverWait(self.driver,self.timeout,self.jiangetime).until(lambda x: x.find_element(*locator))
        return  ele

    def findElements(self,locator):
        eles = WebDriverWait(self.driver,self.timeout,self.jiangetime).until(lambda x: x.find_elements(*locator))
        return eles

    def clickEle(self,locator):
        ele = self.findElement(locator)
        ele.click()

    def sendKey(self,locator,keys):
        ele = self.findElement(locator)
        ele.send_keys(keys)

    def is_element_be(self,locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def is_elements_be(self,locator):
        eles = self.findElements(locator)
        ln = len(eles)
        if ln == 0:
            return False
        elif ln == 1:
            return True
        else:
            return True

    def screenEle(self,locator):
        '''截取某个元素'''
        ele = self.findElement(locator)
        self.driver.save_screenshot("button.png")
        x1 = ele.location["x"]
        y1 = ele.location["y"]
        x2 = ele.location["x"]+ele.size["width"]
        y2 = ele.location["y"]+ele.size["height"]
        im = Image.open('button.png')
        im = im.crop((x1,y1,x2,y2))
        im.save("button.png")

    def get_text(self,locator):
        try:
            t = self.findElement(locator).text
            return t
        except:
            return " "

    def is_text_in_element(self,locator,text):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.jiangetime).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def get_ElementScreen(self,locator,name):
        ele = self.findElement(locator)
        driver.save_screenshot(name)
        # print(ele.location)
        # print(ele.size)
        x1 = ele.location["x"]
        y1 = ele.location["y"]
        x2 = ele.location["x"]+ele.size["width"]
        y2 = ele.location["y"]+ele.size["height"]
        im = Image.open(name)
        im = im.crop((x1,y1,x2,y2))
        im.save(name)


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://agent.sofang.com/majorLogin?type=2")
    basecls = Base(driver)
    locname = ("id","lproname")
    locpwd = ("id","lpropwd")
    locbutton = ("id","login")
    loc_get_name = ("css selector",".head_r>span")
    basecls.sendKey(locname,"15910304557")
    basecls.sendKey(locpwd,"123456")
    basecls.clickEle(locbutton)
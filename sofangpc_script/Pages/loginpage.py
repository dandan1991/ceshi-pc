import time
from selenium import webdriver
from common.base import Base

login_url = "http://agent.sofang.com/majorLogin?type=2"
class Login(Base):

    locname = ("id","lproname")
    locpwd = ("id","lpropwd")
    locbutton = ("id","login")
    loc_get_name = ("css selector", ".head_r>span")
    loc_get_err = ("id", "lpromsg")
    locgunbi = ("xpath", '//*[@class="no_id"]/div/h2/a')

    def inpu_username(self,name):
        self.sendKey(self.locname,name)

    def inpu_pwd(self,pwd):
        self.sendKey(self.locpwd,pwd)

    def click_button(self):
        self.clickEle(self.locbutton)

    def get_login_text(self,type,text):
        ''''''
        if type == "1":
            jieguo = self.is_text_in_element(self.loc_get_name,text)
            return jieguo
        elif type == "2":
            jieguo1 = self.is_text_in_element(self.loc_get_err,text)
            return jieguo1

# def jqlogin(driver
#     vars = '''
#            $('#lproname').val('15910304557')
#            $('#lpropwd').val('123456')
#            $('#login').click()
#            '''
#     driver.execute_script(vars)

    def logins(self,name,pwd,type,tishi):
        self.inpu_username(name)
        self.inpu_pwd(pwd)
        self.click_button()
        rees = self.get_login_text(type,tishi)
        print(rees)

    def denglu(self,name,pwd):
        self.inpu_username(name)
        self.inpu_pwd(pwd)
        self.click_button()
        time.sleep(2)
        self.is_element_be(self.locgunbi)
        self.clickEle(self.locgunbi)

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get(login_url)
    clslogin = Login(driver)
    clslogin.denglu("15910304557","123456")
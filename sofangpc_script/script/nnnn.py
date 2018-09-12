from selenium import webdriver
import time
import random
import mysql.connector
import json

class SqlDatas():
    def connectdatabase(self,hosts,users,passwds,databases):
        '''链接数据库
        hosts：数据库主机地址
        users：数据库用户名
        passwds：数据库密码
        databases：库名
        return：获得python执行Mysql命令的方法,也就是我们所说的操作游标
        '''
        mydb = mysql.connector.connect(
            # host= "192.168.1.85",
            # user= "admin",
            # passwd="abc.123",
            # database="sofang2017_user"
            host=hosts,
            user=users,
            passwd=passwds,
            database=databases
        )
        return mydb

    def data(self,mydb,sql):
        '''返回查询数据
        mycursor：python执行Mysql命令的方法,也就是我们所说的操作游标
        sql：查询语句
        :return 返回查询数据
        '''
         # sql = "SELECT * FROM brokers LIMIT 3"
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult

if __name__ == "__main__":
    clssql = SqlDatas()
    mydb = clssql.connectdatabase("192.168.1.85","admin","abc.123","sofang2017_user")
    sql = "SELECT mobile,realName FROM brokers LIMIT 3"
    user_data = clssql.data(mydb,sql)
    print(user_data)
